import unittest

class OurTestCase (unittest.TestCase):
    def test_method(self):
        self.assertEqual(4,4)
    def test_method2(self):
        self.assertEqual(4,7)


if __name__=='__main__':
    from HtmlTestRunner import HTMLTestRunner
    unittest.main(testRunner = HTMLTestRunner(output = r'Desktop'))


suite = unittest.TestLoader().loadTestsFromTestCase(OurTestCase)

result = unittest.TestResult()
suite.run(result)

print (result)
