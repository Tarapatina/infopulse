import unittest

class TestStringMethod(unittest.TestCase):

    def _split_with_sep(self, s , sep):
        s.split(sep=sep)

    def test_wrong_split(self):
        self.assertRaises(TypeError,self._split_with_sep,'hello!',2)


    def test_split(self):
        s = 'hello'
        with self.assertRaises(TypeError):
            s.split(2)

if __name__=='__main__':

    from HtmlTestRunner import HTMLTestRunner
    unittest.main(testRunner = HTMLTestRunner(output = r'Desktop1'))
