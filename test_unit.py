import unittest
from distance import distance

class DistanceTests(unittest.TestCase):
    def test_zero(self):
        res = distance(0,0,0,0)
        self.assertEqual(res, 0)



#if__name__=='__main__':
 #   unittest.main()

