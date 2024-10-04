---
title: "Swift Command Line Application - Joy's Soul Lies In the Doing"
date: 2024-10-04T16:43:56+05:30
draft: false
description: "Finally getting it right - a template for creating command line Swift Applications"
keywords: ["swift", "beginner"]
tags: ["swift", "beginner"]
topics: ["swift", "beginner"]
---
{{< figure src="/images/DSC00090.webp" >}}

I am getting deeper into Swift the programming language. I am not into iOS or Apple Development Ecosystem.
I am super intrigued about Swift's Server Side Support. I am beginning to feel that Swift is a well-rounded 
language for backend development.

So, I bit the bullet, and started exploring how Swift applications are structured beginning with command line
applications. While Swift's website has a great [starter template](https://www.swift.org/getting-started/cli-swiftpm/) for starting out with a command line application, I felt it lacked facets that I lean towards when starting out. 

I am not a huge fan of the starter template's structure. It assumes that you will be writing your code in one module. I usually structure 
the command line applications like so:
- *Main Module* The Entry-point module. This module contains the Tool-like aspect of the program, like gather user input, configuration etc.
- *Core Module* This module is responsible of housing the core api of the applications, and last but not the least -
- *Tests* I usually write tests for the code module.

Let's begin with  the starter template and modify it the way I like to structure the code. We will create a `SampleTool` application.
`SampleTool` is the entry point module, `SampleCore` is going to be the API Core, and `SampleCoreTests` is for testing the `SampleCore` module.

We begin by generating the code using Swift Package Manager:

```bash
mkdir SampleTool
cd SampleTool
swift package init --name SampleTool --type executable
Creating executable package: SampleTool
Creating Package.swift
Creating .gitignore
Creating Sources/
Creating Sources/main.swift
```
This will generate the following structure:
```bash
├── Package.swift
└── Sources
    └── main.swift

2 directories, 2 files
```
The `Package.swift` file contains the following text:
```Swift
import PackageDescription

let package = Package(
    name: "SampleTool",
    targets: [
        .executableTarget(
            name: "SampleTool"),
    ]
)
```
While this works, I noticed the `swift` command line options also supports adding a `tool` type package. The `tool` package type includes the 
`ArgumentParser` dependency, an important support package that makes it easier to add support for options and flags.

```bash
swift package init --name SampleTool --type tool
Creating tool package: SampleTool
Creating Package.swift
Creating .gitignore
Creating Sources/
Creating Sources/SampleTool.swift
```

If we look at the contents of `Package.swift` now, it will include `ArgumentParser` dependency.

```Swift
import PackageDescription

let package = Package(
    name: "SampleTool",
    dependencies: [
        .package(
          url: "https://github.com/apple/swift-argument-parser.git", 
          from: "1.2.0"),
    ],
    targets: [
        .executableTarget(
            name: "SampleTool",
            dependencies: [
                .product(name: "ArgumentParser", 
                 package: "swift-argument-parser"),
            ]
        ),
    ]
)
```
Now, lets add a target for our `SampleCore` module, this module will house the core api.

```bash
swift package add-target SampleCore --type library
swift package add-target-dependency SampleCore SampleTool
```
If we look at the structure of our project it looks like so:

```bash
.
├── Package.swift
└── Sources
    ├── SampleCore
    │   └── SampleCore.swift
    └── SampleTool.swift

3 directories, 3 files
```
And, our `Package.swift` looks like this:
```Swift
import PackageDescription

let package = Package(
    name: "SampleTool",
    dependencies: [
        .package(url: "https://github.com/apple/swift-argument-parser.git", from: "1.2.0"),
    ],
    targets: [
        .executableTarget(
            name: "SampleTool",
            dependencies: [
                .product(name: "ArgumentParser", package: "swift-argument-parser"),
                .target(name: "SampleCore"),
            ]
        ),
        .target(name: "SampleCore"),
    ]
)
```
Lastly, lets add the test target:

```bash
swift package add-target SampleCoreTests --type test
swift package add-target-dependency SampleCore SampleCoreTests
```
With these changes, our `Package.swift` looks like this:

```Swift
import PackageDescription

let package = Package(
    name: "SampleTool",
    dependencies: [
        .package(url: "https://github.com/apple/swift-argument-parser.git", from: "1.2.0"),
    ],
    targets: [
        .executableTarget(
            name: "SampleTool",
            dependencies: [
                .product(name: "ArgumentParser", package: "swift-argument-parser"),
                .target(name: "SampleCore"),
            ]
        ),
        .target(name: "SampleCore"),
        .testTarget(name: "SampleCoreTests",dependencies: [
    .target(name: "SampleCore"),]),
    ]
)
```

When I run the `build` command, I get this error:

```bash
error: 'sampletool': Source files for target SampleTool should be located under 'Sources/SampleTool', 
or a custom sources path can be set with the 'path' property in Package.swift
```
We get this error message because `SampleTool.swift` should be in its own module directory.
So we move the file to its own directory, and finally our structure looks like this:

```bash
.
├── Package.resolved
├── Package.swift
├── Sources
│   ├── SampleCore
│   │   └── SampleCore.swift
│   └── SampleTool
│       └── SampleTool.swift
└── Tests
    └── SampleCoreTests
        └── SampleCoreTests.swift

6 directories, 5 files
```
And, that's it! Now, that I have setup the project the way I like, I can start developing.

Swift Package Manager is a wonderful tool that takes a getting used to. If you are like me, you
might get confused between `module`, `target`, and `product`, here's its [proposal](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0146-package-manager-product-definitions.md)






















