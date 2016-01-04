#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)

AUTHOR = u'Philip Marc Schwartz'
AUTHOR_EMAIL = u'philip@progmad.com'
TWITTER_USERNAME = 'xhypno402'
SITENAME = u'Stalking the Programing world'
SITEURL = u'http://localhost:8000'

PATH = 'content'

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid']

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    'assets',
    'sitemap',
    'gravatar',
    'related_posts',
    'series',
    'tipue_search',
    'liquid_tags.img',
    'liquid_tags.video',
    'liquid_tags.youtube',
    'liquid_tags.vimeo',
    'liquid_tags.include_code',
    'tag_cloud',
]

DIRECT_TEMPLATES = [
    'archives',
    'authors',
    'categories',
    'index',
    'search',
    'tags',
    'tipue_search',
]

TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'

# Theme related values
THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
PYGMENTS_STYLE = "native"
# BOOTSTRAP_FLUID = True
DISPLAY_BREADCRUMBS = True
# DISPLAY_CATEGORY_IN_BREADCRUMBS = True
BOOTSTRAP_NAVBAR_INVERSE = True
RELATED_POSTS_MAX = 10
DISPLAY_ARTICLE_INFO_ON_INDEX = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
RECENT_POST_COUNT = 5
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_MAX_ITEMS = 10
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_SERIES_ON_SIDEBAR = True
SHOW_SERIES = True
DOCUTIL_CSS = True
#CC_LICENSE = "CC-BY-NC-SA"

SHOW_ARTICLE_AUTHOR = True
SHOW_DATE_MODIFIED = True

CUSTOM_CSS = 'static/custom.css'

STATIC_PATHS = [
    'images',
    'files',
    'extra/robots.txt',
    'extra/custom.css',
    'extra/CNAME',
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/CNAME': {'path': 'CNAME'}
}

# Addthis
ADDTHIS_PROFILE = u'ra-568734d5aaae4d18'

# GITHUB_USER = u'pschwartz'
# GITHUB_SKIP_FORK = True

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = None

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/xhypno402'),
    ('github', 'http://github.com/pschwartz'),
    ('google-plus', 'https://plus.google.com/+PhilipSchwartzRax'),
    ('linkedin', 'https://www.linkedin.com/in/philip-schwartz-a18126a'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'

DEFAULT_DATE_FORMAT = ('%d/%b/%Y %a')
ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

