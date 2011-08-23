#!/usr/bin/env python

from setuptools import setup, find_packages

setup(version='0.1',
      description='Trend following library',
      author='Nate Reed',
      author_email='nate@natereed.com',
      packages=['trendfollowing'],
      install_requires=['numpy'],
      test_suite="trendfollowing.test",
)
