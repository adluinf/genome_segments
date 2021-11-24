# Implementation
# The program should be written in Python, with limited use of external libraries. The goal is to write quick code that still tries to follow good programming practices as regards object-oriented programming, system architecture, unit testing, and such. This is to be regarded as pilot code designed in such a way to support the possible expansion with other file types and analyses in a simple manner. The code does not need to be fully polished, but please comment places where improvements may be made.

"""

    write tests
    document

    write code

    run ...
"""

#import numpy as np
from numpy import loadtxt

class Segment:

    def load(self,file_name):
    """
        This method loads a segment.
    """
    #print('TODO')
    self.data=loadtxt(file_path)

