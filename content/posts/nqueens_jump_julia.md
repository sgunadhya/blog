+++
author = "Sushant Srivastava"
date = "2020-04-04T02:50:27+05:30"
description = "N-Queens Problem and the JuMP Package"
draft = false
keywords = ["julia", "optimization"]
tags = ["julia", "optimization"]
title = "N-Queens Problem and the JuMP Package"
topics = ["julia", "optimization"]
type = "post"
+++

In the past I discussed about using the [JuMP Package](http://www.ssushant.in/2016/09/10/using-julia-for-linear-programming/) for solving an optimization problem.
Recently I came across another problem that seemed like a good fit for the
JuMP Package - The N-Queens puzzle.

## Summary of the N-Queens Puzzle
So what is the N-Queens puzzle?

Imagine you have a chessboard and eight queens with you. 
The challenge is to place the queens in such a way that they do not
attack each other with their usual moves.

## Solution of the N-Queens Puzzle

This code listing is an attempt at solving the puzzle using the `JuMP` package
from Julia:

```jl {linenos=table,linenostart=1}
using JuMP, GLPK, Gadfly
N=8
model = Model(GLPK.Optimizer);
@variable(model, board[1:N,1:N], binary=true)
@objective(model, Max, sum( board[i,j] for i in 1:N, j in 1:N))

for j in 1:N
    @constraint(model, sum(board[i,j] for i in 1:N) == 1)
end
for i in 1:N
    @constraint(model, sum(board[i,j] for j in 1:N) == 1)
end

for k in 2:2*N
    @constraint(model, 
    sum(board[i,j] for i in 1:N, j in 1:N if i+j == k) <= 1)
end

for k in -(N-1):(N-1)
    @constraint(model, 
    sum(board[i,j] for i in 1:N, j in 1:N if i-j == k) <= 1)
end

print(model)
optimize!(model)
spy(JuMP.value.(board))
```
* Line 1 is about importing the required packages. We're using `JuMP` for formulating our 
  linear programming problem, `GLPK` is one of the solvers available in Julia. `Gadfly` is used
  to visualize our result.

* In line 2 we parameterize our Chess board.

* In line 3 we define our model. We are asking `JuMP` to create a model with the `GLPK` optimizer.

* In line 4 we model our Chessboard as a grid of an 8x8 matrix. Each cell in the matrix represents a square on the chess board. The cell has a value of 1 or 0 indicating whether the queen should be placed in the square or not.

* In lines 7-9 we specify our first constraint. What we are saying here is that no two queens should be placed in the same column.
  This is because queens in the same column can attack each other.

* In lines 10-12 we specify our second constraint. What we are saying here is that no two queens should be placed in the same row.
* In lines 14-22 we are saying that no two queens should be in the same diagonal.
* In line 25, we set the solver in motion using the `optimize!` command.
* In line 26, we visualize the result using the BinaryMatrix visualization command `spy` from the `Gadfly` package.

## What does Solving an Optimization Problem like N-Queens Entail?

N-Queens puzzle can be formulated as a linear programming problem.
In this class of problems we model the puzzle and constraints as 
set of linear expressions. There are other ways of solving this problem,
for example, using brute force method. There are many advantages of expressing
the problem in an abstract linear program.

There are two styles of programming - Procedural and Declarative. In procedural
programs we specify the path that the solver should take to find the solution
to the program. We specify a series of steps and the computer takes them in the specified order.
 In declarative programs, on the other hand, the problem is specified in a
domain-specific language and a solver or planner does all the hard work of finding
a solution.

When you write a Java program to find the root of an equation using Newton-Raphson
or other method, you are using a procedural style of programming.

When you are querying a relational database using an SQL-like language, you are using
a declarative style of programming.

Two thing stand out when you use a declarative style of programming.

1. Knowledge of the domain-specific language

	When you use declarative style, you should know the DSL. For example, when you query
	a database, you should be able to formulate a query.

2. You should be able to translate your problem into the language of the domain

	Modeling is the name of the game, and over the course of time I have realized
	that it is more of an art than an exact science. 

Another convenience that Julia offers is that we don't have to understand the underlying
solver which solves the Linear Programming problem. The solvers use an algorithm like
the [Simplex Algorithm](http://fourier.eng.hmc.edu/e176/lectures/NM/node32.html) to solve these problems. 

## A similar problem - The Confused Queens

I came across a similar puzzle which is an antithesis of the original N-Queens puzzle -
The confused Queens puzzle, or what I would like to call as "Everybody was Chess-fu fighting".
Here we have to find an arrangement where all the Queens **do** attack each other. That's for later!
