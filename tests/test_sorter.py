import math
import unittest
from src.sorter import sort

class TestSorter(unittest.TestCase):

    def test_standard_small_and_light_returns_STANDARD(self):
        self.assertEqual(sort(10, 10, 10, 1), "STANDARD")

    def test_bulky_by_volume_exact_threshold_returns_SPECIAL(self):
        self.assertEqual(sort(100, 100, 100, 1), "SPECIAL")

    def test_bulky_by_dimension_all_axes(self):
        for dims in [(150,10,10), (10,150,10), (10,10,150)]:
            with self.subTest(dims=dims):
                self.assertEqual(sort(*dims, 1), "SPECIAL")

    def test_heavy_threshold_and_above(self):
        for m in [20, 100]:
            with self.subTest(m=m):
                self.assertEqual(sort(10, 10, 10, m), "SPECIAL")

    def test_rejected_when_both_bulky_and_heavy(self):
        for dims in [(150,100,100), (1000,1000,1000)]:
            with self.subTest(dims=dims):
                self.assertEqual(sort(*dims, 20), "REJECTED")

    def test_near_threshold_volume(self):
        self.assertEqual(sort(100, 100, 99.9999, 1), "STANDARD")
        self.assertEqual(sort(100, 100, 100.0001, 1), "SPECIAL")

    def test_near_threshold_dimension(self):
        self.assertEqual(sort(149.9999, 10, 10, 1), "STANDARD")
        self.assertEqual(sort(150.0, 10, 10, 1), "SPECIAL")

    def test_near_threshold_mass(self):
        self.assertEqual(sort(10, 10, 10, 19.9999), "STANDARD")
        self.assertEqual(sort(10, 10, 10, 20.0), "SPECIAL")

    def test_dimension_permutation_invariance(self):
        base = (50, 80, 251)
        expected = sort(*base, 1)
        for dims in [(base[0], base[2], base[1]), (base[1], base[0], base[2]), (base[2], base[1], base[0])]:
            with self.subTest(dims=dims):
                self.assertEqual(sort(*dims, 1), expected)

    def test_monotonicity_non_decreasing(self):
        self.assertIn(sort(10, 10, 10, 1), ["STANDARD"])
        self.assertIn(sort(10, 10, 10, 25), ["SPECIAL", "REJECTED"])

        self.assertIn(sort(10, 10, 10, 1), ["STANDARD"])
        self.assertIn(sort(160, 10, 10, 1), ["SPECIAL", "REJECTED"])

    def test_validation_zero_and_negative_each_field(self):
        bads = [
            (0, 10, 10, 1), (10, 0, 10, 1), (10, 10, 0, 1), (10, 10, 10, 0),
            (-1,10,10,1), (10,-1,10,1), (10,10,-1,1), (10,10,10,-1)
        ]
        for args in bads:
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    sort(*args)

    def test_validation_non_numeric_each_field(self):
        bads = [
            ("a",10,10,1), (10,"a",10,1), (10,10,"a",1), (10,10,10,"a")
        ]
        for args in bads:
            with self.subTest(args=args):
                with self.assertRaises(TypeError):
                    sort(*args)

    def test_validation_bool_nan_inf_policy(self):
        for args in [
            (True, 10, 10, 1),
            (10, 10, 10, math.nan),
            (10, 10, 10, math.inf)
        ]:
            with self.subTest(args=args):
                with self.assertRaises((TypeError, ValueError)):
                    sort(*args)

if __name__ == "__main__":
    unittest.main()
