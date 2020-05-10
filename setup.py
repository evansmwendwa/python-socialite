#!/usr/bin/env python
# fmt: off
import codecs
import os.path
from setuptools import setup, find_packages  # type: ignore


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Evans Mwendwa",
    author_email="evans@authenticvisualsmedia.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="Simple Python oAuth Login",
    install_requires=["requests"],
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_data={"python_socialite": ["py.typed"]},
    include_package_data=True,
    keywords="python_socialite",
    name="python_socialite",
    package_dir={"": "src"},
    packages=find_packages(
        include=["src/python_socialite", "src/python_socialite.*"]
    ),
    setup_requires=[],
    url="https://github.com/evansmwendwa/python-socialite",
    version=get_version("src/python_socialite/__init__.py"),
    zip_safe=False,
)
# fmt: on
