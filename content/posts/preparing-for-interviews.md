+++
author = "Sushant Srivastava"
date = "2021-04-20"
description = "Preparing for Technical Interviews: A retrospective"
draft = false
keywords = ["java", "algorithms", "interviews"]
tags = ["java", "algorithms", "interviews"]
title = "Preparing for Technical Interviews: A retrospective"
topics = ["java", "algorithms","interviews"]
type = "post"

+++

I dread Programming Interviews.

I have been programming for a while now (over a decade), but attending a programming interview is still a humbling experience for me.
You get rusty, and the inertia to start the preparation all over is too daunting. Treating the preparation as an opportunity for self-development regardless of outcome is something that gets me started. If you are embarking on your preparation for interviews, then I hope you find these pointers helpful.


### Mental Models {#mental-models}

Alan Kay in one of his [presentations](https://www.youtube.com/watch?v=p2LZLYcu%5FJY) brings home this notion of "Doing with Images Make Symbols". The phrase summarizes our learning progression. The progression starts from specific to generic to more abstract. For example, a child learns by doing, then imagines the act of doing with images, and then makes symbols denoting the act of doing something. CS reverses the entire progression. In CS, they introduce us to the symbols before the images, and images before doing. Some of the best programmers I met could visualize the algorithms and their code, and they could reason about the code with this mental model.


Visualizing arrays as sequential cells is commonplace. You can do one better by identifying patterns of code with animations. For example, sliding window visualization as an animation running over sequential cells reinforces recall, and also helps in "explain ability". You can dial it up to eleven by labelling the visual with variables and what they denote for example the pointers. Visualizing linear and non-linear data structures becomes second-nature the more you practice and mindfully cultivating this will speed up the learning.


### Spaced Repetition {#spaced-repetition}

In an interview situation, you will need to remember many facts. Competitive programming and programming for interviews need you to remember many patterns and techniques. It is another of those situations where preparation for interviews is far-removed from the real-world situations. In real-world situations, you have access to Stackoverflow, search engines, IDE-support, etc. Some interviews require you to code syntactically correct code in the first pass. For someone who is used to writing code in real-world with ample support from IDE, and search engines, it takes practice and perseverance to write code in a plain-text editor. It takes some time before writing syntactically correct code becomes muscle memory.


You will still need to remember algorithms and patterns. Many people have had successes using Spaced Repetition to recall information. Spaced Repetition is a recall of information that you had studied for at regular intervals so that it is always, so to speak, hydrated. A popular mechanism is to use Flashcards. Software like Anki makes it easy for you to organize decks and cards. The algorithm schedules your study.


People on the Internet share their flashcards for studying CS and Algorithms. I find it suboptimal. Making Flashcards for recall is a personal experience. If you are embarking on studying for interviews using Flashcards, then you're better off making them on your own. You can make flashcards for remembering snippets of code, or identifying algorithms given a situation.


### Organising using Test classes {#organising-using-test-classes}

Over learning to code, you will definitely write a good amount of code. Commit them in a repository for posterity and revisit them. Another good idea is to use a testing framework for writing the test cases.


A common pattern that I have seen people use when writing the code for preparation is to have a class with a `public static void main` method to test the code. I am taking Java as an example here. While there is nothing inherently wrong in the pattern, I feel that organising code using a Test framework like Junit is better. Testing is just as important as writing the code. Develop the habit of writing test code after writing the method signature. The test methods are named-testing units you can use to automate different boundary conditions. You can also organize the test classes by paradigms like "Divide and Conquer", "Dynamic Programming" using [Test suites](https://junit.org/junit4/javadoc/latest/org/junit/runners/Suite.html). Also, you are using good engineering practices in learning.

```java
import org.junit.runner.RunWith;		
import org.junit.runners.Suite;		

@RunWith(DynamicProgrammingSuite.class)				
@Suite.SuiteClasses({				
  KnapsackTest.class,
  EditDistanceTest.class,
  ... 			
})		

public class Test {				
			...
}
```


### Zen Mind, Beginner's Mind {#zen-mind-beginner-s-mind}

Last but not the least, attending interviews is a humbling experience after you have been coding for a while. Think of it as an opportunity to refactor your understanding of code and related subjects. Another trick that helps is thinking of the interviews as another opportunity to meet people and understand their contexts, constraints, and preferences.


Last, here are two books that might help you get started on the journey:


-   [Elements of Programming Interviews in Python: The Insider's Guide](https://www.amazon.in/Elements-Programming-Interviews-Python-Insiders-ebook/dp/B092SX1SSJ) lists programming interview questions grouped by Data Structures and Techniques like Greedy Programming.
-   [Cracking the Coding Interview](https://www.amazon.in/Cracking-the-Coding-Interview/dp/0984782869) is a widely read and respected book. The book gives a great rundown of what it entails to prepare for interviews in the big companies.
