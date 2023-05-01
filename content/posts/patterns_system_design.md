+++
author = "Sushant Srivastava"
date = "2023-05-01"
description = "Patterns and Pattern Sequences for System Design"
draft = false
keywords = ["patterns", "design"]
tags = ["patterns", "design"]
title = "Such Stuff as Systems Are Made On: Patterns and Sequences for System Design"
topics = ["patterns", "design"]
type = "post"

+++

There is no handbook for Software Engineering.

Way back in 2006, when I started my development career, I was using the [Struts Web Framework](https://struts.apache.org/index.html "Struts Web Framework"). 
It was my gateway to web development, and I remember distinctly the MVC pattern based web framework.
I had not done any web development before, but the gurus at my workplace were all praise for the framework.
I could see their point when I worked with PHP and cgi.

After some years, when I started serious object-oriented development, I saw code-base structured around [Gang-of-Four Design Patterns](https://www.digitalocean.com/community/tutorials/gangs-of-four-gof-design-patterns "Gang-of-Four Design Patterns")
. I recall grokking their value after working with 10-odd code-bases. It changed how I approached code-bases
and new feature design. I looked for opportunities to use them.

{{< figure src="/images/patternsEverywhere.png" >}}

Formally, a design pattern is a proven solution to a recurring problem in software development. 
A pattern sequence is a series of design patterns that work together to solve a complex problem.
Note that the terminology can be slightly different depending on who you're speaking with. For example, 
the authors in [Software Architecture in Practice](https://www.oreilly.com/library/view/software-architecture-in/9780132942799/ "Software Architecture in Practice") call the recurring solution **tactics**, 
and sequences of these tactics - **patterns**.
Despite the terminology, if you spoke with someone who have "been around", they're likely to extol the virtues of design patterns.

The Cloud Devs have also caught up with the patterns. I have not been keeping up in this area, and I thought it would be a good 
opportunity to see around now that the cloud practices have crystallized into patterns. Here are the common patterns that I came across:


## Microservices Pattern 

[Microservices Patterns](https://microservices.io/patterns/index.html "Microservices Patterns") is a catalog of patterns for implementing
Microservices. Microservices are the *defacto* strategy for implementing the services or solution. The collection is comprehensive discussing important
topics like Transaction management across different services.   

## API Design Patterns

[API Patterns for Microservices](https://microservice-api-patterns.org/patterns/ "API Patterns for Microservices") is an index of patterns 
for implementing Microservices API. Implementing API is not limited to modeling domains as resources and throwing a REST API on top of it.
API design is a thoughtful endeavor. It *should* be. What I like about the list is that it gives a starting point for discussing such problems as 
whether the API is a meant to be consumed internally or if it is a public API. The constraints on these use cases are different.

## Cloud Architecture Design Patterns

[Azure Cloud Architecture Patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/ "Azure Cloud Architecture Patterns") is a list of 
patterns for architecting solution on the Azure Cloud Family. The list of patterns is cloud-agnostic. You will find that the cloud families have their own 
notion of "Well Architected Solution". At the same time, there are common patterns that are applicable across the board. As it should be obvious, there is a lot of 
overlap between the cloud architecture patterns list and Microservices Patterns Catalog because a majority of cloud services follow the Microservices pattern for 
implementing their solutions.

## Distributed Systems Design Patterns
Reading technical papers on Systems by big tech companies give you an impression that the problems are unique to each of them. For example, Chubby, Zookeeper, and Etcd
are systems design for starkly similar use cases but they differ in their implementations and constraints. [Patterns of Distributed Systems](https://martinfowler.com/articles/patterns-of-distributed-systems/ "Patterns of Distributed Systems")
is a collection of patterns that condenses patterns for implementing such distributed system primitives like Replication logs.

The Application Developers rarely get an insight into the underpinnings of distributed system primitives like a config store, but knowing the primitives and options available give them
an opportunity to calibrate their options and make informed trade-offs.

## Messaging Design Patterns

[Messaging Design Patterns](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ "Messaging Design Patterns") is a list of patterns for designing messaging based systems.
This is the oldest collection in the list, but it has come on its own after Microservices-ssance. This is because the different Microservices rely on messaging asynchronous or synchronous, to communicate with 
one another. While ESBs have been around a lot longer, streaming-based microservices, and Messaging Products like Camel that provide these patterns out of the box have brought the discussion of these patterns to fore now.


How is knowing these patterns helpful? Is this not overwhelming? It might be so, but in my opinions the benefits outweigh the cons. Speaking a common language for your solution is your gateway to getting your point across.
This, assuming that the person or the group of people you are presenting or knowledgeable in patterns and are already sold on them, having seen their benefits in the past. 
