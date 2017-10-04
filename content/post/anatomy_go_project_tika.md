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
