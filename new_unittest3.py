import unittest

def func():
    return 100



class CreateBookTests(unittest.TestCase):
    def setUp(self):
        pass




    def test_one(self):
        #TODO something
        self.assertEqual(func(), 100)

    def test_two(self):
        self.assertEqual(10**2,10)


if __name__=='__main__':

    test_suite = unittest.TestLoader().loadTestsFromTestCase(CreateBookTests)

    result = unittest.TestResult()
    test_suite.run(result)
    print (result)
