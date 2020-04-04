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

In the past I discussed about using [JuMP Package](http://www.ssushant.in/2016/09/10/using-julia-for-linear-programming/) for solving optimization problem.
Recently I came across another problem that seemed like a good fit for the
JuMP Package - The N-Queens Problem.

## Summary of the N-Queens Problem

## Solution of the N-Queens Problem


## What does Solving an Optimization Problem like N-Queens Entail

Modelling is the name of the game, and over the course of time I have realized
that it is more of an art than an exact science. 

The convenience that Julia offers is that we don't have to understand the underlying
solver which solves the Linear Programming problem. The solvers use an algorithm like
the [Simplex Algorithm](http://fourier.eng.hmc.edu/e176/lectures/NM/node32.html) to solve these problems. 
## A similar problem - The Confused Queens

I came across a problem which is an antithesis of the original N-Queens Problem
- The confused Queens problem, or what I would like to call as "Everybody was Chess-fu fighting".
In this problem we have to find an arrangement where all the Queens