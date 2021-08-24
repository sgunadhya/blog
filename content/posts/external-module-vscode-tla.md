+++
title = "How to Add a New Module Dependency in VSCode TLA?"
author = ["Sushant Srivastava"]
date = 2021-08-24
tags = ["tla+", "vscode"]
categories = ["vscode", "tla+"]
draft = false
+++

TLA+ has community modules that user modules can extend from. The Github repository [tlaplus/CommunityModules](https://github.com/tlaplus/CommunityModules) houses these community modules. The community modules are packaged as a jar file. If you are using TLA Toolbox, then you can add the jar file in the classpath and use the community module in your TLA modules. The _README_ files includes a link to a video that shows how you can include the module in your code.

If you are using VScode and its excellent [TLA+ Plugin](https://marketplace.visualstudio.com/items?itemName=alygin.vscode-tlaplus), then how do you include the jar file in your classpath?

It turns out that the plugin allows you to include custom jar files having external modules in your classpath. From the [documentation](https://github.com/alygin/vscode-tlaplus/wiki/Java-Options#adding-dependencies):

> If you provide a `-cp` or `-classpath` option that doesn't explicitly contain a path to the tal2tools.jar library, the exstension will add the default class path to the end of the option value.

{{< figure src="/ox-hugo/communityModules.png" >}}
