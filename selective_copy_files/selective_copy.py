#! python
""" Copy a specific file extension in the tree directory """

import os, shutil, sys

path = ''
pathDestiny = '' 
extension = ''
my_files = []

# Red the terminal
helpMenssage = 'Write the folder to search files, the folder destination, and the file extensions \
(example: main.py "user/myfolder" "user/imgaesFolder" ".jpg")'
if len(sys.argv) == 4:  
    path = sys.argv[1]
    pathDestiny = sys.argv[2]
    extension = sys.argv[3]

else: 
    print (helpMenssage)
    sys.exit()

# Function with the parameters: file_extension, origin, destination
def find_files (extention, origin): 
    """Find all files with specific extension"""
    files_found = []

    # Check correct extension
    if not extention.startswith('.'): 
        extention = '.' + extention #Add a dot

    absPath = os.path.abspath(origin)

    # walk inside the origin tree
    for folder_name, subfolder_name, file_names in os.walk(absPath): 
        
        # if the file has the correct extension, save complite path
        for file in file_names: 
            if file.endswith(extention):
                files_found.append(os.path.join(folder_name,file))
        
    return files_found

def copy_files (files, destiny):
    """ Loop inside a list of files and copy to destiny"""

    absPath = os.path.abspath(destiny)

    for file in files: 
        print ('Copying %s to %s ...' % (file, absPath))
        shutil.copy(file, absPath)

        

# Print menssage for the copy action

my_files = find_files(extension, path)
copy_files (my_files, pathDestiny)