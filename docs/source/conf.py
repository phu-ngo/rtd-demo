# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Endpoint Engineering'
copyright = '2025, EEP'
author = 'Phu, Thien'

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
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = "shibuya"

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Localization configuration

locale_dirs = ['locale/']  # Path to translation files
gettext_compact = False  # Use separate .po files for each document

# -- Language configuration

language = 'en'  # Default language

# -- Customization for multiple languages

html_context = {
    'languages': [
        ("English", "/%s/", 'en')
    ],
}
# Customizing the theme options
# This is where you can set theme-specific options
html_theme_options = {
    "logo_target": "/",
    "light_logo": "_static/logo_light.svg",
    "dark_logo": "_static/logo_dark.svg",

    "og_image_url": "https://shibuya.lepture.com/icon.png",
    "twitter_creator": "lepture",
    "twitter_site": "lepture",

    "discussion_url": "https://github.com/lepture/shibuya/discussions",
    "twitter_url": "https://twitter.com/lepture",
    "github_url": "https://github.com/lepture/shibuya",

    "globaltoc_expand_depth": 1,
    "nav_links": [
        {
            "title": "Platforms",
            "url": "writing",
            "children": [
                {
                    "title": "Admonitions",
                    "url": "writing/admonition",
                    "summary": "Bring the attention of readers",
                },
                {
                    "title": "Code Blocks",
                    "url": "writing/code",
                    "summary": "Display code with highlights",
                },
                {
                    "title": "Autodoc",
                    "url": "writing/api",
                    "summary": "API documentation automatically"
                },
                {
                    "title": "Jupyter Notebook",
                    "url": "extensions/nbsphinx",
                    "summary": "Rendering .ipynb files"
                },
            ]
        },
        {
            "title": "Branding",
            "url": "branding",
        },
        {
            "title": "Sponsor me",
            "url": "https://github.com/sponsors/lepture",
            "external": True,
        },
    ]
}