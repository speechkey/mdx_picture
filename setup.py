#!/usr/bin/env python

from setuptools import setup

setup(
    name='mdx_picture',
    version='1.0',
    author='Artem Grebenkin',
    author_email='speechkey@gmail.com',
    description='Python-Markdown extension supports the <picture> tag.',
    url='http://www.artemgrebenkin.com/',
    py_modules=['mdx_picture'],
    install_requires=['Markdown>=2.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
