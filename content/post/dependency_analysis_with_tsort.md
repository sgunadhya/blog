+++
author = "Sushant Srivastava"
date = "2016-10-25T22:17:42-04:00"
description = "Using tsort in your build pipeline for managing dependencies"
draft = false
keywords = ["til", "build"]
tags = ["til", "build"]
title = "Using tsort in your build workflow"
topics = ["build"]
type = "post"

+++

I use [maven](https://maven.apache.org/) for building Java projects. We have several project modules which are built independently. The projects are dependent on one another. We don't push the newer artifacts to a common maven repository, so the developers have to pull the latest changes from the source code repository, install it on the local maven repository, and use the dependencies. It so happens that sometimes we end up in a dependency hell where we spend several minutes resolving the correct dependency order.

I wrote a small shell script which uses [`tsort`](https://en.wikipedia.org/wiki/Tsort) to automatically generate a topological sort of all the projects which we can then use to systematically build our projects.

Here are the assumptions I am making for this to work:

* All your projects use the same `groupid`, in this case `com.xyz`.
* Your project directories are named after the maven projects, if this is not the case you will need a mapping between your maven project name and the project directory's name on the filesystem.

First, we get hold of the current project and its dependencies using `mvn`.

```
$ CUR_PROJ=$(mvn -DincludeGroupIds=com.ef dependency:list | grep Building | awk '{print $3}')
$ mvn -DincludeGroupIds=com.xyz dependency:list | grep com.xyz | awk -F':' -v proj=$CUR '{print $2 "\t" proj}' >> /tmp/dependencies
```

This writes the output to a file `/tmp/dependencies` which stores the partial ordering. Next, we use topological sorting to generate a linear list of build projects starting from the base dependencies to higher.

```
for proj in $(tsort /tmp/dependencies); do
    cd $proj
    git pull
    mvn install -DskipTests=true
    cd ..
done
```

This way we can be sure that our dependencies are up to date. There must be easier ways to do this using `mvn`, but this works for me for now.
