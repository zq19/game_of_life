import unittest
from core_code import live_or_dead
import copy

test_l = [[0 for i in range(3)] for i in range(3)]
test_0 = copy.deepcopy(test_l)
test_0[1][1] = 1
test_1 = copy.deepcopy(test_0)
test_1[0][2] = 1
test_2 = copy.deepcopy(test_1)
test_2[2][0] = 1
test_3 = copy.deepcopy(test_2)
test_3[0][0] = 1
test_5 = copy.deepcopy(test_3)
test_5[1][1] = 0
test_4 = copy.deepcopy(test_3)
test_4[0][1] = 1
print(test_4)

class TestSurroundcell(unittest.TestCase):

    def test_surround0(self):
        self.assertEqual(0, live_or_dead(test_0)[1][1])

    def test_surround1(self):
        self.assertEqual(0, live_or_dead(test_1)[1][1])

    def test_surround2(self):
        self.assertEqual(1, live_or_dead(test_2)[1][1])

    def test_surround3(self):
        self.assertEqual(1, live_or_dead(test_3)[1][1])

    def test_surround4(self):

        self.assertEqual(0, live_or_dead(test_4)[1][1])

    def test_surround5(self):
        self.assertEqual(1, live_or_dead(test_5)[1][1])

    def left_top(self):
        self.assertEqual(0, live_or_dead(test_4)[0][0])


if __name__ == '__main__':
    unittest.main()