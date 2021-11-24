# write class for function
from numpy import loadtxt

class FunctionData:

    def load(self,file_path):
        self.data=loadtxt(file_path)

