# write tests here:

import unittest



class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_load_segment(self):
        # Check that at least one segment is loaded.
        # Check that the regions within one SEGMENT file are not allowed to overlap.
        # Check that the SEGMENT file is in sorted order.
        self.assertTrue(0)

    def test_load_function(self):
        # A FUNCTION file thus must have 10 million lines:
        #  Load a dummy function file and count its lines
        self.assertEqual(0,10**6)

    def test_overlap(self):
        estimated_overlap=0
        self.assertEqual(estimated_overlap,3)

    def test_correlation(self):
        estimated_correlation=0
        self.assertEqual(estimated_correlation,0.9452853)

    def test_mean_function_over_segments(self):
        mean_function=0
        self.assertEqual(mean_function,13.5)

if __name__ == '__main__':
    unittest.main()
