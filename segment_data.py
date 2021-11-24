# Implementation
# The program should be written in Python, with limited use of external libraries. The goal is to write quick code that still tries to follow good programming practices as regards object-oriented programming, system architecture, unit testing, and such. This is to be regarded as pilot code designed in such a way to support the possible expansion with other file types and analyses in a simple manner. The code does not need to be fully polished, but please comment places where improvements may be made.

"""

    write tests
    document

    write code

    run ...
"""

#import numpy as np
from numpy import loadtxt, fromstring

class SegmentData:

    def load_file(self,file_name):
        """
            This method loads a segment from a file.
        """
        #print('TODO')
        self.data=loadtxt(file_path)


    def load_string(self, input_string):
        """
            This method loads a segment from a string.
        """
        data=[]
        for line in input_string.split('\n'):
            data.append([int(i) for i in line.split()])
        self.data=data

    def is_sorted(self):
        """
            Return true if the segment data is sorted in ascending order, false otherwise.
        """
        return all(self.data[i][0] <= self.data[i+1][0] for i in range(len(self.data)-1) )

    def has_overlaps(self):
        """
            Return true if the segment data contains overlaps, false otherwise.
        """
        return any(self.data[i][1] > self.data[i+1][0] for i in range(len(self.data)-1) )

