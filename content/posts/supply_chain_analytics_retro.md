+++
author = "Sushant Srivastava"
date = "2016-12-30T02:16:33+05:30"
description = "Retrospective on the course - Supply Chain Analytics"
draft = false
keywords = ["retro", "supply chain"]
tags = ["retro", "supply chain"]
title = "Supply Chain Analytics Edx Course - A Retrospective"
topics = ["retro", "supply chain"]
type = "post"

+++

I enrolled in the course "[Supply Chain Analytics](https://www.edx.org/course/supply-chain-analytics-mitx-ctl-sc0x-0)" from MIT on Edx. The course was about analytical methods that are useful to Supply Chain Professionals in their line of work. The course entailed Mathematical Modeling and Reasoning about uncertainty using the calculus of Probability. Here are my notes from the course and some salient points:


#### Linear Programming

Supply Chain Designers make use of Linear programming for designing delivery network with the shortest route or other properties.
I had [used glpk](https://www.ssushant.in/2016/04/28/using-glpk-to-solve-knapsack-and-related-problems/) in the past for solving linear programming problems like shortest path. Recently, I came across Julia's excellent JuMP package for optimization. The package uses Julia's metaprogramming
chops to create a DSL for optimization. An added advantage is that when we use the package, we have Julia's excellent libraries and programming constructs at our disposal. I blogged about some of them as well:

 * [Using Julia for Linear Programming](https://www.ssushant.in/2016/09/10/using-julia-for-linear-programming/)
 * [Using Julia for Non Linear Optimization](https://www.ssushant.in/2016/11/21/using-julia-for-non-linear-optimization/)


#### R

[R](https://www.r-project.org/about.html) is the language **du jour** of statisticians. If you happen to use a statistical workflow, it is very likely that someone has written an R package for it.

 * A helpful introduction about the analysis of [Categorical Variables](http://courses.ncssm.edu/math/Stat_Inst/PDFS/Categorical%20Data%20Analysis.pdf). [PDF Alert]
 
#### Discrete Event Simulation

An excellent revelation in the course was discovery of R's [simmer package](r-simmer.org/reference/index.html) for building discrete event simulation models, especially Queuing theory models. The course's original recommendation was [Anylogic](http://www.anylogic.com/), but I was looking for a library or package which gives programmatic control. I came across [SimPy](https://simpy.readthedocs.io/) and [SimJulia](simjuliajl.readthedocs.io/en/stable/welcome.html), both of which are excellent packages, but I found R's simmer package closer to what I was looking for. Simmer's workflow is focused around Resources and trajectory which takes some time to get used to, but it has [excellent documentation](http://r-simmer.org/articles/A-introduction.html).


I made a notes-like draft for skimming through important concepts. You can find the document here: [SCA-Notes](/notes-supply-chain-analytics.pdf)

Overall, I found the course insightful.

