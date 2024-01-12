# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Bouncmpe Web Templates'
copyright = '2024, Department of Computer Engineering, Boğaziçi University'
author = 'Dogan Ulus'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_inline_tabs",
]

myst_title_to_header = True
myst_heading_anchors = 3
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "attrs_block",
    "attrs_inline",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "My Computer Engineering Laboratory"
html_short_title = "BounCmpeLab"
html_theme = 'furo'
html_static_path = ['_static']
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
]
html_theme_options = {
    "navigation_with_keys": True,
    "top_of_page_button": "edit",
    # "light_logo": "boun_logo.png",
    # "dark_logo": "boun_logo.png",
    # "light_css_variables": {
    #     "color-brand-primary": "#1e4a8b",
    #     "color-brand-content": "#1e4a8b",

    #     "color-foreground-primary": "#2e3440", # for main text and headings
    #     "color-foreground-secondary": "#4c566a", # for secondary text
    #     "color-foreground-muted": "#d8dee9", # for muted text
    #     "color-foreground-border": "#3b4252", # for content borders     

    #     "color-background-primary": "#eceff4",
    #     "color-background-secondary": "#eceff4",
    #     "color-background-hover": "#4c566a",
    #     "color-background-hover--transparent":"#fff",
    #     "color-background-border":"#e5e9f0",
    #     "color-background-item":"#fff",

    #     "color-admonition-background": "orange",
    # },
    # "dark_css_variables": {
    #     "color-brand-primary": "#1e4a8b",
    #     "color-brand-content": "#8cc8ea",

    #     "color-background-primary": "#2e3440",
    #     "color-background-secondary": "#2e3440",
    #     "color-background-hover": "#4c566a",
    #     "color-background-hover--transparent":"",
    #     "color-background-border":"#4c566a",
    #     "color-background-item":"#4c566a",

    #     "color-admonition-background": "orange",

    # },
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/bouncmpe/#",
            "html": "",
            "class": "fa-brands fa-solid fa-git-alt fa-2x",
        },
    ],
    "source_repository": "https://github.com/bouncmpe/#",
    "source_branch": "main",
    "source_directory": "content",
}
