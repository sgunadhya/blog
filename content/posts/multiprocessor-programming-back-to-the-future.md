
+++
author = "Sushant Srivastava"
date = "2021-07-30T02:50:27+05:30"
description = "Multiprocessor Programming - Back to the Future"
draft = false
keywords = ["java", "multithreading", "tla+"]
tags = ["java", "multithreading", "tla+"]
title = "Multiprocessor Programming - Back to the Future"
topics = ["Java", "tla+"]
type = "post"
+++

## Why Go Back to the Drawing Board

Writing correct programs is hard; writing correct concurrent programs is harder. Multi-threading throws beginning Java Programmer off, and I’d argue some seasoned programmers as well. Many senior Java programmers do not understand the concept well. This is because the concepts are not applied in a day job. Suppose you’re not working in a Java shop like Investment banks that use multi-threading concepts. In that case, you’re not likely to come across the concepts in a regular run-of-the-mill Spring CRUD web application. Abstraction has its own disadvantages. Many beginner Java books bring home the idea that multi-threaded programming is complicated. When I ran through the books, I would skip the sections because let’s face it - beginners have a lot of ground to cover in Java. They do not want to be bogged down by the hard stuff. Multi-threaded programming has always been a high-churn-topic in Java World. Java had OS-like primitives like `synchronized`, `wait`, `notify` for multi-threaded programming. Java 5 introduced the `java.util.concurrent` package in the Java world, which made reasoning about the primitives easier. People who were well-versed with Java 4 constructs continued writing the code using the 1.4 primitives for a long time even when Java 5 primitives were available. 

But the world has changed, and the constructs are now _sine qua non_ of everyday programs. We see different programming models for concurrent programming by the day, like the Actor model, Software Transactional memory, etc. Java’s concurrency primitives are growing as well. You will need a firm grounding in multiprocessor programming for understanding what is happening in the landscape. A senior programmer is “expected” to know the underpinnings of each model and understand what problems they solve. I found that a thorough grounding in the basics of multiprocessor programming sets you up for success in understanding the pros and cons of new paradigms. When everyone is after the latest and greatest, it is meditative to slow down. Also, multiprocessor programming is closely related to distributed systems theory. 

## A Book and a Proof Checker 

I decided to go back to the drawing board. I did not want a text in dry academic style. I wanted something which is grounded in practice, and at the same time did not cut corners on the basics. I chose to give (The Art of Multiprocessor Programming [Herlihy, Shavit, Luchangco, & Spear, 2020](#org932fdaa))
 a shot. I skimmed through the book once a few years ago. I chose the book because it has useful examples in Java and the theory is not hand-wavy.

I quickly realized that while the book has great explanations and code samples, it is somewhat labor-intensive to reason about the algorithms. For example, I understand that the book uses linear history without any cycles to prove correctness of mutual exlusion algorithms. The state space of runtime of these algorithms are huge, and you can arrive at the state using book's examples, I felt that there should be an automated way of arriving at a state that proves or disproves the correctness of the algorithms. In software engineering, we are used to writing unit tests for checking correctness of the code. I was looking for a similar automated tool for executing the specification and generating a counter-example.

I had read about TLA+ before, that it had been successfully used to find bugs in a [complex concurrent program](https://awsmaniac.com/how-formal-methods-helped-aws-to-design-amazing-services/). I thought this was an opportune moment to give TLA+ a shot. My idea was that I could specify the algorithm in TLA+ and play around with the state space that it generates. The exploratory nature of learning piqued my interest. I normally use VSCode for coding, and sure enough I found a [plugin that supports TLA+ development](https://marketplace.visualstudio.com/items?itemName=alygin.vscode-tlaplus).

I started out by translating one of the first algorithms in the book to PlusCal. PlusCal is the language in which you code specification in TLA+.
The tool translates  PlusCal into another specification. The `tlc` tool checks the specification for any deadlock or errors in algorithms.
In theory, it should work well, but I hit a wall early on. Translating the code/pseudo-code from the book into PlusCal took a bit of time.
For example, here is the code for the `lock-one` algorithm from the book


```java
    class Lockone implements Lock {
        private boolean[] flag = new boolean[2];
        public void lock() {
            int i = ThreadID.get(); int j = 1 - i;
            flag[i] = true;
            while (flag[j]) {}
        }
        public void unlock() {
            int i = ThreadID.get();
            flag[i] = false;
        }
    }

```

To translate the code in PlusCal, I tried looking at the implementation on web. I did not find any snippet of code that implements the algorithm. Instead, I borrowed a snippet from the implementation of Peterson Algorithm, and worked backwards from there to arrive at the following code:

```ruby
(* --algorithm lockone
    variables flag = [i \in {0, 1} |-> FALSE];
    fair process proc \in {0,1}
    begin
        a1: while(TRUE) do
            skip;
        a2: flag[self] := TRUE;
        a3: await (flag[1-self] =  FALSE);
            cs: skip;
        a4: flag[self] := FALSE;

        end while
            end process
    end algorithm; *)
```

The pattern here is that first we have the lock implementation, followed by a critical section step - labeled here with `cs`, and then the code for the unlock section.

```ruby
(* --algorithm mutex-generic-two-processor
    variables flag = [i \in {0, 1} |-> FALSE];
    fair process proc \in {0,1}
    begin
        a1: while(TRUE) do
            skip;
        // lock code
            cs: skip;
       // Unlock code

        end while
    end process
    end algorithm; *)
```

Then I run the tool in VSCode to transpile the Pluscal code in TLA+ specification. After successful transpilation, I run the `tlc` tool from VSCode to run the checker. Sure enough, it found a deadlock with the trace.

{{< figure src="/images/tladeadlock.png" class="mid">}}

Overall, I am happy with the approach, and I feel that it is a good starting point. As I go through the book, I wil try to encode the code in PlusCal and run the checker. Like Unit test driven development, the workflow has a red-fail-code-green-check feel to it. 


## Bibliography {#bibliography}

<a id="org932fdaa"></a>Herlihy, M., Shavit, N., Luchangco, V., & Spear, M. (2020). _The art of multiprocessor programming_. Newnes.

