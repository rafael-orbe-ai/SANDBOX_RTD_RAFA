# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ORBE.AI'
copyright = '2021, Orbe.AI'
author = 'Orbe.AI'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
    'IPython.sphinxext.ipython_directive',
    'sphinx_thebe'
]

thebe_config = {
    "repository_url": "https://github.com/binder-examples/jupyter-stacks-datascience",
    "path_to_docs": "docs"
}


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_logo = 'logo_orbe.png'

html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'use_download_button': True
}

# -- Options for EPUB output
epub_show_urls = 'footnote'



def setup(app):
    app.connect('builder-inited', create_archives)


def create_archives(app):
    '''Creates an .tar.xz archive in _downloads for each entry in _archives.'''

    import os
    import tarfile
    from sphinx.util import logging

    _ARCHIVE_DIR = '_archives'
    _DOWNLOAD_DIR = '_downloads'

    logger = logging.getLogger(__name__)
    cwd = os.getcwd()
    archivedir = os.path.join(cwd, _ARCHIVE_DIR)
    downloaddir = os.path.join(cwd, _DOWNLOAD_DIR)
    if not os.path.exists(downloaddir):
        os.makedirs(downloaddir)
    archives = os.listdir(archivedir)
    for archive in archives:
        tarname = os.path.join(_DOWNLOAD_DIR, archive + '.tar.gz')
        tarpath = os.path.join(cwd, tarname)
        filename = os.path.join(_ARCHIVE_DIR, archive)
        filepath = os.path.join(cwd, filename)
        tartime = os.path.getmtime(tarpath) if os.path.exists(tarpath) else 0.0
        filetime = _newest_modification_time(filepath)
        if tartime <= filetime:
            with tarfile.open(tarpath, 'w:gz') as tar:
                tar.add(filepath, arcname=archive)
            logger.info('Created archive {} from {}'.format(tarname, filename))
        else:
            logger.info('Skipped unchanged archive {} from {}'\
                        .format(tarname, filename))


def _newest_modification_time(filepath):
    '''Returns the newes modification time of any file below a given folder.'''
    import os
    mtime = 0.0
    for root, dirs, entries in os.walk(filepath):
        for entry in entries:
            entrytime = os.path.getmtime(os.path.join(root, entry))
            mtime = max(mtime, entrytime)
    return mtime
