#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

from __future__ import unicode_literals

AUTHOR = u'Universidad de La Laguna'
SITENAME = u'Carta de Servicios'
# SITEURL = '<site_url>'

PATH = 'content'

TIMEZONE = 'Atlantic/Canary'

DEFAULT_LANG = u'en'

# Disable link generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ULL_CSS_URL = 'http://static.ull.es/v3/dist/css/ull.min.css'

# Blogroll
GENERIC_BLOCKS = [
    {
        'fa_icon': 'fa-external-link-square',
        'title': 'Links',
        'content': [
            '<a href="http://www.ull.es/" target="_blank"><img width="80%" style="margin-left: 10%; margin-right: 10%; margin-bottom: 5%;" title="Universidad de La Laguna" src="images/ull.png"></img></a>',
        ]
    },
    {
        'fa_icon': 'fa-cogs',
        'title': 'Tecnología',
        'content': [
			'<div class="panel-body" style="text-align: center;">',
				'<a href="http://www.djangoproject.com/" target="_blank"><img src="https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif" border="0" alt="Powered by Django." title="Powered by Django."/></a>',
				'<a href="https://www.python.org/" target="_blank"><img src="images/python.png" border="0" alt="Python" title="Python"/></a>',
				'<a href="http://www.archimatetool.com/" target="_blank"><img src="images/archi.png" border="0" width="128" height="56" alt="Archimate" title="Archimate"/></a>',
				'<a href="https://www.opengroup.org/togaf9/cert/showcase/participants/ffcg/index.html" target="_blank"><img src="images/togaf.jpg" border="0" width="128" height="56" alt="Togaf" title="Togaf"/></a>',
			'</div>',
        ]
    },
]

# Social widget
"""
SOCIAL = (('Facebook', '<facebook_url>'),
          ('Twitter', '<twitter_url>'),
          ('Google plus', '<google_plus_url>'),
          ('Youtube', '<youtube_url>'),)
"""

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'themes/pelican-bootstrap3-imagenull'
# JUMBOTRON_IMAGE_URL='images/banner.jpg'

STATIC_PATHS = ['images', 'css', 'js', 'php']
# Uncomment to be able to use the contact form
# CUSTOM_JS='js/app.js'

# Páginas
PAGE_ORDER_BY = 'sortorder'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

# Panel de financiadores
"""
WORK_SUPPORTED_BY_HTML = (('This work is being supported by <suporter>'),
                          ('<You can put here html, like an image>'),)
"""

# Licencia
"""
LICENSE = (
    ('License url'),
    ('License image link'),
)
"""

# Technology
"""
TECHNOLOGY = (('<You can put here html, like an image>'),)
"""

# Desactivar elementos propios de un blog
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_ARCHIVES_ON_MENU = False

TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
ARTICLE_SAVE_AS = ''

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

GITHUB_REPO = 'https://github.com/RocioDSI/Carta-Servicios-STIC.git'

PLUGIN_PATHS = ["plugins", THEME + "/plugins", ]
PLUGINS = ['toc', ]

TOC_TITLE = u'Table of Content'
