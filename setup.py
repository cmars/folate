# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='folate',
    version='0.0.0',
    description='First Order Logic As The Engine',
    long_description=readme,
    author='Casey Marshall',
    author_email='me@cmars.tech',
    url='https://github.com/cmars/folate',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

