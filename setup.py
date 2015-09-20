#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name=u'Cotolengo Doações',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description=u'Cotolengo Doações',
    # GETTING-STARTED: set author name (your name):
    author='Francisco Zanfranceschi',
    # GETTING-STARTED: set author email (your email):
    author_email='sistemas@cotolengosp.org.br',
    # GETTING-STARTED: set author url (your url):
    url='http://www.python.org/sigs/distutils-sig/',
    # GETTING-STARTED: define required django version:
    install_requires=[
         'Django==1.8.4'
		,'Pillow==2.9.0'
		,'argparse==1.2.1'
		,'django-admin-bootstrapped==2.5.5'
		,'requests==2.7.0'
		,'six==1.9.0'
		,'wsgiref==0.1.2'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
