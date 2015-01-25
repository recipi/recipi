# -*- coding: utf-8 -*-
import os
import pkg_resources

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipi.conf.development')


try:
    import sphinx_rtd_theme
except ImportError:
    sphinx_rtd_theme = None


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage']

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'recipi'
copyright = u'2015, Benjamin Banduhn, Christopher Grebs'

import ipdb; ipdb.set_trace()
dist = pkg_resources.get_distribution('recipi')
version = release = dist.version

exclude_patterns = []

pygments_style = 'sphinx'

if sphinx_rtd_theme:
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
else:
    html_theme = 'default'

html_static_path = ['_static']

htmlhelp_basename = 'recipidoc'

latex_elements = {}

latex_documents = [
    ('index', 'recipi.tex', u'recipi Documentation',
     u'recipi', 'manual'),
]

man_pages = [
    ('index', 'recipi', u'recipi Documentation',
     [u'recipi'], 1)
]

texinfo_documents = [
    ('index', 'recipi', u'recipi Documentation',
     u'recipi', 'recipi', 'Nutrition database and meal planner',
     'Miscellaneous'),
]

epub_title = u'recipi - Nutrition database and meal planner'
epub_author = u'Benjamin Banduhn, Christopher Grebs'
epub_publisher = u'Benjamin Banduhn, Christopher Grebs'
epub_copyright = u'2015, Benjamin Banduhn, Christopher Grebs'

intersphinx_mapping = {'http://docs.python.org/': None}
