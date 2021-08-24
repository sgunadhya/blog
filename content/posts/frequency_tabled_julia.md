+++
author = "Sushant Srivastava"
date = "2016-12-17T20:33:02+05:30"
description = "Generating Frequency tables in Julia"
draft = false
keywords = ["julia", "frequency", "two way tables", "prop.tables"]
tags = ["julia", "frequency", "two way tables", "prop.tables"]
title = "Frequency Tables in Julia"
topics = ["julia", "frequency", "two way tables", "prop.tables"]
type = "post"

+++

[R](https://www.r-project.org/about.html) has a [number of methods](http://www.statmethods.net/stats/frequencies.html) to calculate Frequency tables. I was surprised to find out that there wasn't any straight forward method to compute two way tables. My Google search led me to this [Github issue](https://github.com/JuliaStats/StatsBase.jl/issues/32). The last comment led me to the useful package from [nalimilan](https://github.com/nalimilan).


[FreqTable](https://github.com/nalimilan/FreqTables.jl) is a package for Julia to compute Contingency tables or Frequency tables.
The installation is a straightforward `Pkg.add`. Here's some usage examples:


```julia
using FreqTables

table = freqtable(dataset,[:x, :y])

table(x=1, y=2)

```
