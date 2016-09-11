+++
author = "Sushant Srivastava"
date = "2016-09-10T01:55:45+05:30"
description = "JuMP DSL for optimization problems"
draft = false
keywords = ["linear programming", "optimization"]
tags = ["linear programming", "optimization"]
title = "Using Julia for Linear Programming"
topics = ["optimization"]
type = "post"

+++

In a [previous post](http://www.ssushant.in/2016/04/28/using-glpk-to-solve-knapsack-and-related-problems/), I discussed using GLPK to solve a linear programming problem. GLPK is a tailor-made tool to solve linear and mixed integer linear programs. I came across Julia's [JuMP module ](https://jump.readthedocs.io/en/latest/) which is a domain-specific language for modelling optimization problems. The scope of JuMP is wide - Linear optimization, Non-linear optimization, and Semi-definite optimization etc. As an example, I tried translating my previous optimization program to JuMP's DSL.


```julia
using JuMP
items = ["A", "B", "C"]
weight = Dict("A" => 0.3, "B" => 0.2, "C" => 2)
value = Dict("A" => 3000, "B" => 1800, "C" => 2500)
volume = Dict("A" => 0.025, "B" => 0.15, "C" =>  0.002)
m = Model()
@variable(m, take[items] >= 0, Int)
@objective(m, Max,sum{take[i]*value[i], i=items})
@expression(m, knap_weight, sum{take[i]*weight[i], i=items})
@expression(m, knap_volume, sum{take[i]*volume[i], i=items})
@constraint(m, knap_weight <= 25)
@constraint(m, knap_volume <= 0.25)
print(m)
status = solve(m)
print(getvalue(take))
```

    Max 3000 take[A] + 1800 take[B] + 2500 take[C]
    Subject to
     0.3 take[A] + 0.2 take[B] + 2 take[C] ≤ 25
     0.025 take[A] + 0.15 take[B] + 0.002 take[C] ≤ 0.25
     take[i] ≥ 0, integer, ∀ i ∈ {A,B,C}
    take: 1 dimensions:
    [A] = 9.0
    [B] = 0.0
    [C] = 11.0


Few things to notice:

* The syntax is programming language-like. JuMP programs are Julia Programs and therefore they can use Julia's programming language data structures like dictionaries.
* You can easily integrate the problem in a larger program. It is not straightforwrd to integrate a GLPK based script in a larger program.
* JuMP supports a lot of optimization routines, and the syntax for specifying them is similar. There's an advantage learning JuMP's DSL for optimization problems.
* The expression syntax is MathProg-like, so there is direct mapping from MathProg based GLPK programs to JuMP based DSL when specifying Linear or Mixed Integer programs.

I found that the DSL is easy to learn and I was able to translate the problem in a short time. I defintely see an advantage in learning Julia which is quickly becoming a mainstream language in academic circles overtaking Matlab.


