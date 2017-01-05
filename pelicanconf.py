#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# https://raw.githubusercontent.com/getpelican/pelican/master/samples/pelican.conf.py

from __future__ import unicode_literals

AUTHOR = u'Hayley Song'
SITENAME = u'small simplicity'
SITESUBTITLE = u'this is a subtitle'
SITEURL = 'http://cocoaaa.github.io/blog'
TIMEZONE = 'America/New_York'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%Y-%m-%d(%a)'

DEFAULT_LANG = u'en'

# Paths
PATH = 'content'
PAGE_PATH = ['pages']
#ARTICLE_PATHS = ['posts',] #output folder for articles

# add the following directories to the output folder
STATIC_PATHS = ['images', 'pdfs']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Design
TYPOGRIFY = True
#MD_EXTENSIONS = ['codehilite(css_class=codehilite code)']

THEME = 'themes/elegant' # path relative to the settings file
#CSS_FILE = "css/hyde.css"

THEME_STATIC_DIR = '_theme' #destination directory in the output path
#THEME_STATIC_PATHS = [''] #static theme paths you want to copy

# Link and Save
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

## URL to refer to an article draft
## and place we will save an article draft
DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'

## If you do not want one or more of the default pages to be created (e.g., you are the only author on your site and thus do not need an Authors page), set the corresponding *_SAVE_AS setting to ''
AUTHOR_SAVE_AS = ''

## archieve
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://cocoaaa.github.com'),
        ('LinkedIn', 'http://todo'),
        )

DEFAULT_PAGINATION = 10


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
#DISPLAY_PAGES_ON_MENU = False


# Prevent caching of previous settings (esp. the metadata ones)
LOAD_CONTENT_CACHE = False
