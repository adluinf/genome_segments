class ProgramData:

    """Docstring for ProgramData.
        A class to store information about data files,
        to load data according to file types,
        and to call the appropriate analysis methods.
    """

    def __init__(self, file_path_1, file_path_2):
        self.file_1=file_path_1
        self.file_2=file_path_2

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

        :returns:
            :computation_name: string naming the computation,
            :result: value resulting of the computation.

        """
        file_1_type=self.find_file_type(self.file_1)
        file_2_type=self.find_file_type(self.file_2)

        if file_1_type == 'SEGMENT':
            if file_2_type == 'SEGMENT':
                computation_name='overlap'
                from computations import overlap
                result=overlap(self.data_1,self.data_2)

            elif file_2_type == 'FUNCTION':
                computation_name='mean function'
                from computations import mean_function
                result=mean_function(self.data_1,self.data_2)

        if file_1_type == 'FUNCTION':
            if file_2_type == 'FUNCTION':
                computation_name='Pearon correlation'
                from computations import correlation
                result=overlap(self.data_1,self.data_2)

            elif file_2_type == 'SEGMENT':
                computation_name='mean function'
                from computations import mean_function
                result=mean_function(self.data_2,self.data_1)

        return computation_name, result

    def load_a_file(self, file_path):
        """Docstring for load_a_file.

        :file_path: path to the file to load.
        :returns: data loaded from the file.

        """
        file_type=self.find_file_type(file_path)
        if file_type == 'SEGMENT':
            from segment_data import SegmentData
            data=SegmentData(file_path)
        elif file_type == 'FUNCTION':
            from function_data import FunctionData
            data=FunctionData(file_path)
        return data

