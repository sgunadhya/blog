+++ 
title = "Extracting public key from pem file" 
slug ="extracting-public-key-from-pem-file" 
date = "2015-05-28" 
tags = ["automation", "pki"] 
summary = "Extracting public key from a pem file" 
author = "Sushant Srivastava"
draft = false
+++

If you need to extract the public key from your
[PEM](http://en.wikipedia.org/wiki/Privacy-enhanced_Electronic_Mail)
format certificate file, you can use the `ssh-keygen` command for this
like so:

{{< highlight bash >}}
    ssh-keygen -f certificate.pem -y
{{< / highlight >}}


where `certificate.pem` is your pem file. This command will output the
public key on `stdout`.
