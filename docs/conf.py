# -*- coding: utf-8 -*-
#
# build configuration file, created by
# sphinx-quickstart on Mon Nov 10 16:33:38 2008.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# All configuration values have a default value; values that are commented out
# serve to show the default value.

# from __future__ import unicode_literals

extlinks = {}
extensions = []
templates_path = []

# import lino
# from lino.sphinxcontrib import configure
from atelier import sphinxconf

sphinxconf.configure(globals())  #, 'lino_book.projects.min1.settings.doctests')

# from atelier.sphinxconf import interproject
# interproject.configure(globals())

# extensions += ['atelier.sphinxconf.blog']
# extensions += ['atelier.sphinxconf.complex_tables']
extensions += ['lino.sphinxcontrib.logo']
extensions += ['lino.sphinxcontrib.base']  # for tcname
# extensions += ['sphinxcontrib.taglist']
# extensions += ['sphinxcontrib.youtube']
extensions += ['sphinx.ext.inheritance_diagram']

# extensions += ['atelier.sphinxconf.sigal_image']

# sigal_base_url = 'http://sigal.saffre-rumma.net'


# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#sys.path.append(os.path.abspath('some/directory'))

# General configuration
# ---------------------

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['.templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General substitutions.
project = "Lino Community Guide"
copyright = '2019-2020 Rumma & Ko Ltd'


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%d.%B.%Y'


# Note 20100703 : unused_docs and exclude_trees  replaced by exclude_patterns

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['.build/*', 'shared/*']
exclude_patterns.append('locales/*')

# List of documents that shouldn't be included in the build.
#unused_docs = []



# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Lino Community Guide"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "Home"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "logo2.jpg"
# html_logo = "logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['.static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%Y-%m-%d'
#~ html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True


# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
#html_copy_source = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''
# html_use_opensearch = lino.SETUP_INFO['url']

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'lcg'


# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [
  ('directives/index', 'cd.tex', 'Cooperation Directives', 'Rumma \& Ko Ltd', 'article', True),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

# extlinks.update(ticket=('http://trac.lino-framework.org/ticket/%s', '#'))
# extlinks.update(ticket=('javascript:alert("Sorry, linking to tickets (%s) is not yet implemented!")', '#'))
# extlinks.update(ticket=('http://bugs.saffre-rumma.net/tickets/Ticket/%s', '#'))
extlinks.update(ticket=('https://hobbit.saffre-rumma.net/#/api/tickets/AllTickets/%s', '#'))

html_sidebars = {
    '**': ['languages.html', 'globaltoc.html', 'searchbox.html', 'links.html'],
}

# html_theme = "classic"
# html_theme_options = dict(collapsiblesidebar=True, externalrefs=True)

# html_theme = "bizstyle"
# html_theme_options = dict(collapsiblesidebar=True, externalrefs=True)

# blogref_format = "http://luc.lino-framework.org/blog/%Y/%m%d.html"

inheritance_graph_attrs = dict(rankdir="TB")
# inheritance_graph_attrs.update(size='"12.0, 16.0"')
inheritance_graph_attrs.update(size='"48.0, 64.0"')
inheritance_graph_attrs.update(fontsize=14, ratio='compress')

if False:
    # extensions += ['yasfb']
    # extensions += ['sphinxcontrib.feed']
    extensions += ['sphinxfeed']
    # NB : not the public sphinxfeed but my extended version
    feed_base_url = 'https://community.lino-framework.org'
    feed_author = 'Luc Saffre'
    feed_title = "Lino Community Guide"
    feed_field_name = 'date'
    feed_description = "News about the Lino Community"

# extensions += ['hieroglyph']  # Generate HTML presentations
# autoslides = False
# slide_numbers = True

import os
os.environ['LC_TIME'] = 'de_BE.UTF-8'

# from pprint import pprint
# pprint(intersphinx_mapping)
#
# raise foo

language = 'en'
locale_dirs = ['locales/']
gettext_compact = False
translated_languages = ['de', 'fr']  # used by atelier
