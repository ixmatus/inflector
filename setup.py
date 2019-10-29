import os
from io import open
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

README = open(os.path.join(here, 'README.md'), 'r', encoding='utf-8').read()
VERSION = open(os.path.join(here, 'VERSION'), 'r', encoding='utf-8').read()

setup(name='Inflector',
      version=VERSION.strip(),
      description='Inflector for Python',
      long_description=README,
      classifiers=["Intended Audience :: Developers",
                   "License :: OSI Approved :: Python Software Foundation License",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      author='Parnell Springmeyer',
      author_email="parnell@digitalmentat.com",
      url="https://github.com/ixmatus/inflector",
      keywords="inflector text language english",
      packages=["inflector"],
      package_dir={'inflector': 'inflector'},
      include_package_data=True,
      zip_safe=False,
      test_suite='tests'
      )

