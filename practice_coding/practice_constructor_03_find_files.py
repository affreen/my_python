import os
"""
   Practice Python Constructors.
   Display the path of a file. Exe-03
"""

class My_Files(object):
    def __init__(self, filename, search_path):
        self.filename = filename
        self.search_path = search_path
        result = []
        for root, dir, files in os.walk(search_path):
            if filename in files:
                result.append(os.path.join(root, filename))

        for one_item in result:
            print("Folder found for the given file:", one_item.strip('\\')) # format the folder name
        return None

my_file = My_Files("terraform.exe", "C:\\")
