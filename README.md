# More Testing

`FuzzyTestCase` extends the `unittest.TestCase` to provide deep, yet fuzzy, structural comparisons; intended for use in test cases dealing with JSON.


## Details

The primary method is the `assertEqual` method with the following parameters:

* `test_value` - the value, or structure being tested
* `expected` - the expected value or structure.  In the case of a number, the accuracy is controlled by the following parameters.  In the case of a structure, only the not-null parameters of `expected` are tested for existence.
* `msg` - Detailed error message if there is no match
* `digits` - number of decimal places of accuracy required to consider two values equal
* `places` - number of significant digits used to compare values for accuracy
* `delta` - maximum difference between values for them to be equal

This method `assertEqual` is recursive; it does a deep comparison; it can not handle cycles in the data structure.


