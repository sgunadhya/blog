+++
author = "Sushant Srivastava"
date = "2022-02-02"
description = ".NET and Java - Two Households Alike In Dignity"
draft = false
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
the MONO Runtime. .NET is also getting much love from open source developers. The platform has gone from being the *bete noire* for
the open source cabal to being the *pupillam oculorum* (that's apple of the eyes) of the open source ecosystem.

## Everything Is Awesome Now (For the Most Part)

While I feel that the cross platform .NET ecosystem in on-par with such disruptive innovations like the sliced-bread, I wanted to sum up the key points under three headers - Documentaion, CLI (Command-line interface - the `dotnet` command), and C#.

### Documentation

.NET documentation is one of the best documentation for any platform right now. Need a tutorial-like quick-start guide for getting 
up and running with web api? There is a [documentation for that](https://docs.microsoft.com/en-us/aspnet/core/getting-started/?view=aspnetcore-6.0&tabs=macos). Need to grok the C# language in depth? There are [docs for that](https://docs.microsoft.com/en-us/dotnet/csharp/). The docs are self-contained reference books and tutorials.

The documentation is very state-of-the-art. You can find documentation for common architectural patterns like CQRS, DDD. The [cloud architecture documentation](https://docs.microsoft.com/en-us/azure/architecture/patterns/) for Azure is a must-read even if you're not planning to use Azure for your services. The patterns are robust
and general - they can be carried over to any cloud platform.

### CLI

I consider the `dotnet` command to be the crown-jewel of the .NET ecosystem. You can create projects, update dependencies, run
tests, build the project, create a new template, install additional tooling using the same command (of course different subcommands).
For example, you can create a solution that has a console application, a grpc service, a web-api project using ASP.NET without
launching your graphical IDE. I recall that Rails was one of the first projects since I started working that provided scaffolding 
using the cli-subcommands, and developers quickly warmed up to the idea. The convenience cannot be overstated. The scaffolds are not 
limited to projects, you can for example create a scaffold for `gitignore` that you can use across different projects.

You can also install third-party tooling using the `dotnet` command. For example, you can install a third party tool which analyses your 
projects for vulnerabilities, and then run it on your repo using the tool command. Needless to say that this has spanned an ecosystem of templates
and scaffolds, a lot of them are housed in [nuget.org](https://www.nuget.org/).

### C#

C# is a pleasant language to use.
I knew for a long time that C# is at the forefront of including advanced constructs like lambda, async-await.
Using them in projects is pleasant, so much so that I wonder why Java does not have these convinient features.

## Warts and All

It is not all hunky-dory in the dotnet world. Take for example the state of desktop development.
WPF is the de facto framework for writing Desktop apps, or it was until recently. The desktop
development paradigm has been in a state of churn. I read conflicting messaging about which framework to use
for a new desktop project. The recommendations ranged from UWP to WinUI3. UWP is heading towards deprecation, and
WinUI3 is still in preview as of now.
Another case in point - I ran into many issues when trying to run a console app. Granted I was using an M1 mac, and the beta release - so that was a double whammy. Here are the steps I followed:

1. Installed .NET 6 on M1 Mac
2. Ran into an error - ASP.NET library was not found
3. Edited the file location `/etc/dotnet/install_location` to specify the location.
4. `dotnet --roll-forward Major bin/Debug/netcoreapp3.1/newconsoleapp.dll` `--roll-forward Major` was recommended here: {{< icon "github" >}}[Running a .NET 5 project on macOS M1 with .NET 6 leads to confusing error message](https://github.com/dotnet/runtime/issues/59168>)

With time I foresee that the issues will be ironed out. For example, when I ran into the issue the issue was still open, but the developers quickly brought it to closure.

I see the question pops up on Hacker News asking people what would they choose as their modern development stack.
My answer to that question is unequivocal - .NET.
