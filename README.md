# Selective_copy
Copy a specific file extension in the tree directory

# Install

## How to use
``` bash
# Import pakage
from selective_copy_files import selective_copy

#  Save local folders
from_folder = "c:\\user\\my_files"
to_folder = "c:\\user\\backup_of_my_files"
extention = "png"

# backup folder 
selective_copy.Copy(from_folder, to_folder, extention)

```
