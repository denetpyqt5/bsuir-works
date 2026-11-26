# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "ppois-second"
copyright = "2026, denetpyqt5"
author = "denetpyqt5"


import os
import sys

sys.path.insert(
    0,
    os.path.abspath(
        r"C:\Users\aieng\OneDrive\Desktop\bsuir-works\ppois\second\src\second"
    ),
)

extensions = [
    "sphinx.ext.autodoc",  # Ядро: извлекает докстринги из кода
    "sphinx.ext.napoleon",  # Позволяет понимать Google/NumPy стиль докстрингов
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",  # (Опционально) Добавляет ссылки на исходный код
]


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
