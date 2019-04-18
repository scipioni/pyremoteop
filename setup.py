# -*- coding:utf-8 -*-

from setuptools import find_packages, setup

requires = [
]

setup(name='pyremoteop',
      version='0.1',
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Stefano Scipioni',
      author_email='stefano.scipioni@csgalileo.org',
      url='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points={
          'console_scripts': [
              'pyremoteop_run = pyremoteop.main:main',
          ],
      },
      )
