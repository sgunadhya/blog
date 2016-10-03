+++
title = "Getting the list of older versions of a Pypi Package"
draft = true
description = "Getting the list of older versions of a Pypi Package"
keywords = [
  "pypi",
  "versions",
]
topics = [
  "PyPI",
]
tags = [
  "pypi",
  "versions",
]
date = "2016-10-03T19:03:53+05:30"
type = "post"
author = "Sushant Srivastava"
 +++
As of right now, there's no link on PyPI to list older versions of a package.
I was looking for an older version of oauth2client package on PyPI, but could not find
any link on the package's page.

It turns out there is a JSON API which lists any package's metadata.

https://pypi.python.org/pypi/oauth2client/json
* JSON API
* using jq
