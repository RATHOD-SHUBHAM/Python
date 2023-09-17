'''
    This module provides a portable way of using operating system dependent functionality.
    os: https://docs.python.org/3/library/os.html#os.mkdir
'''

import os

# Todo: List out all the module
module_lst = dir(os)
# print(module_lst)

# Todo: Retrun all the environment variable
path_to_dir = os.environ
# print(path_to_dir)

# get specific environment variable
path_to_env = os.environ.get('HOME')
# print(path_to_env)

# Todo: Current dir
cur_dir = os.getcwd() # the current folder we are present in
print(cur_dir)

# Todo: Change dir
# os.chdir('/Users/shubhamrathod/PycharmProjects')
# print(os.getcwd())

# os.chdir('/Users/shubhamrathod/PycharmProjects/basicFoundation')
# print(os.getcwd())

# Todo: List Dir
lst_dir = os.listdir() # we can pass a path as well
# print(lst_dir)

# Todo: Create new folder
# os.mkdir('dummy') # single folder
# os.makedirs('dummy-2/dummy-1/dummy') # Multi level directories

# Todo: Remove Dirs
# os.rmdir('dummy') # single folder
# os.removedirs('dummy-2/dummy-1/dummy') # Multi level directories

# Todo: Rename
# os.rename('dummy', 'test') # rename files and folders

# Todo: Get the status of file or a file discriptor
f_stat = os.stat('python_OS.py')
# print(f_stat)

# To get the date in human redable format
from datetime import datetime
mod_time = os.stat('python_OS.py').st_mode
date_mod_time = datetime.fromtimestamp(mod_time)
# print(date_mod_time)

# Todo: Traverse directory tree.
'''
    Generate the file names in a directory tree by walking the tree either top-down or bottom-up. 
    For each directory in the tree rooted at directory top (including top itself), 
    It yields a 3-tuple (dirpath, dirnames, filenames).
    
    Default: TopDown walk
'''

# for dirpath, dirnames, filenames in os.walk('/Users/shubhamrathod/PycharmProjects/basicFoundation'):
#     print("dirpath: ",dirpath)
#     print("dirnames: ", dirnames)
#     print("filenames: ", filenames)



