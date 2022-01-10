import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'async-riot-api',
    version = '0.0.27',
    author = 'Andrea Princic',
    author_email = 'princic.1837592@studenti.uniroma1.it',
    description = 'Async wrapper for the Riot Games API for League of Legends',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Princic-1837592/async-riot-api',
    packages = ['async_riot_api'],
    python_requires = '>=3.7',
    install_requires = [
        'aiohttp',
        'requests',
        'fuzzywuzzy',
        'python-Levenshtein'
    ]
)
