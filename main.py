from os.path import join
from program_data import ProgramData

""" Documentation

    This is the main file to run the program.

"""

"""
class ProgramData:

    """Docstring for ProgramData. """

    def __init__(self, file_path_1, file_path_2):
        self.file_1=file_path_1
        #self.file_1_type=self.file_1.split('.')[-1]
        self.file_2=file_path_2
        #self.file_2_type=self.file_2.split('.')[-1]

    def find_file_type(cls, arg1):
        """Docstring for find_file_type.

        :arg1: a file name string.
        :returns: file type

        """
        dict_file_types={ 'f': 'FUNCTION', 's': 'SEGMENT' }
        file_ext=arg1.split('.')[-1]
        return dict_file_types[file_ext]

    def load_data_files(self):
        """Docstring for load_data_files.
        Check which data files have been provided
        and load the files into memory.
        """
        self.data_1=self.load_a_file(self.file_1)
        self.data_2=self.load_a_file(self.file_2)

    def analyse_data_files(self):
        """Docstring for analyse_data_files.
        Check which data files have been provided
        and compute the relevant analysis.

        """
        #self.data_1=self.load_a_file(self.file_1)
        #self.data_2=self.load_a_file(self.file_2)
        print('TODO')
        pass

    def load_a_file(self, file_path):
        """TODO: Docstring for load_a_file.

        :arg1: TODO
        :returns: TODO

        """
        file_1_ext=file_1.split('.')[-1]
        dict_file_types={ 'f': 'FUNCTION', 's': 'SEGMENT' }
        print("# You gave files of the following types:")
        print("  1: "+  dict_file_types[file_1_ext] )

        return load_file( data_folder , file_1 )
    #data_1=loaddd_file( os.path.join(data_folder , file_1 )
    #data_1= join(data_folder , file_1 )
    #print(data_1)

def correlation(function_data_1, function_data_2):
    """Docstring for correlation.

    Compute the sample Pearson correlation coefficient of the two lists of
    function data.

    :function_data_1: list or array of floats.
    :function_data_2: list or array of floats.

    :returns: sample_pearson_correlation (float), Pearson correlation of the input lists.

    """
    from numpy import corrcoef
    #print(type(function_data_1),type(function_data_2))
    sample_pearson_correlation=corrcoef(function_data_1,function_data_2)[0,1]
    return sample_pearson_correlation

def overlap(segments_1, segments_2):
    """TODO: CHECK THIS ! Docstring for overlap.
    Compute the length of the overlap between the segments in segments_1 and
    segments_2.

    :segments_1: list of pairs of integers describing segments [beginning,end].
    :segments_2: list of pairs of integers describing segments [beginning,end].

    :returns: length of the overlap as integer.

    """
    overlap_length=0
    for s1 in segments_1:
        for s2 in segments_2:
            diff_12 = min(s1[1],s2[1])-max(s1[0],s2[0])
            if diff_12>0:
                overlap_length+=diff_12
            #if s1[0]<s2[1]:
            #    if s1[1]>=s2[0]:
            #        overlap_length+=
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
    for s in segment_data:
        function_values_in_segments.extend(function_data[s[0]:s[1]])
    return average(function_values_in_segments)

def average(a_list):
    """Docstring for average.
    Compute the average of a list of numerical values.

    :a_list: list of numerical values (integers or floats).

    :returns: average of a_list (float).

    """
    return sum(a_list)/float(len(a_list))
"""

def read_filename():
    """TODO: Docstring for read_filename.
    Read input filname from command line and check if it is supported.
    Raise exception if the filename is unsupported.

    :returns: a filename
    """
    file_name=''
    try:
        current_input=input("#  Supported file extesions are: .s and .f")
        if len(current_input)>0 :
            file_1=current_input
        else:
            file_1='testfile_a.s'

        file_1_type=ProgramData.find_file_type[file_1]
        if file_1_type in ['FUNCTION','SEGMENT']:
            print("# The file type is:")
            print("   "+ file_1_type )
        else:
            raise WrongFileTypeException('WrongFileType')
    except:
        print("The file extension you provided is not supported.\n Please try again.")
    return file_name

def main():
    """Docstring for main.
    This is the main method run.
    It reads a file path and two file names from the standard input.
    Then it loads the data and computes the quantity relevant given the file
    extensions.
    """
    print("#  Genome Segments Main Function: ")
    print("# ")

    current_input=input("#  Please type the path to the data, default: ../data/ \n")
    if len(current_input)>0 :
        data_folder=current_input
    else:
        data_folder='../data/'

    current_input=input("#  Please select file_1, default: 1: testfile_a.s\n")
    try:
        file_1=read_filename()
    except:
        file_1='testfile_a.s'

    current_input=input("#  Please select file_2, default: 2: testfile_a.f\n")
    try:
        file_2=read_filename()
    #if len(current_input)>0 :
    #    file_2=current_input
    except:
        file_2='testfile_a.f'

    print("# You gave a file of the following types:")
    print("  1: "+  ProgramData.find_file_type[file_1] )

    file_path_1=join(data_folder , file_1 )
    file_path_2=join(data_folder , file_2 )
    data_object=ProgramData(file_path_1,file_path_2)

    print("#  - Loading data ... please wait ...")
    data_object.load_data_files()

    print("#  - Analysing data ... please wait ...")
    result=data_object.analyse_data_files()

    print("# The following quantity will be computed:")

    print("# The result is:")
    print(result)

if __name__ == "__main__":
    main()
