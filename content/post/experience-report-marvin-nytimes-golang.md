+++
author = "Sushant Srivastava"
date = "2017-09-01T02:50:27+05:30"
description = "Experience Report - NYTimes Marvin for building Microservices on Appengine"
draft = true
keywords = ["golang", "marvin", "experience-report"]
tags = ["golang", "marvin", "experience-report"]
title = "Experience Report - NYTimes Marvin for building Microservices on Appengine"
topics = ["golang", "marvin", "experience-report"]
type = "post"
+++

NYTimes recently open-sourced [Marvin](https://github.com/NYTimes/marvin), a library for building Microservices on Google AppEngine. The project is based off their earlier library [Gizmo](https://github.com/NYTimes/gizmo).
I was looking for a similar project to implement some of my own microservices, so I thought
that it was an opportune moment to give this toolkit a shot. 

By way of documentation, the repository has a sample application, `readinglist`, and its documentation is lacking.
The `README` page has bit description about the files. It took me a while to understand the machinations because
I had not worked on Gizmo earlier.

Marvin is a toolkit to implement Microservices which use protocol buffers or JSON as their communication format. First off, Marvin expects an [OpenAPI](https://www.openapis.org/) specification file. You can generate protobuf file which generates `.proto` file. [`openapi2proto`](https://github.com/NYTimes/openapi2proto) is another open source project from NYTimes which comes handy here.  You can then use the `.proto` file to generate Go code for services. Marvin `MixServices` interface gives you endpoints to implement protocol buffer and JSON Web Services. Here's a run-down of the workflow:

*  Write the `openapi` spec in a file, say `service.yaml`
*  Use `openapi2proto` to generate the service specification in Protobuf. The protobuf file has domain specific models from the openapi definitions.
*  Generate Go code for the service using protobuf compiler
*  Implement the service method, usually it is `marvin.MixService` which is an interface for implementing both `json` and `protobuf` services. I discovered `impl`, a utility to generate stub implementation for any interface. You can generate the stub implementation like so:
   ```
   impl 's Service' github.com/NYTimes/marvin.MixService
   ```
   You can then add custom middlewares, routing and Endpoints by implementing the methods from the interface.
* Write the usual `app.yaml` file for deploying the project on GAE. In the `main` function, bootstrap the service like so:

	```Go

	func main() {
		marvin.Init(api.NewService())
		log.Print("hello initialization")
		appengine.Main()
	}

	```
* Use the local setup to test
	```bash
	dev_appserver.py server/app.yml
	```
	
It took me a while to figure out the workflow. I liked the openapi-first approach for developing Microservice APIs. 
While `openapi2proto` generates the domain objects from the definitions file, it discards the endpoints information,
which you have to implement separately. It'd be nice to generate stub implementation from the `paths` section of
the spec file. To sum up:

* You can generate protobuf and JSON webservices is a huge plus.
* You can generate neat documentation from `swagger-gen` tool for your APIs.
* It'd be great if the tool also generated stub implementation for the endpoints using the `paths` information from 
the `openapi` spec file.

{{<figure src="/experience-report-marvin-golang.jpg" attr="" class="col-md-offset-3" attr="Experience Report">}}
