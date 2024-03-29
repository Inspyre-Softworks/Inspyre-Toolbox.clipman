#!/usr/bin/env python

"""The setup script."""

#  Copyright (c) 2021. setup.py is a part of the ''inspyre-toolbox.clipman' project by Inspyre Softworks D.O. and is licensed under the MIT License. Feel free to copy, share, distribute any code from this project  as you please. If you do; please share where you got it.

import codecs
import os

from setuptools import find_packages, setup

about = {}

with codecs.open(os.path.join("inspyre_toolbox", "clipman", "__init__.py")) as f :
    exec(f.read(), about)

with codecs.open('README.rst') as readme_file:
    readme = readme_file.read()

with codecs.open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
        'inspyre-toolbox>=1.0a7',
        'inspy-logger>=2.1a14',
        'PySimpleGUI',
        'PySimpleGUIQt',
        'clipboard'
        ]

extras = {
        "docs":  [
                "sphinx", "furo",
                ],
        "tests": [
                
                ],
        }

setup(
        name=about["__title__"],
        author=about["__author__"],
        author_email=about["__email__"],
        version=about["__version__"],
        description=about["__summary__"],
        long_description=readme + '\n\n' + history,
        long_description_content_type="text/x-rst",
        license=about["__license__"],
        url=about["__url__"],
        keywords=["inspyre_toolbox.clipman", ],
        python_requires='>=3.6',
        classifiers=[
                'Development Status :: 2 - Pre-Alpha',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: MIT License',
                'Natural Language :: English',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7',
                'Programming Language :: Python :: 3.8',
                'Environment :: GPU',
                'Environment :: MacOS X',
                'Environment :: Plugins',
                'Environment :: X11 Applications',
                'Intended Audience :: End Users/Desktop',
                'Intended Audience :: System Administrators',
                'License :: Freeware',
                'Operating System :: Microsoft :: Windows :: Windows 10',
                'Programming Language :: Python :: 3 :: Only',
                'Topic :: System',
                'Topic :: Utilities'
                
                ],
        entry_points={
                'console_scripts' : [
                        'inspyre_toolbox.clipman=inspyre_toolbox.clipman.cli:main',
                        ],
                },
        install_requires=requirements,
        extras_require=extras,
        include_package_data=True,
        packages=find_packages(include=['inspyre_toolbox.clipman', 'inspyre_toolbox.clipman.*']),
        zip_safe=False,
        )
