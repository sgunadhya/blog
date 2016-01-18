+++
title =  "Design Rules for Data Mining Algorithms : A Tryst with Modularity"
slug =  "design-rules-for-data-mining-algorithms-a-tryst-with-modularity"
date =  "2015-06-03"
tags =  ["machine learning", "modularity"]
category =  ["machine learning"]
summary =  "Modular Data Mining Algorithms."
+++

I took a few Machine Learning courses, and most of them introduced ready-made toolboxes
in languages like R and Python. These ready-made toolboxes are good as long as we do
not dig deep into the nitty-gritties of the algorithm. Most of the software packages present Machine Learning tasks as a monolithic
subroutine which makes it harder, if not impossible, to customize their operations except maybe change a parameter to the subroutine itself. These software
packages are not *modular*.

Modular software architectures are evolvable, easy to analyse and upgrade. In the book Design Rules [Baldwin]_, the authors outline the benefits of
modularity with six modular operators for modular designs - Splitting, Substitution, Augmenting, Excluding, Inversion, and Porting. *Splitting* and *Substitution* are complementary operators which allow interconnected task to be split into independent tasks and evolve separately or replaced by a performant module. Similarly, *Augmenting* and *Excluding* are complementary operators which can enhance an already existing design by adding a helper module or taking away a redundant module from the design. *Inversion* and *Porting* allow a design to move common modules reusable across all the other modules. These are good thumbrules for designing modular systems and some framework like `Guice <https://github.com/google/guice/wiki/GettingStarted>`_ make it easier to apply these to software design than others.



1. **Task**
   The data mining task the algorithm uses. It could be - regression, classification, clustering etc.

2. **Structure**
   The functional form of the model we are fitting our data to.

3. **Score Function**
   It is used to judge the quality of the fitted models. We usually try to minimize or maximize this function.

4. **Search Method**
   The search heuristic or the optimization method we use to maximize or minimize our Score Function.

5. **Data Management Techniques**
   Data Management technique is one of the most ignored aspects of Machine learning algorithms.
   This is where Computational Resources at hand come into picture. Massive datasets can change the
   game of the machine learning procedure.


+-------------------------------+-------------------------------+--------------------------------+----------------------------+------------------------------------------------------------------+
|                               | CART                          | Backpropagation                | A Priori                   | Vector Space for Text Retrieval                                  |
+===============================+===============================+================================+============================+==================================================================+
| **Task**                      | Classification and Regression | Regression                     | Rule Pattern Discovery     | Retrieval of similar documents in a database relative to a query |
+-------------------------------+-------------------------------+--------------------------------+----------------------------+------------------------------------------------------------------+
| **Structure**                 | `Decision Tree`_              | `Neural Network`_              | Association Rules          | Vector of Term Occurrences                                       |
+-------------------------------+-------------------------------+--------------------------------+----------------------------+------------------------------------------------------------------+
| **Score Function**            | Cross-Validated Loss Function | Squared Error                  | Support/Accuracy           | Angle between two vectors                                        |
+-------------------------------+-------------------------------+--------------------------------+----------------------------+------------------------------------------------------------------+
| **Search Method**             | Greedy search over Structures | Gradient Descent on Parameters | Breadth-first with Pruning | Various Techniques                                               |
+-------------------------------+-------------------------------+--------------------------------+----------------------------+------------------------------------------------------------------+
| **Data Management Technique** | Unspecified                   | Unspecified                    | Linear Scans               | Fast Indexing Techniques                                         |
+-------------------------------+-------------------------------+--------------------------------+----------------------------+------------------------------------------------------------------+




.. [Baldwin] `Baldwin, Carliss Young. Design Rules. Cambridge, Mass.: MIT Press, 2000. Print. <http://www.amazon.com/Design-Rules-Vol-Power-Modularity/dp/0262024667>`_

.. [2] `Hand, D. J, Heikki Mannila, and Padhraic Smyth. Principles Of Data Mining. Cambridge, Mass.: MIT Press, 2001. Print.`_

.. _`Decision Tree`: http://scikit-learn.org/stable/modules/tree.html
.. _`Neural Network`: http://scikit-learn.org/stable/modules/neural_networks.html
.. _`Hand, D. J, Heikki Mannila, and Padhraic Smyth. Principles Of Data Mining. Cambridge, Mass.\: MIT Press, 2001. Print.`: http://www.amazon.co.uk/Principles-Adaptive-Computation-Machine-Learning/dp/026208290X/ref=sr_1_1?s=books&ie=UTF8&qid=1434103925&sr=1-1&keywords=Principles+of+data+mining

