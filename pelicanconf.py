#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# https://raw.githubusercontent.com/getpelican/pelican/master/samples/pelican.conf.py

from __future__ import unicode_literals
from landing_page import *
from profile import *


AUTHOR = u'Hayley Song'
SITENAME = u'small simplicity'
SITESUBTITLE = u'hae jin song // hayley'
#SITEURL = 'http://cocoaaa.github.io/blog'
TIMEZONE = 'America/New_York'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%Y-%m-%d(%a)'
DEFAULT_LANG = u'en'

# Paths
PATH = 'content'
PAGE_PATHS = ['pages', 'pubs'] # A list of directories and files to look at for pages, relative to PATH.
#ARTICLE_PATHS = ['posts',] #output folder for articles

# add the following directories to the output folder as is
STATIC_PATHS = ['images', 'pdfs']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'misc'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Design
TYPOGRIFY = True
#MD_EXTENSIONS = ['codehilite(css_class=codehilite code)']

THEME = 'themes/elegant' # path relative to the settings file. Need it to generate the correct html??(ie. for local use?)
#CSS_FILE = "themes/elegant/static/css/solarizedlight.css"

THEME_STATIC_DIR = 'theme' #destination directory in the output path
THEME_STATIC_PATHS = ['themes/elegant'] #static theme paths you want to copy

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
TAG_SAVE_AS = ''
### From Elegant theme config
#DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
DIRECT_TEMPLATES = (('index', 'search'))
## archieve
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('Github', 'https://cocoaaa.github.com'),
        ('LinkedIn', 'http://https://www.linkedin.com/in/hayleysong'),
        )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
#DISPLAY_PAGES_ON_MENU = False

#Don't show published date for pages
#Look at page.html
#page = {'date': False}; this is wrong. should be set in each page md's metafield

# Prevent caching of previous settings (esp. the metadata ones)
LOAD_CONTENT_CACHE = False
