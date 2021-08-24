+++
title = "Writing Pipe-able Python Scripts"
slug = "Writing Pipe-able Python Scripts"
date = "2020-06-30"
tags = ["python", "productivity", "script"]
category = ["python", "productivity", "script"]
description = "Writing Pipe-able Python Scripts"
author = "Sushant Srivastava"
draft = false
+++

I have written many Python scripts over the course of many years.
I wrote the scripts for tasks like data cleanup, data extraction,
integration scripts and what not. In retrospect, the majority of the 
scripts I wrote were standalone, or custom unix bash scripts glued them
together. Recently, I had an opportunity to write a Python script which 
was a part of a larger pipleine of scripts for data transformation. 
I wanted the script to be used in the pipeline without any custom glue code.


Doug McIlroy, the inventor of Unix pipes, had this to say about writing programs 
in-line with Unix philosophy

> Expect the output of every program to become the input to another, as yet unknown, program. Don't clutter output with extraneous information. Avoid stringently columnar or binary input formats. Don't insist on interactive input.

This principle became my North star when I emabarked on writing the script.


### Input ###

Right off the gate, I wanted to zero-in on how we specify input and the output for the script.
One possible solution could be to use the command line arguments. Conventionally, the first argument
is the input, and the second argument is the output. The problem with this approach is that it is not 
clear whether the files specified as the command-line arguments are all input or they are input and output
respectively. One solution is to use long-form options, like `--input` and `--output`. I am on the fence 
about this choice, but [explicit is always better than implicit](https://www.python.org/dev/peps/pep-0020/).

#### Just Read from `stdin` ####

To be a part of the pipeline, the script should read the input from the standard input.
We have an additional constraint, that the input can be supplied using the long-form command option.
We can have a check which tests if the input is supplied, if not we revert to `sys.stdin`.
This will work, but I wanted a more generic solution.

#### `fileinput` To the Rescue ####

Can we do better?

It turns out the module `fileinput` iterates over the lines of all the files listed in 
the argument, and if the file list is empty, then it defaults to `sys.stdin`. A perfect solution
which covers all the bases. Here's what I came up with:
```python
   lines = [line.strip() for line in fileinput.input(args.input)]
```


### Output ###
Next, the output. Let us recapitulate our constraints

1. The script following the current script in the pipeline should be able to use the output as its input.
2. We should be able to write to the file provided using the long-form option.

One can always argue that we can use the redirection operator `>>` to write to the file, but for the
sake of uniformity, I am not looking into that option.

This is what I came up with after a few tries:

```python
    try:
        with open(args.output, 'w') as output_file:
            output_file.write(output)
    except TypeError:
        sys.stdout.write(output)
```



#### Is this Pythonic though? ####

Is the code with try-catch block Pythonic? People coming from other languages than Python are skeptical of this code.
At the outset, this code looks like it does not check for pre-conditions and leaps into computation without any
safety-harness. Surely, that looks unsafe.

I invoke the doctrine of [***EAFP***.](https://docs.python.org/3.4/glossary.html#:~:text=Easier%20to%20ask%20for%20forgiveness,many%20try%20and%20except%20statements.)

It is easier to ask for forgiveness than permission. `try-and-catch` pattern is the corenerstone of this programming
style.



### Conclusion ###

I had begun to seek a generic solution to the pipe-able Python script problem.
I wouldn't say that the solution is perfect, but as a template this works fine for my use-case.


```python

    def main():
		parser = argparse.ArgumentParser(description='Script Description')
		parser.add_argument('--input', action='store', dest='input', metavar='FILE', help='Input file')
		parser.add_argument('--output', action='store', dest='output', metavar='FILE', help='Output file')
		
		lines = [line.strip() for line in fileinput.input(args.input)]
		
		# do something with the lines
		
		try:
			with open(args.output, 'w') as output_file:
				output_file.write(output)
	    except TypeError:
		    sys.stdout.write(output)
```

