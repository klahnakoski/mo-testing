# encoding: utf-8
# THIS FILE IS AUTOGENERATED!
from setuptools import setup
setup(
    author='Kyle Lahnakoski',
    author_email='kyle@lahnakoski.com',
    classifiers=["Development Status :: 4 - Beta","Topic :: Software Development :: Libraries","Topic :: Software Development :: Libraries :: Python Modules","License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)","Programming Language :: Python :: 3.8","Programming Language :: Python :: 3.9","Programming Language :: Python :: 3.10","Programming Language :: Python :: 3.11","Programming Language :: Python :: 3.12"],
    description='More Testing! Extends the `unittest.TestCase` to provide deep, yet fuzzy, structural comparisons',
    extras_require={"tests":["mo_times","mo_logs"]},
    include_package_data=True,
    install_requires=["mo-dots==10.632.24139","mo-future==7.584.24095","mo-logs==8.632.24139","mo-math==7.632.24139","mo-times==5.632.24139"],
    license='MPL 2.0',
    long_description='# More Testing\n\n\n[![PyPI Latest Release](https://img.shields.io/pypi/v/mo-testing.svg)](https://pypi.org/project/mo-testing/)\n[![Build Status](https://github.com/klahnakoski/mo-testing/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/klahnakoski/mo-testing/actions/workflows/build.yml)\n[![Coverage Status](https://coveralls.io/repos/github/klahnakoski/mo-testing/badge.svg?branch=dev)](https://coveralls.io/github/klahnakoski/mo-testing?branch=dev)\n[![Downloads](https://pepy.tech/badge/mo-testing/month)](https://pepy.tech/project/mo-testing)\n\n\n`FuzzyTestCase` extends the `unittest.TestCase` to provide deep, yet fuzzy, structural comparisons; intended for use in test cases dealing with JSON.\n\n\n## Details\n\nThe primary method is the `assertAlmostEqual` method with the following arguments:\n\n* `test_value` - the value, or structure being tested\n* `expected` - the expected value or structure.  In the case of a number, the accuracy is controlled by the following parameters.  In the case of a structure, only the not-null parameters of `expected` are tested for existence.\n* `msg` - Detailed error message if there is no match\n\nKeyword arguments:\n* `digits` - number of decimal places of accuracy required to consider two values equal\n* `places` - number of significant digits used to compare values for accuracy\n* `delta` - maximum difference between values for them to be equal\n\nThis method `assertEqual` is recursive; it does a deep comparison; it can not handle cycles in the data structure.\n\n## Major Changes\n\n### Version 8\n\n* `digits`, `places`, and `delta` must be specified as keyword arguments\n',
    long_description_content_type='text/markdown',
    name='mo-testing',
    packages=["mo_testing"],
    url='https://github.com/klahnakoski/mo-testing',
    version='8.633.24139'
)