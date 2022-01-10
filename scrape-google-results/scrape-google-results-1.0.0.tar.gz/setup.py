import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
VERSION = '1.0.0'
PACKAGE_NAME = 'scrape-google-results'
AUTHOR = 'DataKund'
AUTHOR_EMAIL = 'datakund@gmail.com'
KEYWORDS='google python bot_studio automation search result scraper title description'
LICENSE = 'Apache License 2.0'
DESCRIPTION = 'A python library to scrape google search result'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'requests','bot-studio'
]
setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(),
      keywords = KEYWORDS
      )