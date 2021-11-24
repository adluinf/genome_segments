"""Docstring for Computations.
    This file contains the following functions:

    - correlation
    - overlap
    - mean_function
    - average
"""

def correlation(function_data_1, function_data_2):
    """Docstring for correlation.

    Compute the sample Pearson correlation coefficient of the two lists of
    function data.

    :function_data_1: list or array of floats.
    :function_data_2: list or array of floats.

    :returns: sample_pearson_correlation (float), Pearson correlation of the input lists.

    """
    from numpy import corrcoef
    sample_pearson_correlation=corrcoef(function_data_1.data,function_data_2.data)[0,1]
    return sample_pearson_correlation

def overlap(segments_1, segments_2):
    """TODO: CHECK THIS ! Docstring for overlap.
    Compute the length of the overlap between the segments in segments_1 and
    segments_2.
    Note: performance can be improved by breaking the inner for-loop if s1[0]>=s2[1].

    :segments_1: list of pairs of integers describing segments [beginning,end].
    :segments_2: list of pairs of integers describing segments [beginning,end].

    :returns: length of the overlap as integer.

    """
    overlap_length=0
    for s1 in segments_1.data:
        for s2 in segments_2.data:
            diff_12 = min(s1[1],s2[1])-max(s1[0],s2[0])
            if diff_12>0:
                overlap_length+=diff_12
    return overlap_length

def mean_function(segment_data, function_data):
    """Docstring for mean_function.
    Compute the mean of the numbers in function_data over the positions covered
    by segment_data.

    :segment_data: list of pairs of integers describing segments [beginning,end].
    :function_data: list or array of floats.

    :returns: float, the mean of function_data over segment_data.

    """
    function_values_in_segments=[]
    for s in segment_data.data:
        #print(' the slice is: s[0]:s[1] :', s[0],s[1])
        function_values_in_segments.extend(function_data.data[s[0]:s[1]])
    return average(function_values_in_segments)

def average(a_list):
    """Docstring for average.
    Compute the average of a list of numerical values.

    :a_list: list of numerical values (integers or floats).

    :returns: average of a_list (float).

    """
    return sum(a_list)/float(len(a_list))
