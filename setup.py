import sys
from setuptools import setup, find_packages

if not '2.5' <= sys.version:
    raise ImportError('Python version not supported')

tests_require = []

with open("LICENSE", 'r') as f:
    LICENSE = f.read()

with open("README.md", 'r') as f:
    README = f.read()

setup(
    name="Inflector",
    version="2.0.2",
    description="A port of ROR's inflector class",
    long_description=README,
    classifiers=["Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    author="Parnell Springmeyer",
    author_email="parnell@ixmat.us",
    url="https://github.com/ixmatus/inflector",
    license=LICENSE,
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    test_suite='tests',
)
