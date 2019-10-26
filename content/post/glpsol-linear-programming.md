+++
author = "Sushant Srivastava"
date = "2016-04-28T15:14:33+05:30"
description = "Using GLPK to solve knapsack and related problems"
draft = false
keywords = ["glpsol", "glpk"]
tags = ["linear programming", "optimization"]
title = "Using GLPK to solve knapsack and related problems"
topics = ["Linear Programming"]
type = "post"

+++
I am taking a course in Supply Chain management from Edx. The transport-network problem in the Supply chain management domain maps
directly with the network flow problem. The course recommends using Excel to formulate and solve the model problems.
I never had a knack for Excel and while I find it useful for some use cases, I prefer programming using a text editor. I would rather work out numeric problems with R or Python than write formulae and values in cells in Excel. I was looking for an open source alternative to formulate and solve the network flow problems so that I can avoid the drudgery of dealing with Excel spreadsheets.

I came across the `glpk` library for solving linear programs such as Network flow problems. GLPK uses MathProg as its programming
language. You specify your variables, objective function, and constraints in MathProg, run the `glpsol` command providing the MathProg file as
an input, and the solver outputs a solution if the solution exists. The constraints and the objective function are specified using a math-like
notation for inequalities. Here is a sample MathProg specification ::

{{< highlight ampl >}}
  set Items;
  param weight{t in Items};
  param value{t in Items};
  param quantity{t in Items};

  var take{t in Items}, integer, >=0, <=quantity[t];
  maximize knap_value: sum{t in Items} take[t] * value[t];
  s.t. knap_weight : sum{t in Items} take[t] * weight[t] <= 25;
  s.t. knap_vol    : sum{t in Items} take[t] * volume[t] <= 0.25;


 {{< / highlight >}}

This is a specification for a knapsack problem. We are maximizing the value of the items in the knapsack subject to the constraint the total weight does exceed 400.
The expression `knap_value` is the objective function which is the value of the items. The expression `knap_weight` is the constraint.

Next, we'll need to provide the `.dat` file as data. We can structure the file like so:

{{< highlight apl >}}
data;

param : Items   : weight   value     volume :=
         A      0.3        3000      0.025
         B      0.2	       1800	     0.015
         C		  2.0	       2500      0.002
;
end;

 {{< / highlight >}}

We can solve the Knapsack problem like so:

 {{< highlight bash >}}
    glpsol --model knapsack.mod --data knapsack.dat -o result
 {{< / highlight >}}

The file `result` produced as a result of the `glpsol` command will have the details about the solution, if a solution exists.


[1] http://rosettacode.org/wiki/Knapsack_problem/Bounded#Mathprog
