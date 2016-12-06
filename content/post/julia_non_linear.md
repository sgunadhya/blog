+++
author = "Sushant Srivastava"
date = "2016-11-21T12:49:51+05:30"
description = "Using Julia for Non Linear Optimization"
draft = false
keywords = ["julia", "optimization"]
tags = ["julia", "optimization"]
title = "Using Julia for Non Linear Optimization"
topics = ["optimization"]
type = "post"

+++

In a [previous post](https://www.ssushant.in/2016/09/10/using-julia-for-linear-programming/), I discussed using Julia for Linear Programming. It turns out, Julia's JuMP package can also be used for Non linear optimization and root finding.

To use JuMP's non linear solvers, you'll need to install a non linear solver package, for example `Ipopt`.

```
Pkg.add("Ipopt")
```

On my mac, Julia installed the non linear optimization package `ipopt` using `homebrew`.

Let's try to solve an unconstrained optimization problem - find the minimum of `-80*x^2 + 26000*x -2000000`.

First, we load the `JuMP` package like so:

```
using JuMP
```

We model the problem:

```

using Ipopt

m = Model(solver=IpoptSolver())
@variable(m, x)
@NLobjective(m, Max, -80*x^2 + 26000*x -2000000)

```
As you can see, you'll need to pass the custom solver `IpoptSolver` to the model.

Next, we try to find the optimum solution


```
solve(m)

```

Here's the output from my workstation:


```
This is Ipopt version 3.12.4, running with linear solver mumps.
NOTE: Other linear solvers might be more efficient (see Ipopt documentation).


Number of nonzeros in equality constraint Jacobian...:        0
Number of nonzeros in inequality constraint Jacobian.:        0
Number of nonzeros in Lagrangian Hessian.............:        1

Total number of variables............................:        1
                     variables with only lower bounds:        0
                variables with lower and upper bounds:        0
                     variables with only upper bounds:        0
Total number of equality constraints.................:        0
Total number of inequality constraints...............:        0
        inequality constraints with only lower bounds:        0
   inequality constraints with lower and upper bounds:        0
        inequality constraints with only upper bounds:        0

iter    objective    inf_pr   inf_du lg(mu)  ||d||  lg(rg) alpha_du alpha_pr  ls
   0  2.0000000e+06 0.00e+00 1.00e+02  -1.0 0.00e+00    -  0.00e+00 0.00e+00   0
   1 -1.1250000e+05 0.00e+00 0.00e+00  -1.0 1.62e+02    -  1.00e+00 1.00e+00f  1

Number of Iterations....: 1

	   (scaled)                 (unscaled)
Objective...............:  -4.3269230769230774e+02   -1.1250000000000000e+05
Dual infeasibility......:   0.0000000000000000e+00    0.0000000000000000e+00
Constraint violation....:   0.0000000000000000e+00    0.0000000000000000e+00
Complementarity.........:   0.0000000000000000e+00    0.0000000000000000e+00
Overall NLP error.......:   0.0000000000000000e+00    0.0000000000000000e+00


Number of objective function evaluations             = 2
Number of objective gradient evaluations             = 2
Number of equality constraint evaluations            = 0
Number of inequality constraint evaluations          = 0
Number of equality constraint Jacobian evaluations   = 0
Number of inequality constraint Jacobian evaluations = 0
Number of Lagrangian Hessian evaluations             = 1
Total CPU secs in IPOPT (w/o function evaluations)   =      0.001
Total CPU secs in NLP function evaluations           =      0.000~

EXIT: Optimal Solution Found.
:Optimal

```

From the output, it looks like we found the optimal solution.

To show the value of x at the optimum point, we use the `getvalue` function.

```
julia> getvalue(x)
162.5

```

In this post, I used the `JuMP` package for non linear optimization.
JuMP is a convenient and useful tool and should be in every modeler's toolbox.
It is turning out to be an uber package for optimization. I'll continue blogging
as I explore the JuMP package.



