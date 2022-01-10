# Configuration file for the Sphinx documentation app.

# This file only contains a selection of the most common options. For a
# full list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from datetime import datetime
import inspect
import os
from os.path import relpath, dirname
import re
import sys

from kikuchipy import release as kp_release
import kikuchipy


# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
sys.path.append("../")

# Project information
project = "kikuchipy"
copyright = f"2019-{datetime.now().year}, {kp_release.author}"
author = kp_release.author
version = kp_release.version
release = kp_release.version

master_doc = "index"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinxcontrib.bibtex",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.linkcode",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "sphinx_gallery.load_style",
    "nbsphinx",
]

# Create links to references within kikuchipy's documentation to these
# packages
intersphinx_mapping = {
    "dask": ("https://docs.dask.org/en/stable", None),
    "diffpy.structure": ("https://www.diffpy.org/diffpy.structure", None),
    "diffsims": ("https://diffsims.readthedocs.io/en/latest", None),
    "hyperspy": ("https://hyperspy.org/hyperspy-doc/current", None),
    "matplotlib": ("https://matplotlib.org", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "orix": ("https://orix.readthedocs.io/en/stable", None),
    "python": ("https://docs.python.org/3", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    "skimage": ("https://scikit-image.org/docs/stable", None),
    "sklearn": ("https://scikit-learn.org/stable", None),
    "h5py": ("https://docs.h5py.org/en/stable", None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files. This image also
# affects html_static_path and html_extra_path.
exclude_patterns = ["build", "_static/logo/*.ipynb"]

# The theme to use for HTML and HTML Help pages. See the documentation
# for a list of builtin themes.
html_theme = "furo"

# Add any paths that contain custom static files (such as style sheets)
# here, relative to this directory. They are copied after the builtin
# static files, so a file named "default.css" will overwrite the builtin
# "default.css".
html_static_path = ["_static"]

# Syntax highlighting
pygments_style = "friendly"

# Logo
html_logo = "_static/logo/plasma_logo.svg"
html_favicon = "_static/logo/plasma_favicon.png"

# nbsphinx configuration
# Taken from nbsphinx' own nbsphinx configuration file, with slight
# modification to point nbviewer and Binder to the GitHub develop branch
# links when the documentation is launched from a kikuchipy version with
# "dev" in the version.
if "dev" in version:
    release_version = "develop"
else:
    release_version = "v" + version
# This is processed by Jinja2 and inserted before each notebook
nbsphinx_prolog = (
    r"""
{% set docname = 'doc/' + env.doc2path(env.docname, base=None) %}

.. raw:: html

    <style>a:hover { text-decoration: underline; }</style>

    <div class="admonition note">
      This page was generated from
      <a class="reference external" href="""
    + f"'https://github.com/pyxem/kikuchipy/blob/{release_version}"
    + r"""/{{ docname|e }}'>{{ docname|e }}</a>.
      Interactive online version:
      <span style="white-space: nowrap;"><a href="""
    + f"'https://mybinder.org/v2/gh/pyxem/kikuchipy/{release_version}"
    + r"""?filepath={{ docname|e }}'><img alt="Binder badge" src="https://mybinder.org/badge_logo.svg" style="vertical-align:text-bottom"></a>.</span>
      <script>
        if (document.location.host) {
          $(document.currentScript).replaceWith(
            '<a class="reference external" ' +
            'href="https://nbviewer.jupyter.org/url' +
            (window.location.protocol == 'https:' ? 's/' : '/') +
            window.location.host +
            window.location.pathname.slice(0, -4) +
            'ipynb">View in <em>nbviewer</em></a>.'
          );
        }
      </script>
    </div>

.. raw:: latex

    \nbsphinxstartnotebook{\scriptsize\noindent\strut
    \textcolor{gray}{The following section was generated from
    \sphinxcode{\sphinxupquote{\strut {{ docname | escape_latex }}}} \dotfill}}
"""
)
# https://nbsphinx.readthedocs.io/en/0.8.0/never-execute.html
nbsphinx_execute = "auto"  # always, auto, never
nbsphinx_allow_errors = True
nbsphinx_execute_arguments = [
    "--InlineBackend.rc=figure.facecolor='w'",
    "--InlineBackend.rc=font.size=15",
]

# sphinxcontrib-bibtex configuration
bibtex_bibfiles = ["bibliography.bib"]


# Relevant for the PDF build with LaTeX
latex_elements = {
    # pdflatex doesn't like some Unicode characters, so a replacement
    # for one of them is made here
    "preamble": r"\DeclareUnicodeCharacter{2588}{-}"
}


def linkcode_resolve(domain, info):
    """Determine the URL corresponding to Python object.

    This is taken from SciPy's conf.py:
    https://github.com/scipy/scipy/blob/develop/doc/source/conf.py.
    """
    if domain != "py":
        return None

    modname = info["module"]
    fullname = info["fullname"]

    submod = sys.modules.get(modname)
    if submod is None:
        return None

    obj = submod
    for part in fullname.split("."):
        try:
            obj = getattr(obj, part)
        except Exception:
            return None

    try:
        fn = inspect.getsourcefile(obj)
    except Exception:
        fn = None
    if not fn:
        try:
            fn = inspect.getsourcefile(sys.modules[obj.__module__])
        except Exception:
            fn = None
    if not fn:
        return None

    try:
        source, lineno = inspect.getsourcelines(obj)
    except Exception:
        lineno = None

    if lineno:
        linespec = "#L%d-L%d" % (lineno, lineno + len(source) - 1)
    else:
        linespec = ""

    startdir = os.path.abspath(os.path.join(dirname(kikuchipy.__file__), ".."))
    fn = relpath(fn, start=startdir).replace(os.path.sep, "/")

    if fn.startswith("kikuchipy/"):
        m = re.match(r"^.*dev0\+([a-f0-9]+)$", kikuchipy.__version__)
        pre_link = "https://github.com/pyxem/kikuchipy/blob/"
        if m:
            return pre_link + "%s/%s%s" % (m.group(1), fn, linespec)
        elif "dev" in kikuchipy.__version__:
            return pre_link + "develop/%s%s" % (fn, linespec)
        else:
            return pre_link + "v%s/%s%s" % (kikuchipy.__version__, fn, linespec)
    else:
        return None
