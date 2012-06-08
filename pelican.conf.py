#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Kfir Breger"
SITENAME = u"kfirbreger.com"
SITEURL = '/blog'

THEME = './'
DEFAULT_CATEGORY = 'Uncategorized'

# /year/month/article
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
PAGE_URL = '{date:%Y}/{date:%m}/pages/{slug}.html'
PAGE_LANG_URL = '{date:%Y}/{date:%m}/pages/{slug}-{lang}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
PAGE_SAVE_AS = '{date:%Y}/{date:%m}/pages/{slug}.html'
PAGE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/pages/{slug}-{lang}.html'

ARTICLES_ON_INDEX = 20 # Number of articles to show in the index page

TIMEZONE = "Europe/Amsterdam"

DEFAULT_LANG='en'

# Blogroll
LINKS =  (
    ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
    ('Python.org', 'http://python.org'),
    ('Jinja2', 'http://jinja.pocoo.org'),
    ('You can modify those links in your config file', '#')
         )

# Social widget
SOCIAL = (
          ('You can add links in your config file', '#'),
         )

TWITTER_USERNAME = 'kfirbreger'

DEFAULT_PAGINATION = False