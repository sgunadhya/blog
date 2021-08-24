+++
title = "Where is the Specification File in TLA+ VSCode Plugin?"
description = "Where is the Specification file in TLA+ VSCode Plugin?"
date = "2021-08-22"
author = ["Sushant Srivastava"]
draft = false
keywords = ["tla+", "algorithms"]
tags = ["tla+", "algorithms"]
topics = ["tla+", "algorithms"]
type = "post"
+++

I am using the excellent Visual Studio code plugin, [TLA+](https://marketplace.visualstudio.com/items?itemName=alygin.vscode-tlaplus), for writing TLA+ code, and running the code. The plugin makes it easy to write PlusCal code by providing syntax-highlighting, and syntax checking. The plugin can run the specification through the `tlc` checker, and report errors or success. The plugin makes it easy for people familiar with VS Code to write the specification and run them in an authoring mode that is familiar to them. My workflow is - write the PlusCal code, parse the code using "TLA+: Parse Module" editor command, and then run the "TLA+: Check model with TLC" editor commands from the plugin.

There are however some caveats. When you start your "Parse Module" editor command, the plugin notifies that that a `cfg` file should be present for running the checker. This is something to be mindful of when running the checker. Also, when you run the checker with the default configuration file, then it reports another error: "The specification file cannot specify both INIT/NEXT and SPECIFICATION fields". I delete the "INIT" and "NEXT" declarations from the file, and re-run the checker.

For example, here is the module for the famous **readers-writers** problem from the book (Practical TLA+ [Wayne, 2018](#org2abc65f)) book. The module declares a constant `MaxQueueSize`.

```ruby
---- MODULE test ----
EXTENDS TLC, Integers, Sequences
CONSTANTS MaxQueueSize
(*--algorithm message_queue
variable queue = <<>>;
define
  BoundedQueue == Len(queue) <= MaxQueueSize
end define;
process writer = "writer"
begin Write:
  while TRUE do
    queue := Append(queue, "msg");
    await Len(queue) <= MaxQueueSize;
  end while;
end process;
process reader = "reader"
variables current_message = "none";
begin Read:
  while TRUE do
    await queue /= <<>>;
    current_message := Head(queue);
    queue := Tail(queue);
  end while;
end process;
end algorithm;*)
====

```

If I attempt to parse the module using the "Parse Module" editor command, I get the notification : "Model file test.cfg does not exist. Cannot check the model."

{{< figure src="/images/spec-file.png" title=" file test.cfg does not exist." >}}

After, I click on the "Create model file" button, the editor generates a .cfg file with the following contents:



```ruby
SPECIFICATION Spec
\* Uncomment the previous line and provide the specification name if it's declared
\* in the specification file. Comment INIT / NEXT parameters if you use SPECIFICATION.

CONSTANTS
    greeting = "Hello"

INIT Init
NEXT Next

\* PROPERTY
\* Uncomment the previous line and add property names

\* INVARIANT
\* Uncomment the previous line and add invariant names

```

When I run the checker with this configuration file, I am greeted with another error: "The configuration file cannot specify both INIT/NEXT and SPECIFICATION fields". 

{{< figure src="/images/cannot-specify.png" title="Cannot specify INIT/NEXT and SPECIFICATION." >}}

When I empty the contents of the file, I get another error : "The constant parameter MaxQueueSize is not assigned a value by the configuration file.". Notice that the `tla` file declared a constant which should be initialized in the configuration file.
I could get the checker running with this version of the configuration file:

```ruby
SPECIFICATION Spec

CONSTANTS
    MaxQueueSize = 2

```

So what is the configuration file? When we run the checker through the plugin, it invokes the following command:

```bash
java -cp tla2tools.jar -XX:+UseParallelGC tlc2.TLC test.tla -tool -modelcheck -coverage 1 -config test.cfg
```

The configuration file is the input to the `-c` option in the command. The configuration file tells TLC the names of the specification and of the properties to be checked. The configuration file must specify values for all the constant parameters of the specification. We can also specify any invariants that the tool should check in the specification file. For example, in the specification listed above, there is an invariant `BoundedQueue`. We can ask `tlc` to check for the invariant by specifying it in the file like so:

```ruby
SPECIFICATION Spec

CONSTANTS
    MaxQueueSize = 2

INVARIANT BoundedQueue

```




## Reading {#bibliography}

<a id="org2abc65f"></a>Wayne, H. (2018). _Practical TLA+_. <https://doi.org/10.1007/978-1-4842-3829-5>
