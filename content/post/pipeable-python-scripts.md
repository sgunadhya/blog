+++
title = "Writing Pipe-able Python Scripts"
slug = "Writing Pipe-able Python Scripts"
date = "2020-06-25"
tags = ["python", "productivity", "script"]
category = ["python", "productivity", "script"]
description = "Writing Pipe-able Python Scripts"
author = "Sushant Srivastava"
draft = true
+++

* Written Python Scripts
* Opprtunity to write Python script 
*[B] Wanted to be pipe-able
*[T] Looked into internet

* sys.stdin
* [B] Issue with Stdin
* [T] switched to fileinput


* [B]What about the output?
*[T] Looking for output patterns.


[A]Write to stdout
[B]What about if the user provides an output file
[T] Try catch pattern - Python zen

[A]Long option vs arguments
[B]Confusing
[T]Long options

```python
    parser = argparse.ArgumentParser(description='Generate package.xml for metadata export')
    parser.add_argument('--input', action='store', dest='input', metavar='FILE', help='Input file which has the name of metadata line by line')
    parser.add_argument('--output', action='store', metavar='FILE', dest='output', help='Generated package.xml file location')
```

```python
   lines = [line.strip() for line in fileinput.input(args.input)]
```

```python
    try:
        with open(args.output, 'w') as h:
            h.write(output)
    except TypeError:
        sys.stdout.write(output)
```



