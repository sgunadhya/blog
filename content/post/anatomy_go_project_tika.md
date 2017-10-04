+++
author = "Sushant Srivastava"
date = "2017-10-04T02:50:27+05:30"
description = "Decontructing a Golang Project - go-tika"
draft = true
keywords = ["golang", "libraries", "analysis"]
tags  = ["golang", "libraries", "analysis"]
title = "Deconstructing a Golang Project - go-tika"
topics = ["golang", "libraries", "analysis"]
type = "post"
+++

I am learning Golang, and I try to analyze open source Golang repositories to learn patterns and idiomatic usage. I came across the library [go-tika]() by a team at Google, and I found it to be a perfect fit for analysis because it is a small-enough but not a toy project. I have decided to document what I learn for posterity and to gather feedback from people who are already good at Golang.

`go-tika` is command line utility and a library to interface with an external [Apache Tika Server](). It is a common pattern among the 
Golang projects to have a core library code as well as a command line code which makes use of the library. You can call the core library component as the core api of the project and the command line component as the UI which uses the core library component. So, there are two components - 

1. *The Core Library Component* This component is the crux of the Golang project. It contains the meat of the project. The core library us structured in such a way that the client can import the library and use all the exported API in their projects.

2. *The Command Component* This component is the UI of the project. It imports the core component APIs and provides a command line interface. This is the component which is compiled to generate an executable. 

So, let's analyze the library. `go-tika` is a golang library to talk to an external server or program. The project structure is:

```
<Root Directory>



```
The core library can also be viewed as consisting of two components 

1. *The Server Component* The Server Component is responsible for starting the external program or server. Optionally, the server component can also download the server or the program binaries from the internet; super convenient.

2. *The Client Component* This is the main component which is responsible for issuing commands to the server. In this case the server exposes a RESTful API, so the client is an HTTP client.

Let start with the Server component. If you peruse the file `server.go`, you will find these notable exported API methods and symbols:
* `type Option`
 * `func WithHostname(h string) Option`
 ...
 
* `type Server`
 * `func NewServer(jar string, options ...Option) (*Server, error)`
 * `func (s *Server) Start(ctx context.Context) (cancel func(), err error)`
 ...
 
 In the file `server.go`, the server options are modeled as a struct with these fields
 
 ```
 type Server struct {
	jar            string
	url            string // url is derived from port and hostname.
	port           string
	hostname       string
	cancel         func()
	startupTimeout time.Duration
}
 
 ```
 `jar`, `url`, `port`, `hostname` are the usual suspects; these are the options to locate and run the server. `cancel` is a something dissimilar. `cancel` is a function which when called cancels the execution of the context. This is a common pattern provided by the APIs which
 support passing in a `context`. By returning a `cancel` function, the API offers an opportunity to the calling function to suspend the execution. You can find more information about using contexts in the execellent [blog post](https://blog.golang.org/context).

