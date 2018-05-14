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
    from HtmlTestRunner import HTMLTestRunner

    unittest.main(testRunner=HTMLTestRunner(output=r'Desktop'))

   #unittest.main()
#     test1 = CreateBookTests('test_one')
#     test2 = CreateBookTests('test_two')
#     result = test1.run()
#     print (result)
#     result = test2.run()
#     print (result)
#
#
#     test_suite = unittest.TestSuite([test1,test2])
#     result = unittest.TestResult()
#     test_suite.run(result)
#     print(result)
#
