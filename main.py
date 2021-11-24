from os.path import join
from program_data import ProgramData

""" Documentation

    This is the main file to run the program.

"""
class WrongFileTypeException(Exception):
    pass

def read_filename(default_file_name='testfile_a.s'):
    """Docstring for read_filename.
    Read input filname from command line and check if it is supported.
    Raise exception if the filename is unsupported.

    :returns: a filename
    """
    file_name=default_file_name
    try:
        file_name=input("#  Supported file extesions are: .s and .f\n")
        print('  file_name',file_name)
        file_type=ProgramData.find_file_type(file_name)
        print('  file_type',file_type)
        if file_type in ['FUNCTION','SEGMENT']:
            print("# The file type is:")
            print("   "+ file_type )
        else:
            raise WrongFileTypeException('WrongFileType')
    except KeyError or WrongFileTypeException:
        print("The file extension you provided is not supported.")
        print(">> Using default file instead.")
        print('')
        file_name=default_file_name
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

    print("#  Please select file_1, default: 1: testfile_a.s")
    file_1=read_filename(default_file_name='testfile_a.s')

    print("#  Please select file_2, default: 2: testfile_a.f")
    file_2=read_filename(default_file_name='testfile_a.f')

    file_path_1=join(data_folder , file_1 )
    file_path_2=join(data_folder , file_2 )
    data_object=ProgramData(file_path_1,file_path_2)

    print("#  - Loading data ... please wait ...")
    print('       File 1:',file_path_1)
    print('       File 2:',file_path_2)
    data_object.load_data_files()

    print("#  - Analysing data ... please wait ...")
    result_name, result=data_object.analyse_data_files()

    print("# The following quantity has been computed:", result_name)
    print("# The result is:")
    print(result)
    print("# Done.")

if __name__ == "__main__":
    main()
