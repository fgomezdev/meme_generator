# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Meme Generator"
copyright = "2024, Fernando D. Gómez"
author = "Fernando D. Gómez"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Genera documentación a partir de los docstrings.
    "sphinx.ext.viewcode",  # Genera un enlace a la fuente de cada objeto.
    "autoapi.extension",  # Genera documentación a partir de los docstrings.
    "sphinx_copybutton",  # Agrega un botón para copiar el código de los bloques de código.
]

autoapi_dirs = [
    "../../src",
]

templates_path = ["_templates"]
exclude_patterns = []

language = "es"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = 'sphinx_rtd_theme'
html_theme = "renku"

html_static_path = ["_static"]
html_logo = "logo.jpg"


latex_documents = [("index", "meme_generator.tex", project, author, "manual")]
latex_logo = "logo.jpg"
