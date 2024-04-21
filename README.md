# More Testing


[![PyPI Latest Release](https://img.shields.io/pypi/v/mo-testing.svg)](https://pypi.org/project/mo-testing/)
[![Build Status](https://github.com/klahnakoski/mo-testing/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/klahnakoski/mo-testing/actions/workflows/build.yml)
[![Coverage Status](https://coveralls.io/repos/github/klahnakoski/mo-testing/badge.svg?branch=dev)](https://coveralls.io/github/klahnakoski/mo-testing?branch=dev)
[![Downloads](https://pepy.tech/badge/mo-testing/month)](https://pepy.tech/project/mo-testing)


`FuzzyTestCase` extends the `unittest.TestCase` to provide deep, yet fuzzy, structural comparisons; intended for use in test cases dealing with JSON.


## Details

The primary method is the `assertAlmostEqual` method with the following arguments:

* `test_value` - the value, or structure being tested
* `expected` - the expected value or structure.  In the case of a number, the accuracy is controlled by the following parameters.  In the case of a structure, only the not-null parameters of `expected` are tested for existence.
* `msg` - Detailed error message if there is no match

Keyword arguments:
* `digits` - number of decimal places of accuracy required to consider two values equal
* `places` - number of significant digits used to compare values for accuracy
* `delta` - maximum difference between values for them to be equal

This method `assertEqual` is recursive; it does a deep comparison; it can not handle cycles in the data structure.

## Major Changes

### Version 8

* `digits`, `places`, and `delta` must be specified as keyword arguments
