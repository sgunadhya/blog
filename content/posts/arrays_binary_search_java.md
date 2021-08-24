+++
author = "Sushant Srivastava"
date = "2021-03-28"
description = "upper_bound and lower_bound in Java Standard Library"
draft = false
keywords = ["java", "algorithms"]
tags = ["java", "algorithms"]
title = "upper_bound and lower_bound in Java Standard Library"
topics = ["java", "algorithms"]
type = "post"

+++

Sometimes, there are simple things that fly under your radar. 

C++ has `upper_bound` and `lower_bound` that return the elements that are bounds for a given element in a sorted array or collection.
Python has a similar `bisect` module that has functions `bisect_left` and `bisect_right`.

I did not find similar functions in Java Standard Library. I would resort to following the binary search again over the collection or array to find the bounds. I discovered that the `binarySearch` methods from `java.util.Collections` and `java.util.Arrays` return the index of element if the element was found
in the collection/array or a negative number indicating the *insertion point* of the element.

The *insertion point* is the clue here. From the Java docs, here is the description of the return value from `binarySearch`:

> index of the search key, if it is contained in the array; otherwise, (-(insertion point) - 1). The insertion point is defined as the point at which the key would be inserted into the array: the index of the first element greater than the key, or a.length if all elements in the array are less than the specified key. 

Also notice here that `(-(insertion point) - 1)` is actually the two's complement of *insertion point*. Applying tilde operator `~` to an integer gives us its 2s complement.


```java
 int upperBound;
 int lowerBound;
 int index = Collections.binarySearch(sortedList);
 if(index < 0) {
	 index = ~index; //Get the insertion point using 2's complement.
 }
 if(index < sortedList.size()) {
	 upperBound = sortedList.get(index);
	 lowerBound = sortedList.get(index - 1);
 }

```