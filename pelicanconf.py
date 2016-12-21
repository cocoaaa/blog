#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hae Jin Song'
SITENAME = u'small simplicity'
SITEURL = ''

# path
PATH = 'content'
STATIC_PATH = ['images', 'pdfs']
THEME = 'theme'

# time 
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

# date format
DATE_FORMATS = {
    'en': '%Y-%m-%d',
}
DEFAULT_DATE = 'fs'
WITH_FUTURE_DATES = True

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# side bar
SIDEBAR_NAME = 'Hae Jin Song (Hayley)'
SIDEBAR_SUBNAME = 'computer vision | 3D reconstruction | machine learning'
SIDEBAR_EMAIL = '<i>firstname</i>.<i>lastname</i>@mit.edu'
SIDEBAR_LOCATION = 'Cambridge, MA'
SIDEBAR_TAGS = ['cv',
                'ml',
                'recognition',
		'semantics']

# menu bar
MENUITEMS = [('Home', '/'),
             ('Projects', '/projects/'),
             ('Publications', '/pubs/'),
             ('About', '/about/'),
             ]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
