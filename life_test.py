import unittest as ut
from life import *

class LifeTestCase(ut.TestCase):
    def testNeighbours(self):
        """Test live neighbour calculation"""
        test_zeros = np.zeros((3,3))
        test_ones = np.ones((3,3))

        self.assertEqual(count_live(test_zeros, (1, 1)), 0)
        self.assertEqual(count_live(test_ones, (1, 1)), 8)

    def testUfunc(self):
        test_ones = np.ones((3,3))
        actual = count_grid(test_ones)
        expected = np.array([
            [3,5,3],
            [5,8,5],
            [3,5,3]
            ])
        self.assertTrue(np.array_equal(actual, expected))

    def testBlinker(self):
        """Test a blinker pattern"""
        start = np.array([
            [0,1,0],
            [0,1,0],
            [0,1,0]
            ])

        end = np.array([
            [0,0,0],
            [1,1,1],
            [0,0,0]
            ])

        self.assertTrue(np.array_equal(iterate(start), end))

if __name__ == '__main__':
    ut.main()
