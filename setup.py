#!/usr/bin/env python
# fmt: off
from setuptools import setup, find_packages  # type: ignore

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
    url="https://github.com/evansmwendwa/python_socialite",
    version="0.1.0",
    zip_safe=False,
)
# fmt: on
