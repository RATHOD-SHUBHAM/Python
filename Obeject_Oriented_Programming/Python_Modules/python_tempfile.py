'''
    This module creates temporary files and directories
    tempfile: https://docs.python.org/3/library/tempfile.html#module-tempfile
    Temp file is deleted after program finish execution
'''

import tempfile

# Todo: Create a temp file
temp = tempfile.TemporaryFile()
print(temp.name)
temp.close()

# Todo: Read and write to temp file
'''
    After writing, you have to rewind the file handle using seek() in order to read the data back from it.
'''
temp = tempfile.TemporaryFile()

try:
    temp.write(b'Hello world!')
    temp.seek(0)
    print(temp.read())
finally:
    temp.close()

temp = tempfile.TemporaryFile()

try:
    temp.write((b'Hello World'))
    temp.seek(0)
    data = temp.read()
    print(data)
finally:
    temp.close()

# Todo: Temporary directory
with tempfile.TemporaryDirectory() as tmpdir:
    print("created dir: ", tmpdir)

    temp = tempfile.TemporaryFile()

    try:
        temp.write(b'Hello world!')
        temp.seek(0)
        print(temp.read())
    finally:
        temp.close()

 # Todo: Get temporary directory
'''
    Return the name of the directory used for temporary files. 
'''
print(tempfile.gettempdir())

# Todo: Nameed temporay file
temp = tempfile.NamedTemporaryFile()
print("name of the file is : ", temp.name)
temp.close

temp = tempfile.NamedTemporaryFile(prefix= "temp_file", suffix='dummy_file')
print("name of the file is : ", temp.name)
temp.close
