project = 'Full documentation'
copyright = '2026, khalandar'
author = 'khalandar'
release = '1.0'


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinxcontrib.plantuml',
]

# Optional (if plantuml not in PATH)
plantuml = 'plantuml'

templates_path = ['_templates']
exclude_patterns = []


html_theme = 'furo'
html_static_path = ['_static']
