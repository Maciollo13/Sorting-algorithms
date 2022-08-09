import unittest
import algorithms

arr = [2, 80, 9, 25, 14, 6, 79, 1, 2]
answer = [1, 2, 2, 6, 9, 14, 25, 79, 80]

class Test(unittest.TestCase):
    def insertion_sort_test(self):
        self.assertEqual(algorithms.insertion_sort(arr),answer)


if __name__ == "__main__":
    unittest.main()