import unittest
from main import sum_numbers, is_anagram, fibonacci_series, prime_factors, create_diamond, create_multiplication_square, create_number_triangle ,create_pascals_triangle, create_pyramid
class TestFunctions(unittest.TestCase):

    # ------------------ sum_numbers ------------------
    def test_sum_numbers(self):
        self.assertEqual(sum_numbers([2, -3, 5, -1]), 3)
        self.assertEqual(sum_numbers([-1, -2, -3]), -6)
        self.assertEqual(sum_numbers([0, 0, 0]), 0)
        self.assertEqual(sum_numbers([]), 0)
        self.assertEqual(sum_numbers([10, -5, -5]), 0)
    # ---------- is_anagram ----------
    def test_is_anagram_true(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("Dormitory", "dirty room"))
        self.assertTrue(is_anagram("The eyes", "They see"))

    def test_is_anagram_false(self):
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("python", "java"))

    def test_is_anagram_edge_cases(self):
        self.assertTrue(is_anagram("", ""))
        self.assertFalse(is_anagram("a", "b"))

    # ------------------ fibonacci_series ------------------
    def test_fibonacci_series_regular(self):
        self.assertEqual(fibonacci_series(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(fibonacci_series(5), [0, 1, 1, 2, 3])

    def test_fibonacci_series_edge(self):
        self.assertEqual(fibonacci_series(0), [])
        self.assertEqual(fibonacci_series(1), [0])
        self.assertEqual(fibonacci_series(2), [0, 1])

    # ------------------ prime_factors ------------------
    def test_prime_factors_regular(self):
        self.assertEqual(prime_factors(84), [2, 2, 3, 7])
        self.assertEqual(prime_factors(13), [13])
        self.assertEqual(prime_factors(60), [2, 2, 3, 5])

    def test_prime_factors_edge(self):
        self.assertEqual(prime_factors(1), [])
        self.assertEqual(prime_factors(2), [2])
        self.assertEqual(prime_factors(0), [])

    # ------------------ create_pyramid ------------------
    def test_create_pyramid(self):
        self.assertEqual(create_pyramid(3), ['  *  ', ' *** ', '*****'])
        self.assertEqual(create_pyramid(1), ['*'])
        self.assertEqual(create_pyramid(0), [])

    # ------------------ create_number_triangle ------------------
    def test_create_number_triangle(self):
        self.assertEqual(create_number_triangle(3), ['  1  ', ' 2 2 ', '3 3 3'])
        self.assertEqual(create_number_triangle(1), ['1'])
        self.assertEqual(create_number_triangle(0), [])

    # ------------------ create_multiplication_square ------------------
    def test_create_multiplication_square(self):
        self.assertEqual(create_multiplication_square(3), ['1 2 3', '2 4 6', '3 6 9'])
        self.assertEqual(create_multiplication_square(1), ['1'])
        self.assertEqual(create_multiplication_square(0), [])

    # ------------------ create_diamond ------------------
    def test_create_diamond(self):
        self.assertEqual(create_diamond(3), ['  *  ', ' *** ', '*****', ' *** ', '  *  '])
        self.assertEqual(create_diamond(1), ['*'])
        self.assertEqual(create_diamond(0), [])

    # ------------------ create_pascals_triangle ------------------
    def test_create_pascals_triangle(self):
        self.assertEqual(create_pascals_triangle(5), [
            '    1    ', 
            '   1 1   ', 
            '  1 2 1  ', 
            ' 1 3 3 1 ', 
            '1 4 6 4 1'
        ])
        self.assertEqual(create_pascals_triangle(1), ['1'])
        self.assertEqual(create_pascals_triangle(0), [])


if __name__ == "__main__":
    unittest.main()




