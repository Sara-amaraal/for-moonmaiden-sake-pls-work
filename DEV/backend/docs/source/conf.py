# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import pathlib
import sys
import os
import django

# Insert the \backend directory into the directories list
sys.path.insert(0, pathlib.Path(
    __file__).parents[2].resolve().as_posix()+'\\main')

# Setting django's environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
django.setup()

project = 'Quirked Up Software'
copyright = '2023, PL2'
author = 'PL2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# EPUB options
epub_show_urls = 'footnote'
