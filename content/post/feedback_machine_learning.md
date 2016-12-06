+++ 
title = "Test Driven Development for Machine Learning projects" 
date= "2014-12-29" 
tags = [ "machine learning", "tdd"] 
keywords = [ "machine learning"] 
topics = ["machine learning"] 
slug = "tdd-machine-learning" 
description = "Seam testing, cross validation and graphing precision/recall are the TDD equivalents for a machine learning project." 
author = "Sushant Srivastava"
type="post"
+++

I use Test Driven Development (TDD) when developing a new software. TDD
is a useful technique for validating assumptions and refactoring the
code. I was wondering what TDD paradigm would work best for a Machine
Learning project. I read up on the subject and I am jotting down my
findings from various sources - books, Quora answers and simple
browsing.

Testing Input and Output data
=============================

Many Machine learning algorithms expect input data in a particular
format, and produce data in a specific format. We can test if the input
and the output data conform to these formats.
[Scikit-Learn](http://scikit-learn.org/stable/) provides [helper methods
for validating input
data](https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/validation.py).

Cross Validation
================

Two risks with machine learning models are -
[Overfitting](https://www.quora.com/What-is-an-intuitive-explanation-of-overfitting)
and
[Underfitting](http://datascience.stackexchange.com/questions/361/when-is-a-model-underfitted).
The Overfitting problems happens when the model fits the data 
tightly whereas Underfitting happens when we don't use enough data while
coming up with a machine learning model.

Cross-validation is a method of splitting all of your data into two
parts: training and validation. The training data is used to build the
machine learning model, whereas the validation data is used to validate
that the model is doing what is expected. Scikit-learn provides helper
methods for [cross
validation](http://scikit-learn.org/stable/modules/cross_validation.html).

Precision and Recall
====================

[Precision and
Recall](http://scikit-learn.org/stable/auto_examples/plot_precision_recall.html)
are good metrics for monitoring how effective the machine learning
implementation is. Precision is the total percentage of true positives
in our training data. Recall is the ratio of true positives to true
positive plus false negatives.
