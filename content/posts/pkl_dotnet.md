+++
author = "Sushant Srivastava"
date = "2024-05-11"
description = ".NET and Pkl - Be Able for Thine Enemy" 
draft = false
keywords = ["pkl", "dotnet", "configuration"]
tags = ["configuration", "dotnet"]
title = ".NET and Pkl - Be Able for Thine Enemy" 
topics = ["configuration", "dotnet"]
type = "post"
+++

[Pkl](https://pkl-lang.org/index.html "Pkl Configuration language") is a language from Apple for configuration management that advetises itself to be programmable, scalable, and safe. It can generate any static configuration format like `json`, `yaml`, or `properties` files. The configuration can adhere to a user-defined schema, so you can catch errors before deployment - this was the selling point for me because I have been burnt by misconfiguration in the past.

I have mostly been programming in dotnet these days. The most common format for managing configuration in dotnet application is `json` with `appsettings.json`, `appsettings.Development.json` etc. 
Would it be possible to use `pkl` for managing configuration in dotnet apps? The most obvious benefit would definitely be catching errors before any deployment.

Turns out, Apple does not officially support C# for Pkl. There is out-of-the-box support for Java, Kotlin, Swift, and Golang. I looked around and found a community-supported [package](https://github.com/Rafaeruo/pkl-csharp "pkl-csharp")

To add support for Pkl in your dotnet project, you'd need to add a reference to the NuGet Package `PklCsharp`

```bash
dotnet add package PklCsharp

```

If you're using dotnet hosting extensions, then you'd also need to add a reference to the `PklCSharp.Microsoft.Extensions.Configuration`.

```bash
dotnet add PklCSharp.Microsoft.Extensions.Configuration
```

In your program setup, add a reference to the `pkl` configuration files like so:

```c#
builder.Configuration.AddPklModule(ModuleSource.FileSource(<Path to pkl file>));
```

and that's it. You can now write the configuration using Pkl files. You can also set custom schema for your configuration, and then you can catch configuration errors during startup!
