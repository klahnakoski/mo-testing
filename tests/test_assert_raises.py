from dataclasses import dataclass

from mo_logs import Log
from mo_times import Date

from mo_testing.fuzzytestcase import FuzzyTestCase, add_error_reporting, assertAlmostEqual



class NullOp:
    pass

NULL = NullOp()


@add_error_reporting
class Tests(FuzzyTestCase):

    def test_raises_w_nothing(self):
        with self.assertRaises():
            raise Exception("problem")

    def test_raises_w_string(self):
        with self.assertRaises("example1"):
            Log.error("example1")

    def test_not_raises(self):
        with self.assertRaises(Exception):
            with self.assertRaises("example2"):
                Log.error("example1")  # DOES NOT MATCH EXPECTED

    def test_raises_w_array1(self):
        with self.assertRaises(["example1", "example2"]):
            Log.error("example1")

    def test_raises_w_array2(self):
        with self.assertRaises(["example1", "example2"]):
            Log.error("example2")


    def test_raises_when_different1(self):
        with self.assertRaises(Exception):
            assertAlmostEqual(1, 0.1, 6)

    def test_raises_when_different2(self):
        with self.assertRaises(Exception):
            assertAlmostEqual(1.000001, 1.000002, 6)

    def test_raises_when_different3(self):
        with self.assertRaises(Exception):
            assertAlmostEqual(1.000001, 1.0000016, 6)

    def test_raises_when_different4(self):
        with self.assertRaises(Exception):
            assertAlmostEqual(1.000001, 1.0000015, digits=6)

    def test_ok_when_same1(self):
        assertAlmostEqual(1.000001, 1.0000011, digits=6)

    def test_ok_when_same2(self):
        assertAlmostEqual(1.000002, 1.0000025, digits=6)

    # tests for number of significant digits (places)
    def test_raises_when_different_places1(self):
        with self.assertRaises(Exception):
            assertAlmostEqual(1.0001, 1.0002, places=5)

    def test_raises_when_different_places2(self):
        with self.assertRaises(Exception):
            assertAlmostEqual(1.0001, 1.00016, places=5)

    def test_raises_when_different_places3(self):
        with self.assertRaises(Exception):
            assertAlmostEqual(100.01, 100.016, places=5)

    def test_raises_when_different_places4(self):
        with self.assertRaises(Exception):
            assertAlmostEqual(0.0010001, 0.00100016, places=5)

    def test_ok_when_same_places1(self):
        assertAlmostEqual(1.0001, 1.00015, places=5)

    def test_ok_when_same_places2(self):
        assertAlmostEqual(100.01, 100.015, places=5)

    def test_ok_when_same_places3(self):
        assertAlmostEqual(0.0010001, 0.00100015, places=5)

    def test_ok_when_same_places4(self):
        assertAlmostEqual(0.0010001, 0.00100016, places=4)

    def test_report_property_name(self):
        with self.assertRaises("asdfasdf="):
            assertAlmostEqual({}, {"asdfasdf":0})

    def test_raises_when_not_missing2(self):
        with self.assertRaises(Exception):
            assertAlmostEqual(0, [])

    def test_raises_when_not_missing3(self):
        with self.assertRaises(Exception):
            assertAlmostEqual(False, [])

    def test_ok_when_missing1(self):
        assertAlmostEqual(None, [])

    def test_ok_when_missing2(self):
        assertAlmostEqual("", [])

    def test_ok_when_missing3(self):
        assertAlmostEqual([], [])

    def test_ok_when_missing4(self):
        assertAlmostEqual([], [])

    def test_ok_when_matching1(self):
        @dataclass
        class Temp:
            a: int
            b: float

        assertAlmostEqual(Temp(1, 3.14), {"a":1, "b": 3.14})

    def test_ok_when_matching2(self):
        assertAlmostEqual([{"a":1, "b":3.14}], {"a":1, "b": 3.14})

    def test_ok_when_matching3(self):
        assertAlmostEqual({"a":1, "b":3.14}, [{"a":1, "b": 3.14}])

    def test_ok_when_matching4(self):
        assertAlmostEqual("test", ["test"])

    def test_ok_when_matching5(self):
        assertAlmostEqual(["test"], "test")

    def test_raises_when_not_matching1(self):
        @dataclass
        class Temp:
            a: int
            b: float

        with self.assertRaises(Exception):
            assertAlmostEqual(Temp(1, 5.14), {"a":1, "b": 3.14})

    def test_raises_when_not_matching2(self):
        @dataclass
        class Temp:
            a: int

        with self.assertRaises("asdfasdf="):
            assertAlmostEqual(Temp(1), {"a":1, "asdfasdf": 3.14})

    def test_raise_when_not_matching3(self):
        with self.assertRaises(Exception):
            assertAlmostEqual([{"a":1, "b":3.14}, {}], {"a":1, "b": 3.14})

    def test_raise_when_not_matching4(self):
        with self.assertRaises(Exception):
            assertAlmostEqual({"a":1, "b":3.14}, [{"a":1, "b": 3.14}, {}])

    def test_ok_when_ordered(self):
        assertAlmostEqual([1, 2, 3], [1,2,3])

    def test_ok_when_unordered(self):
        assertAlmostEqual([1, 2, 3], {3, 2, 1})

    def test_raises_when_bad_length(self):
        with self.assertRaises(Exception):
            assertAlmostEqual([1, 2, 3], {2, 1})

    def test_raise_when_not_matching5(self):
        with self.assertRaises(Exception):
            assertAlmostEqual([1, 2, 3], {2, 1, 4})

    def test_raises_when_not_raises(self):
        with self.assertRaises(Exception):
            with self.assertRaises(Exception):
                pass

    def test_raises_when_not_missing4(self):
        with self.assertRaises(Exception):
            assertAlmostEqual({"a":0}, {"a": NULL})

    def test_ok_when_missing5(self):
        assertAlmostEqual({}, {"a": NULL})

    def test_ok_when_date_equal1(self):
        assertAlmostEqual("2024-04-19", Date("2024-04-19").datetime)

    def test_ok_when_date_equal2(self):
        assertAlmostEqual(Date("2024-04-19"), "2024-04-19")

    def test_ok_when_equal1(self):
        assertAlmostEqual(5, "5")

    def test_ok_when_equal2(self):
        assertAlmostEqual("5", 5)

    def test_ok_when_equal3(self):
        assertAlmostEqual(5, 5.01, delta=0.1)

    def test_raises_when_bad_call(self):
        with self.assertRaises(Exception):
            assertAlmostEqual(5, 5.1, places=0, delta=0.1)

    def test_raise_when_not_equal1(self):
        with self.assertRaises(Exception):
            assertAlmostEqual(6, "test")

    def test_raise_when_not_equal2(self):
        with self.assertRaises(Exception):
            assertAlmostEqual(5.0, 5.1, digits=2)
