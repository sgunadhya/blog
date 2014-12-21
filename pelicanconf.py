#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pyembed.rst import PyEmbedRst
PyEmbedRst().register()

AUTHOR = u'Sushant'
SITENAME = u'orom'
SITEURL = ''
DISQUS_SITENAME='oromin'

PATH = 'content'


DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
THEME='tuxlite_tbs'
PLUGIN_PATHS=["plugins" , "/Users/susrivas/pelican-plugins"]
SOCIAL = (('twitter', 'http://twitter.com/ssushant'),
          ('github', 'http://github.com/mitra-varuna'))
CHECK_MODIFIED_METHOD='mtime'
GOOGLE_ANALYTICS='UA-57632501-1'

# Blogroll

# Social widget

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
