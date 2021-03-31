# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'PBPL010S21'
copyright = '2021, Sergio Rey'
#author = 'Sergio Rey'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        "myst_parser"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
#import sphinx_theme_pd
#html_theme = 'sphinx_theme_pd'
#html_theme_path = [sphinx_theme_pd.get_html_theme_path()]

#html_theme = 'sizzle'

html_theme = "sphinx_book_theme"
html_logo = "_static/logo.png"
html_title = ""
html_theme_options = {
    "repository_url": "https://github.com/sjsrey/pbpl010s20",
    "home_page_in_toc": True
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
    'logo': 'logo.png',
    'github_user': 'sjsrey',
    'github_repo': 'pbpl010s20',
}



html_sidebars = {
   '**': ['searchbox.html', 'globaltoc.html'],
   'using/windows': ['windowssidebar.html', 'searchbox.html'],
}
