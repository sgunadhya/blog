+++
author = "Sushant Srivastava"
date = "2017-08-28T02:50:27+05:30"
description = "Initialize Libraries in an Android Dagger App"
draft = false
keywords = ["android", "libraries"]
tags = ["android", "libraries"]
title = "Initialize Libraries in an Android Dagger App"
topics = ["Android Libraries"]
type = "post"
+++

Many libraries like *Admob* on Android require a one-time initialization snippet
code to be run. Now, the initialization code is a one-time run, and does not return
any object. This is not a factory method. A convenient place that I found happened
to be inside the *applicationInjector* method in the class which extends *DaggerApplication*.

As an example, here I initialize Admob inside the *applicationInjector* like so:

```Java
@Override
protected AndroidInjector<? extends DaggerApplication> applicationInjector() {
    AppComponent appComponent = DaggerAppComponent.builder().application(this).build();
    appComponent.inject(this);
    MobileAds.initialize(this, "ca-app-pub-3940256099942544~3347511713");
    return appComponent;
}
```

Perhaps you can extract a private method to initialize library code like so:

```Java
@Override
protected AndroidInjector<? extends DaggerApplication> applicationInjector() {
    AppComponent appComponent = DaggerAppComponent.builder().application(this).build();
    appComponent.inject(this);
    initializeLibraries();
    return appComponent;
}

private void initializeLibraries() {
    MobileAds.initialize(this, "ca-app-pub-3940256099942544~3347511713");
}
```

and you can conveniently place the initialize snippets inside the *initializeLibraries*
method. Now, there might be a better place to place these snippets, maybe inside
a lifecycle method, but this seems to work.
