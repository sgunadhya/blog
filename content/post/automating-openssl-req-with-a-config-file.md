+++
author = "Sushant Srivastava"
description = "Automating openssl req with a config file"
draft = false
keywords = ["openssl", "automation", "pki"]
title = "Automating openssl req with a config file" 
topics = ["openssl", "automation", "pki"]
type = "post"
date ="2015-05-26" 
slug = "automating-openssl-req-with-a-config-file" 
tags = ["openssl", "automation", "pki"]
+++


+++ title = "Automating openssl req with a config file" date =
"2015-05-26" slug = "automating-openssl-req-with-a-config-file" tags =
\["openssl", "automation", "pki"\] category = \["automation"\] summary =
"Automate openssl req using a config file"

+++

The other day I was trying to generate a Certificate Signing Request
using the `openssl` command . The [openssl](https://www.openssl.org)
command supports [a lot
of](https://www.openssl.org/docs/apps/openssl.html) commands, and if you
are like me, you always have difficulty remembering them.

`req`, `x509` and `ca` commands from `openssl` support providing options
using an INI-style configuration file. The config file option is useful
when running `openssl` commands in batch mode. The batch mode operation
saves time when you are trying to automate a series of steps using bash,
one of which involves using the `opnessl` command to generate a CSR or
sign a certificate.

Let us suppose you want to generate a CSR for your server. You use a
command like so:

You will then enter an interactive mode where you will need to enter
details like Country, Organization Unit etc.

To automate this, you can create a INI-style config file `csr.conf` like
so:

You can then generate your CSR like so:

``` {.sourceCode .bash}
SERVER=www.orom-staging.in openssl req -nodes -config csr.conf -out orom-staging.in.csr
```
