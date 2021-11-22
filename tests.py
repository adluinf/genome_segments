# write tests here:

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_segment(self):
        self.assertTrue(0,1)

    def test_function(self):
        self.assertTrue(0,1)


    def test_overlap(self):
        self.assertTrue(0,1)

    def test_correlation(self):
        self.assertTrue(0,1)

    def test_mean_function_over_segments(self):
        self.assertTrue(0,1)

if __name__ == '__main__':
    unittest.main()
