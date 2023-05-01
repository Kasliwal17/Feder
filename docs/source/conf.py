# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Feder'
copyright = '2023, ---'
author = '---'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'autoapi.extension',  # this one is really important
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinxcontrib.napoleon',
    'sphinx.ext.autosectionlabel',  # allows referring sections its title, affects `ref`
    'sphinx_design',
    'sphinxcontrib.bibtex',
]
# for 'sphinxcontrib.bibtex' extension
bibtex_bibfiles = ['refs.bib']
bibtex_default_style = 'unsrt'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# # configuration for 'autoapi.extension'
# autoapi_type = 'python'
# autoapi_dirs = ['../../fedlab']
# autoapi_template_dir = '_autoapi_templates'
# add_module_names = False  # makes Sphinx render package.module.Class as Class

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
