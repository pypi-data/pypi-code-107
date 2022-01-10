from setuptools import setup, find_packages

VERSION = '2.1.4'
DESCRIPTION = 'Utility package'
LONG_DESCRIPTION = 'Utility package for upswing applications'

# Setting up
setup(
    name="upswingutil",
    version=VERSION,
    author="Harsh Mathur",
    author_email="hmathur@upswing.cloud",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'requests',
        'pydantic',
        'gcsfs',
        'cryptography',
        'fastapi',
        'firebase_admin',
        'pymongo',
        'loguru',
        'mongoengine',
        'amadeus',
        'python-holidayapi',
        'pycountry-convert',
        'google-cloud-secret-manager==2.0.0'
    ],
    keywords=['python', 'upswing'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
    ]
)
