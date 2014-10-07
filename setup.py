#! /usr/bin/env python
#-*- coding : utf-8 -*-
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

__author__ = u'TROUVERIE Joachim'
__version__ = u'0.1'
__appname__ = u'FliKISS'

from setuptools import setup, find_packages

requirements = []
for line in open('REQUIREMENTS.txt', 'r'):
    requirements.append(line)
    
setup(
    name = __appname__,
    version = __version__,
    packages = find_packages(),
    author = __author__,
    author_email = 'joachim.trouverie@joacodepel.tk',
    description = 'Wiki engine based on Markdown flat files powered by Flask',
    long_description = open('README.md').read(),
    install_requires = requirements,
    include_package_data=True,
    url='http://projets.joacodepel.tk/flikiss/',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Framework :: Flask", 
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
    ],
    entry_points = {
        'console_scripts': [
            'flikiss = flikiss.launcher:run',
        ],
    },
)
