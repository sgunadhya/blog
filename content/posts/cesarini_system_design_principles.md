+++
author = "Sushant Srivastava"
date = "2016-09-30T17:55:38-04:00"
description = "Using Cersarini's design Guidelines for building a system"
draft = true
keywords = ["system", "design", "principles"]
tags = ["system", "design", "principles"]
title = "cesarini_system_design_principles"
topics = ["System Design"]
type = "post"

+++

{{<figure src="/orrery.jpg" attr="" class="col-md-offset-3" attr="Photo from Wikipedia : Faithful photographic reproduction of a two-dimensional, public domain work of art.">}}


1.Split up your system’s functionality into manageable, standalone nodes.

* what is functionality
* what is node
* why standalone
* how to split up
* why split-up
* when split-up
* How did you get this idea to split up your application
* An example about splitting up your application
* A wrong way to split up your application
* Why is it a wrong way, what is the correct way

2.Choose a distributed architectural pattern.

* Which architectural pattern
* why architectural pattern
* Why this choice

3.Choose the network protocols your nodes, node families, and clusters will use when communicating with each other.

* How to choose a protocol
*

4.Define your node interfaces, state, and data model.

4.For every interface function in your nodes, pick a retry strategy.

* What is a retry strategy?
* How to choose a retry strategy
* What happens if you choose a wrong retry strategy
* An example of a good retry strategy

6.For all your data and state, pick your sharing strategy across node families, clusters, and types, taking into consideration the needs of your retry strategy.

* How is *retry strategy* dependent on sharing strategy?
* What is sharing strategy?
* how to choose a sharing strategy
* What happens if you choose a wrong sharing strategy

7.Design your system blueprint, looking at node ratios for scaling up and down.

* What is a node ratio?
* What is a system blueprint

8.Identify where to apply backpressure and load regulation.

9.Define your OAM approach, defining system and business alarms, logs, and metrics.

10.Identify where to apply support automation.
