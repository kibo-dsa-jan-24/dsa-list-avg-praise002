import unittest
from listavg import ListAverage

class TestListAverage(unittest.TestCase):
    def test(self):
        lavg = ListAverage([1, 2, 3])
        assert lavg.compute_avg() == 2.0
        
    def test_add(self):
        lavg = ListAverage([1, 3, 5, 7, 9, 11, 13])
        lavg.add(4)
        lavg.add(5)
        assert lavg.compute_avg_faster() == 6.4

    def test_compute_average_faster(self):
        lavg = ListAverage([1, 3, 5, 7, 9, 11, 13])
        assert lavg.compute_avg_faster() == 7.0

if __name__ == '__main__':
    unittest.main()