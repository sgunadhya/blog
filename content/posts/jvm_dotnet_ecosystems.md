+++
author = "Sushant Srivastava"
date = "2022-01-28"
description = ".NET and Java - Two Households Alike In Dignity"
draft = true
keywords = ["java", "dotnet"]
tags = ["java", "dotnet"]
title = ".NET and Java - Two Households Alike In Dignity"
topics = ["java", "dotnet"]
type = "post"

+++
{{< figure src="/images/HouseholdsAlikeInDignity.jpg" >}}

{{< lead >}}
In which I extol the virtues of the .NET Ecosystem
{{< /lead >}}
I have been developing in Java for a long time. I have also worked on Python and Ruby, but for
the most part I have worked in Java. Lately, I had work come in my way
that requires knowing .NET and related tools. I am comfortable in the JVM space. I embarked on my 
.NET learning journey with much trepidiation. I was entering *terra incognita*. What came as a surprise, is
that the .NET ecosystem now is more open than before. For example, you can now .NET applications on Linux - without using 
the MONO Runtime. .NET is also getting much love from open source developers. The platform has went from being the *bete noire* for 
the open source cabal to being the *pupillam oculorum* (that's apple of the eyes) of the open source ecosystem.


## Everything Is Awesome (For the Most Part)
Dotnet has caught up.

- Ecosystem
  - CQRS DDD implemented and suggested straight from the source
- Documentation
  - MSDN had its deterrents
  - The overhauled documentation is awesome!
- Patterns
- CLI
  - crown-jewel of the dotnet ecosystem
    - like maven or gradle, but better
  - templates
- C# is a pleasant version of Java




## Warts and All
It is not all hunky-dory in the dotnet world. Take for example the state of desktop development.
WPF is the de facto framework for writing Desktop apps, or it was until recently. The desktop
development paradigm has been in a state of churn. I read conflicting messaging about which framework to use
for a new desktop project. The recommendations ranged from UWP to WinUI3. UWP is heading towards deprecation, and
WinUI3 is still in preview as of now.
Another case in point

1. Installed .NET 6 on M1 Mac
2. ASP.NET library was not found
3. edited the file location `/etc/dotnet/install_location`
4. `dotnet --roll-forward Major bin/Debug/netcoreapp3.1/newconsoleapp.dll` `--roll-forward Major` was recommended here: {{< icon "github" >}}[Running a .NET 5 project on macOS M1 with .NET 6 leads to confusing error message](https://github.com/dotnet/runtime/issues/59168>)

I see the question pops up on Hacker News asking people what would they choose as their modern development stack.
My answer to that question is unequivocal - .NET.  