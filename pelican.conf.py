#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Kfir Breger"
SITENAME = "kfirbreger.com"
SITEURL = 'http://blog.kfirbreger.com'

THEME = './'
DEFAULT_CATEGORY = 'Uncategorized'
PAGE_EXCLUDES = ('draft')
PAGE_DIR = ('pages')
ARTICLE_DIR = ('src')

# /year/month/article
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
PAGE_SAVE_AS = '{date:%Y}/{date:%m}/pages/{slug}.html'
PAGE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/pages/{slug}-{lang}.html'

ARTICLES_ON_INDEX = 10 # Number of articles to show in the index page

FEED_ALL_ATOM = 'feeds/all.atom.xml'

# STATIC_PATHS = ['images', 'css', 'js']

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
          ('twitter', 'http://twitter.com/kfirbreger'),
         )

#TWITTER_USERNAME = 'kfirbreger'

DEFAULT_PAGINATION = False

PLUGIN_PATH = '/Users/kfir/venvs/blog/pelican-plugins'
PLUGINS = ['sitemap',]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}