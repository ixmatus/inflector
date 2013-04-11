import sys
from setuptools import setup, find_packages

version = '2.0'

if not '2.5' <= sys.version:
    raise ImportError('Python version not supported')

tests_require = []

setup(
    name="Inflector",
    version=version,
    description="A port of ROR's inflector class",
    long_description="""\
        This is a fork of bermi's original `inflector class <https://github.com/bermi/Python-Inflector>`_ - I
        mostly wanted it up on PyPi and will be making some changes to it.
        It has a `mercurial repository
        <https://ixmatus@bitbucket.org/ixmatus/inflector>`_ that
        you can install from with ``easy_install inflector``
        """,
    classifiers=["Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    author="Parnell Springmeyer",
    author_email="ixmatus@gmail.com",
    url="http://bitbucket.org/ixmatus/inflector",
    license="BSD",
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    test_suite='tests',
)
