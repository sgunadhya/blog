+++
author = "Sushant Srivastava"
date = "2017-08-20T02:50:27+05:30"
description = "Android Libraries Du Jour"
draft = false
keywords = ["android", "libraries"]
tags = ["android", "libraries"]
title = "Android Libraries Du Jour"
topics = ["Android Libraries"]
type = "post"
+++

I returned to Android Development after a hiatus of three years and it did not come
as a surprise to me that the lay of the land has changed significantly. Over the past
few days I have been trying to wrap my head around the new ecosystem by lurking
in the subreddits, slack channels and by general good old-fashioned googling. Here's
a run down of the five essential libraries or patterns that are in vogue.

Dagger 2
---------

[Dagger 2](https://google.github.io/dagger/) is a library for Dependency Injection. The concept of Dependency Injection
took Java Enterprise world by storm in the last decade. It is the Star Wars of the Java
Concepts in that it spawned many merchs, sequels, I mean libraries, consultancies.
Essentially, you have a library which provides Dependencies to the objects of your
application. [Spring Framework](https://spring.io/) and [Guice](https://github.com/google/guice/wiki/Motivation) have been the pioneers. Dagger is the new entrant
and the USP is that it provides compile time guarantees that the dependencies are met.
I remember using Spring Framework, wiring my dependencies only to find out the web server
throw up a giant stack trace about a teeny-tiny dependency not wired. So, Dagger (it's an
Object Grapher, more specifically a Directed Acyclic Graph-er, or Dagger, gettit?) is
a welcome entrant.

Using Dependency Injection has its advantages in that it makes for a testable code base.
and the Architecture is decoupled. Having said that, I found that the learning curve was
a bit steep.

Note: Dagger 1 or Dagger was developed by Square. Dagger 2 is a fork by Google and is
actively maintained by folks at Google.

RxJava
------

[RxJava](https://github.com/ReactiveX/RxJava) has taken the Java World by storm. Rx and its reactive extensions enable
Functional Reactive Programming in the language of your choice. RxJava has received
a lot of love from the Java community. Android is the natural place for implementing
FRP. Many libraries use RxJava as well. [Retrofit](http://square.github.io/retrofit/), the sweetest library to call REST APIs,
uses RxJava in the backend. [Retrolambda](https://github.com/orfjackal/retrolambda) is a great companion library because it helps in writing lambda expressions in the subscribe and observe apis resulting in succinct
and fluent code.

Butterknife
-----------
[Butterknife](http://jakewharton.github.io/butterknife/) uses dependency injection to inject widgets into your code so that your View
code is not littered with *findViewByIds*. Doesn't sound much but I have grown to love
this library so much so that the first refactor that I do on an old source code is using Butterknife
to inject the views. It is one of those libraries that you thought you didn't need it until you used and now cannot let go. It is the fidget-spinner of Android Libraries.


Glide
-----
[Glide](https://github.com/bumptech/glide) is an Android Library for loading images. It does what it says on the tin,
only better than the alternatives like Picasso.

MVP
----
MVP stands for Model View Presenter Pattern. It is a pattern that most developers
are gravitating towards now a days. As your Android Application grows adopting
this pattern will help in structuring the application this way. The pattern takes
a leaf from the MVC pattern and recommends separating the view layer from the
model layer. In the beginning I thought this was a bit much and takes a lot of
work but persevering helped because many developers are using this pattern to  structure their apps.

Other sources for learning are downloading Google Android Architecture sample apps. You can also look
at the trending repositores in Gitub for Java, a majority of them currently are Android Libraries or sample applications because, let's face it, Android is where it's at.
