from mo_logs import Log

from mo_testing.fuzzytestcase import FuzzyTestCase, add_error_reporting, assertAlmostEqual


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
