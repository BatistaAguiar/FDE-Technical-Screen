import unittest
from src.sorter import sort


class TestSorter(unittest.TestCase):
    def test_standard_small_and_light_returns_STANDARD(self):
        """Small, light packages should be STANDARD."""
        self.assertEqual(sort(10, 10, 10, 1), "STANDARD")

    def test_bulky_by_volume_exact_threshold_returns_SPECIAL(self):
        """Volume exactly 1,000,000 cm^3 is bulky -> SPECIAL."""
        self.assertEqual(sort(100, 100, 100, 1), "SPECIAL")

    def test_bulky_by_dimension(self):
        self.assertEqual(sort(150, 10, 10, 1), "SPECIAL")
        self.assertEqual(sort(10, 150, 10, 1), "SPECIAL")
        self.assertEqual(sort(10, 10, 150, 1), "SPECIAL")

    def test_heavy(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")
        self.assertEqual(sort(10, 10, 10, 100), "SPECIAL")

    def test_rejected_when_both_bulky_and_heavy(self):
        """Packages that are both bulky and heavy must be REJECTED."""
        self.assertEqual(sort(150, 100, 100, 20), "REJECTED")
        self.assertEqual(sort(1000, 1000, 1000, 20), "REJECTED")

    def test_validation_errors_for_non_positive_and_non_numeric_inputs(self):
        """Negative or zero inputs raise ValueError; non-numeric raise TypeError."""
        with self.assertRaises(ValueError):
            sort(-1, 10, 10, 1)
        with self.assertRaises(ValueError):
            sort(0, 10, 10, 1)
        with self.assertRaises(TypeError):
            sort('a', 10, 10, 1)


if __name__ == '__main__':
    unittest.main()
