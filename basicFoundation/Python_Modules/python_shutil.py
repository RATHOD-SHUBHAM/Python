'''
    The shutil module offers a number of high-level operations on files and collections of files.
    shutil: https://docs.python.org/3/library/shutil.html#shutil.copyfileobj
'''
import shutil

# Todo: Copy a file
# shutil.copy('python_shutil.py', 'test')

# Todo: Copy an entire directory
'''
    If dirs_exist_ok is false (the default) and dst already exists, a FileExistsError is raised. 
    If dirs_exist_ok is true, the copying operation will continue if it encounters existing directories, 
    and files within the dst tree will be overwritten by corresponding files from the src tree.


'''
# shutil.copytree('test', 'dummy', dirs_exist_ok=True)

# Todo: Remove an entire directory
# shutil.rmtree('dummy')

# Todo: Move a file o directory to another location
# shutil.move('test', 'dummy')

