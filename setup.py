#/usr/bin/env python

import sys
from setuptools import setup


def main():
    setup(
        name='reindent',
        version='3.5',
        author="Tim Peters",
        author_email='nottimsemail@notadomain.foo',
        scripts=['reindent'],
        py_modules=['reindent'],
        maintainer="Ryan Ollos",
        maintainer_email="ryan.j.ollos@gmail.com",
        description='reindent script by Tim Peters',
        install_requires=['setuptools'],
        keywords=['reindent', 'pep8', 'syntax', 'lint', 'tab', 'space'],
        classifiers=[
            "Development Status :: 6 - Mature",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "License :: Public Domain",
            "Natural Language :: English",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Topic :: Software Development :: Quality Assurance",
        ],
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        platforms=['any'],
        license="Public Domain"
    )
    return 0


if __name__ == '__main__':
    sys.exit(main())
