+++
title = "Getting the list of older versions of a Pypi Package"
draft = false
description = "Getting the list of older versions of a Pypi Package"
keywords = ["pypi","versions"]
topics = ["PyPI"]
tags = ["pypi","versions"]
date = "2016-10-03T19:03:53+05:30"
type = "post"
author = "Sushant Srivastava"
 +++

As of right now, there's no link on PyPI to list older versions of a package.
I was looking for an older version of oauth2client package on PyPI, but could not find
any link on the package's page.

It turns out there is a JSON API which lists any package's metadata. As an example,
this URL lists all the old versions of oauth2client.
```
https://pypi.python.org/pypi/oauth2client/json
```
I used the [jq](https://stedolan.github.io/jq/) tool to list out any package's versions.

```bash
curl -s "https://pypi.python.org/pypi/$1/json" | jq '.releases | to_entries[] | .key '
```

And as a shell function

```bash
function lspip {
  if [[ -z "$1" ]]; then
    echo usage :$0 package
    return 1
  fi
  curl -s "https://pypi.python.org/pypi/$1/json" | jq '.releases | to_entries[] | .key '
}
```

This is useful when you want to quickly list out all the versions of any PyPI package.
