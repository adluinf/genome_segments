from os.path import join
from program_data import ProgramData

""" Documentation

    This is the main file to run the program.

"""

def read_filename(default_file_name='testfile_a.s'):
    """Docstring for read_filename.
    Read input filname from command line and check if it is supported.
    Raise exception if the filename is unsupported.

    :returns: a filename
    """
    file_name=default_file_name
    try:
        file_name=input("#  Supported file extesions are: .s and .f\n")
        #if len(current_input)>0 :
        #    file_1=current_input

        file_name_type=ProgramData.find_file_type[file_name]
        print('file_1_type',file_type)
        if file_type in ['FUNCTION','SEGMENT']:
            print("# The file type is:")
            print("   "+ file_type )
        else:
            raise WrongFileTypeException('WrongFileType')
    except:
        print("The file extension you provided is not supported.")
        print("Using default file instead.")
        #print("Please try again.")
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
    #print("#  Supported file extesions are: .s and .f")
    #try:
    file_1=read_filename(default_file_name='testfile_a.s')
    #except:
    #    file_1='testfile_a.s'

    print("#  Please select file_2, default: 2: testfile_a.f")
    #print("#  Supported file extesions are: .s and .f")
    #try:
    file_2=read_filename(default_file_name='testfile_a.f')
    #if len(current_input)>0 :
    #    file_2=current_input
    #except:
    #    file_2='testfile_a.f'

    #print("# You gave a file of the following types:")
    #print("  1: "+  ProgramData.find_file_type[file_1] )

    file_path_1=join(data_folder , file_1 )
    file_path_2=join(data_folder , file_2 )
    data_object=ProgramData(file_path_1,file_path_2)

    print("#  - Loading data ... please wait ...")
    print('       File 1:',file_path_1)
    print('       File 2:',file_path_2)
    #print(file_path_1,file_path_2)
    data_object.load_data_files()

    print("#  - Analysing data ... please wait ...")
    result=data_object.analyse_data_files()

    print("# The following quantity will be computed:")

    print("# The result is:")
    print(result)

if __name__ == "__main__":
    main()
