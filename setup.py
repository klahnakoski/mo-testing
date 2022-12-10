# encoding: utf-8
# THIS FILE IS AUTOGENERATED!
from __future__ import unicode_literals
from setuptools import setup
setup(
    author='Kyle Lahnakoski',
    author_email='kyle@lahnakoski.com',
    classifiers=["Development Status :: 4 - Beta","Topic :: Software Development :: Libraries","Topic :: Software Development :: Libraries :: Python Modules","License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)","Programming Language :: Python :: 3.7","Programming Language :: Python :: 3.8","Programming Language :: Python :: 3.9"],
    description='More Testing! Extends the `unittest.TestCase` to provide deep, yet fuzzy, structural comparisons',
    extras_require={"tests":[]},
    include_package_data=True,
    install_requires=["mo-collections==5.292.22344","mo-dots==9.279.22339","mo-future==6.265.22338","mo-logs==7.279.22339","mo-math==7.280.22341","mo-threads==5.292.22344"],
    license='MPL 2.0',
    long_description='# More Testing\n\n`FuzzyTestCase` extends the `unittest.TestCase` to provide deep, yet fuzzy, structural comparisons; intended for use in test cases dealing with JSON.\n\n\n## Details\n\nThe primary method is the `assertEqual` method with the following parameters:\n\n* `test_value` - the value, or structure being tested\n* `expected` - the expected value or structure.  In the case of a number, the accuracy is controlled by the following parameters.  In the case of a structure, only the not-null parameters of `expected` are tested for existence.\n* `msg` - Detailed error message if there is no match\n* `digits` - number of decimal places of accuracy required to consider two values equal\n* `places` - number of significant digits used to compare values for accuracy\n* `delta` - maximum difference between values for them to be equal\n\nThis method `assertEqual` is recursive; it does a deep comparison; it can not handle cycles in the data structure.\n\n\n',
    long_description_content_type='text/markdown',
    name='mo-testing',
    packages=["mo_testing"],
    url='https://github.com/klahnakoski/mo-testing',
    version='5.295.22344'
)