+++
author = "Sushant Srivastava"
date = "2016-06-29T16:34:45+05:30"
description = "Where are the include and link directories for packages installed through Homebrew"
draft = false
keywords = ["cmake", "homebrew"]
tags = ["TIL", "build"]
title = "Where are the include and link directories for packages installed through Homebrew"
topics = ["homebrew", "cmake"]
type = "post"

+++

I was trying to build a project which had dependencies of [`gflags`](https://github.com/gflags/gflags) and [`glog`](https://github.com/google/glog) and used [`cmake`](https://cmake.org/) as the build tool.

I was using [Homebrew](http://brew.sh/) on MacOSX, so I went ahead and installed the dependencies like so:

<pre class="prettyprint">
brew install glog
brew install gflag
</pre>

Now, I wanted to add include path and link path for these libs in the project.
My first shot was to add a `CXXFLAGS` variable and expected that `cmake` would pick it up.

<pre class="prettyprint">
export CXXFLAGS="-I/usr/local/Cellar/glog/0.3.4/include -I/usr/local/Cellar/gflags/2.1.2/include/"

</pre>

`cmake` did not pick up this because it never used CFLAGS or CXXFLAGS.

Next, I added the dependency manually in the `CMakeLists.txt` file using the `include_directories` and `link_directories` like so:


<pre class="prettyprint">
include_directories(/usr/local/Cellar/glog/0.3.4/include)
include_directories(/usr/local/Cellar/gflags/2.1.2/include)
link_directories(/usr/local/Cellar/glog/0.3.4/lib)
link_directories(/usr/local/Cellar/gflags/2.1.2/lib)
</pre>

This approach was not scalable. I searched for a bit and found an acceptable solution. I added `/usr/local/include` and `/usr/local/lib`
in the include and the link path respectively.

<pre class="prettyprint">
include_directories(/usr/local/include)
link_directories(/usr/local/lib)
</pre>
This works! I am of the opinion that we can do better, but as of now I am okay with this.
