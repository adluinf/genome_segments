# write class for function
from numpy import loadtxt, fromstring

class FunctionData:

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

    def load_file(self,file_path):
        self.data=loadtxt(file_path)

    def load_string(self, input_string):
        #self.data=fromstring(input_string)
        data=[]
        for line in input_string.split('\n'):
            data.append(float(line))
        self.data=data
