from numpy import loadtxt, fromstring

class SegmentData:

    def __init__(self, input_string, use_string=False):
        """Docstring for __init__.

        :input_string: string data: either a path to a file, or data to be
        loaded.
        :use_string: default False, if True the input_string is to be parsed as data.

        """
        if use_string:
            self.load_string(input_string)
        else:
            self.load_file(input_string)

    def load_file(self,file_name):
        """
            This method loads a segment from a file.
        """
        self.data=loadtxt(file_name, dtype='int')


    def load_string(self, input_string):
        """
            This method loads a segment from a string.

            :input_string: string containing data, one segment per line,
            values separated by tabs.
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

