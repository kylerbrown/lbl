from __future__ import print_function
from setuptools import setup
from setuptools.command.test import test as TestCommand
import io
import os
import sys

import lbl

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='lbl',
    version=lbl.__version__,
    url='http://github.com/kylerbrown/lbl/',
    license='MIT License',
    author='Kyler Brown',
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    author_email='kylerjbrown@gmail.com',
    description='python tools for manipulating lbl files',
    long_description=long_description,
    py_modules = ['lbl'],
    platforms = 'any',
    test_suite='test_lbl',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)
