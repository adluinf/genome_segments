# write class for function
from numpy import loadtxt, fromstring

class FunctionData:

    def load_file(self,file_path):
        self.data=loadtxt(file_path)

    def load_string(self, input_string):
        #self.data=fromstring(input_string)
        data=[]
        for line in input_string.split('\n'):
            data.append(float(line))
        self.data=data
