# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example:
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'FreeTaxUSA 2024 Tax Filing Guide'
copyright = '2025, FreeTaxUSA'
author = 'FreeTaxUSA Help Center Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# SEO Title shown in the browser tab and at the top of HTML pages
html_title = "FreeTaxUSA 2024: File Your Taxes Online for Free with Maximum Accuracy"

# Optional short title (e.g., for nav bar)
html_short_title = "FreeTaxUSA 2024 Guide"

# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'

# Theme selection (uncomment if using a specific one)
# html_theme = 'sphinx_rtd_theme'

# Hide "View page source" link
html_show_sourcelink = False

# Allow raw HTML in .rst files
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Template and static file paths
templates_path = ['_templates']
# html_static_path = ['_static']  # Uncomment if needed

# Files and directories to ignore
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
