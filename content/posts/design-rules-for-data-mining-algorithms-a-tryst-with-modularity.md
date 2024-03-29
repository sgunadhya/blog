+++ 
title = "Design Rules for Data Mining Algorithms : A Tryst with Modularity" 
slug = "design-rules-for-data-mining-algorithms-a-tryst-with-modularity" 
date = "2015-06-03" 
tags = ["machine learning", "modularity"] 
category = ["machine learning"] 
description = "Modular Data Mining Algorithms." 
author = "Sushant Srivasta"
+++

I took a few Machine Learning courses, and most of them introduced
ready-made toolboxes in languages like R and Python. These ready-made
toolboxes are good as long as we do not dig deep into the nitty-gritties
of the algorithm. Most of the software packages present Machine Learning
tasks as a monolithic subroutine which makes it harder, if not
impossible, to customize their operations except maybe change a
parameter to the subroutine itself. These software packages are not
*modular*.

Modular software architectures are evolvable, easy to analyse and
upgrade. In the book Design Rules \[Baldwin\]\_, the authors outline the
benefits of modularity with the following six operators for modular designs:

1. Splitting
2. Substitution
3. Augmenting
4. Excluding
5. Inversion
6. Porting


*Splitting* and *Substitution* are complementary operators which allow
interconnected task to be split into independent tasks and evolve
separately or replaced by a performant module. Similarly, *Augmenting*
and *Excluding* are complementary operators which can enhance an already
existing design by adding a helper module or taking away a redundant
module from the design. *Inversion* and *Porting* allow a design to move
common modules reusable across all the other modules. These are good
thumbrules for designing modular systems and some framework like
[Guice](https://github.com/google/guice/wiki/GettingStarted) make it
easier to apply these to software design than others.

1.  **Task** The data mining task the algorithm uses. It could be -
    regression, classification, clustering etc.
2.  **Structure** The functional form of the model we are fitting our
    data to.
3.  **Score Function** It is used to judge the quality of the
    fitted models. We usually try to minimize or maximize this function.
4.  **Search Method** The search heuristic or the optimization method we
    use to maximize or minimize our Score Function.
5.  **Data Management Techniques** Data Management technique is one of
    the most ignored aspects of Machine learning algorithms. This is
    where Computational Resources at hand come into picture. Massive
    datasets can change the game of the machine learning procedure.


| **Name**                               | **Task**                       | **Structure**             | **Score Function**           | **Search Method**              | **Data Management Techniques** |
| -------------------------------------- | ------------------------------ | ------------------------- | ---------------------------- | ------------------------------ | ------------------------------ |
| CART                                   | Classification and Regeression | Decision Tree             | Cross-Validted Loss Function | Greedy Search Over Structures  | Unspecified                    |
| Backpropagation                        | Regression                     | Neural Network            | Squared Error                | Gradient Descent On Parameters | Unspecified                    |
| A Priori                               | Rule Pattern Discovery         | Association Rules         | Support/Accuracy             | Breadth-first Search           | Linear Scans                   |
| Vector Space for Information Retrieval | Retrieval of Similar Documents | Vector of Term Occurences | Angle Between Two Vectors    | Various Techniques             | Fast Indexing Techniques       |
