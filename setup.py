"""
Constant Contact Python SDK for v2 API.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

from constantcontact import __version__

# Get the long description from the relevant file
try:
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'readme.md'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = 'Description can be found at: https://github.com/magellantoo/ctct-python-sdk'

setup(
    name='constantcontact',
    # Version found in /constantcontact/baseservice.py
    version=__version__,
    description='A Python SDK for the Constant Contact v2 API',
    long_description=long_description,
    url='http://developer.constantcontact.com/libraries/libraries.html',
    author='Constant Contact Inc.',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],

    keywords='constantcontact sdk',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    #package_dir={'python-sdk': 'python-sdk'},

    install_requires=['requests'],
)
