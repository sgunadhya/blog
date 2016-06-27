+++
author = "Sushant Srivastava"
date = "2016-06-28T02:50:27+05:30"
description = "Using Figaro for Probabilistic Modeling"
draft = false
keywords = ["machine learning", "Probabilistic"]
tags = ["machine learning", "Probabilistic"]
title = "figaro_probabilistic_programming"
topics = ["machine learning"]
type = "post"

+++

Beau Cronin on his [Google+ post](https://plus.google.com/+BeauCronin/posts/KpeRdJKR6Z1) gives a good explanation of what probabilistic
programming is, and why it matters. There are many probabilistic programming languages and tools, and I recently
came across [Figaro](https://www.cra.com/work/case-studies/figaro). Figaro is a [Scala](http://www.scala-lang.org/) library for probabilistic programming. Figaro programs are written in Scala, which means they can take full advantage of using Scala's programming constructs.

Suppose you want to model the roll of a six sided die. In probability problems, it is usually modeled as a [Random Variable](https://en.wikipedia.org/wiki/Random_variable) which
can take any value from 1 to 6. In Figaro you can model it like so:

```scala
 val dieRoll = FromRange(1, 7)
```

You can also model discrete as well as continuous random variables using Figaro. Figaro
programs are structured using Model, Evidence and Inference stages. You model your problem using Figaro's stochastic
models, add evidence, constraints or conditions, and then use one of the many inference algorithms from Figaro to draw inferences.

In this example, I am modeling an experiment where a six-sided die is rolled twice, and we want to infer the probability of
getting a sum of 11.

```scala
import com.cra.figaro.language.Apply
import com.cra.figaro.library.atomic.discrete.{FromRange}
import com.cra.figaro.algorithm.factored.VariableElimination;


object HelloWorld {
  def main(args: Array[String]): Unit = {
    val firstDie = FromRange(1, 7)
    val secondDie = FromRange(1, 7)
    val total = Apply(firstDie, secondDie, (firstDieResult: Int, secondDieResult: Int) => firstDieResult + secondDieResult)
    println(VariableElimination.probability(total, 11))
  }
}
```

`Apply` is a Figaro construct to model operations using Random variable, like in this example we're interested in Sum of the two
Random variables.

Figaro is a convenient library, and I like it because the programs written is Figaro are expressive. There are other useful features
like modeling Bayesian Nets which I'll explore further.
