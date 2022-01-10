import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="authc",
    version="0.0.4",  # Latest version .
    author="R2FsCg",
    author_email="r2fscg@gmail.com",
    description="For authentication.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/private_repo/codefast",
    package_data={setuptools.find_packages()[0]: [
                      'bin/*',
                  ]},
    packages=setuptools.find_packages(),
    install_requires=['codefast'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
