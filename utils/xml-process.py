import os 

def xml_process(folder):
    '''
    xml_process:
        Delete the first line of the .xml files in the folder to make it have the right format for training.
    Input:
        folder - path of the xml (annotation) file folder
    '''
    all_files = os.listdir(folder)
    for file in all_files:
        if file.endswith(".xml"):
            file_name = f'{folder}/{file}'
            with open(file_name, 'r') as fp:
                lines = fp.readlines()
            with open(file_name, 'w') as fp:
                for i in range(1, len(lines)):
                    fp.write(lines[i])
