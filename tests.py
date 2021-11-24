# write tests here:

import unittest

from segment_data import SegmentData
from function_data import FunctionData

from main import average, overlap, mean_function, correlation

class TestGenomeMethods(unittest.TestCase):

    #def test_upper(self):
    #    self.assertEqual('foo'.upper(), 'FOO')

    def test_load_segment(self):
        example_segment_string="""1	2
	    3	6"""
        example_segment_data=SegmentData(example_segment_string, use_string=True)
        #example_segment_data.load_string(example_segment_string)
        # Check that at least one segment is loaded.
        self.assertTrue(len(example_segment_data.data) > 1)
        # Check that we have two segments.
        self.assertEqual(len(example_segment_data.data),2)
        # Check that the regions within one SEGMENT file do not overlap.
        self.assertFalse(example_segment_data.has_overlaps())
        # Check that the SEGMENT file is in sorted order.
        self.assertTrue(example_segment_data.is_sorted())

    def test_load_function(self):
        # A FUNCTION file thus must have 10 million lines:
        #  Load a dummy function file and count its lines
        example_function_string="""10.0
11.0
12.0
13.0
14.0
15.0
16.0"""
        example_function_data=FunctionData(example_function_string,
                                           use_string=True)
        #example_function_data.load_string(example_function_string)    
        #self.assertEqual(0,10**6)
        self.assertEqual(len(example_function_data.data),7)

    def test_overlap(self):
        segments_string_1=""" 1 2
                            3 6"""
        segments_string_2="""  0 1
                            1 5"""
        segments_1=SegmentData(segments_string_1, use_string=True)
        segments_2=SegmentData(segments_string_2, use_string=True)

        estimated_overlap=overlap(segments_1.data, segments_2.data)
        self.assertEqual(estimated_overlap,3)

    def test_correlation(self):
        function_string_1="""10.0
11.0
12.0
13.0
14.0
15.0
16.0"""
        function_string_2="""10.5
11.5
12.0
13.0
13.5
15.0
14.0"""
        functions_1=FunctionData(function_string_1, use_string=True)
        functions_2=FunctionData(function_string_2, use_string=True)
        estimated_correlation=correlation(functions_1.data,
                                          functions_2.data)
        #self.assertEqual(estimated_correlation,0.9452853)
        self.assertAlmostEqual(estimated_correlation,0.9452853,places=7)

    def test_mean_function_over_segments(self):
        segments_string_1=""" 1 2
                            3 6"""
        segments_1=SegmentData(segments_string_1, use_string=True)
        function_string_2="""10.5
11.5
12.0
13.0
13.5
15.0
14.0"""
        functions_2=FunctionData(function_string_2, use_string=True)
        estimated_mean_function=mean_function(segments_1.data, functions_2.data)
        self.assertAlmostEqual(estimated_mean_function,13.5,places=1)

    def test_average(self):
        values=range(15,19)
        self.assertAlmostEqual(average(values),16.5,places=1)
        #print(values)
        #print(average(values),("?=16.5"))

if __name__ == '__main__':
    unittest.main()
