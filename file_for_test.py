import unittest

class OurTestCase(unittest.TestCase):


    def setUp(self):
        pass

    def test_method(self):
        self.assertEqual(7,6)


if __name__=='__main__':

    test1 = unittest.TestLoader().loadTestsFromTestCase(OurTestCase)#OurTestCase(test_method)
    result = unittest.TestResult()
    test1.run(result)

    print (result)

