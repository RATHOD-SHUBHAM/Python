'''
    This module implements some useful functions on pathnames.
    os.path: https://docs.python.org/3/library/os.path.html#module-os.path
'''

import os

# Todo: Absolute path
abs_path = os.path.abspath('test')
print(abs_path)

# Todo: Basename
'''
    Grab file name of any path we are working.
    It need not be a real path
'''
base_name = os.path.basename('/test/temp.txt')
print(base_name)

# Todo: Base directoy
base_dir = os.path.dirname('/test/temp.txt')
print(base_dir)

# Todo: Spilt the path in files and folder
split_dir = os.path.split('/test/temp.txt')
# print(split_dir)

# Todo: Check if path exist
'''
    True: Path exist,
    False: Path doesnt exist. 
'''
path_exist = os.path.exists('/test/temp.txt')
# print(path_exist)

# Todo: Join Path
path_join = '/Users/shubhamrathod/PycharmProjects/basicFoundation/test'
new_path = os.path.join(path_join, 'test.txt')
# print(new_path)

# Todo: Split the extension
extension = os.path.splitext('/test/temp.txt')
# print(extension)

# Todo: Check if this is a file
file_path = os.path.isfile('/test/temp.txt')
print(file_path)