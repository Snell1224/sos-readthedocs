# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SOS'
copyright = '2023, Sandia National Laboratories and Open Grid Computing, Inc.'
author = 'SNL/OGC'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    "ovis-hpc": ("https://ovis-hpc.readthedocs.io/en/latest/", None),
}
intersphinx_disabled_domains = ['std']
intersphinx_disabled_reftypes = ["*"]

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['static']
#html_logo = "images/ovis-logo.png"
html_theme_options = {
    #'logo_only': True,
    'display_version': True,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
