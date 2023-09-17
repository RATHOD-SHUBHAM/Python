'''
    File Handling in Python
'''
import os

# Todo: Read file

## Small file
with open('text.txt' , 'r') as f:
    file_content = f.read()
    print(file_content)

## Large file
with open('text.txt', 'r') as f:
    data = f.readlines()

    for line in data:
        word = line.split()
        print(word)

## read file content in chunk
with open('text.txt', 'r') as f:
    size_to_read = 2 # no of character

    file_content = f.read(size_to_read)

    while len(file_content) > 0:
        print(file_content, end = "")
        file_content = f.read(size_to_read)


# Todo: Write to a file
'''
    Clear everything and rewrite the file.
    Create a new file if file doesnt exist.
'''
with open('text.txt', 'w') as f:
    f.write('Hello there')

with open('abc.txt','w') as f:
    f.write("New file")

# Todo: Append to a file
f = open('abc.txt', 'a')
f.write(" new line")
f.close()

# Todo: Copy file content of one to another
with open('text.txt', 'r') as rf:
    with open('abc.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# Todo: Copy Image
with open('demo.jpg', 'rb') as rf:
    with open('demo_copy.jpg', 'wb') as wf:
        size_to_read = 4096  # no of character

        file_content = rf.read(size_to_read)

        while len(file_content) > 0:
            wf.write(file_content)
            file_content = rf.read(size_to_read)

# Todo: Read, Write, Update, Delete

class Operation:

    def read_file(self, filename):
        self.filename = filename
        try:
            with open(self.filename, 'r') as f:
                file_content = f.read()
                print(file_content)
        except IOError:
            print("Error: Count not find the file: ", self.filename)

    def write_file(self, filename):
        self.filename = filename
        try:
            with open(self.filename, 'w') as f:
                f.write('Hello there')
        except IOError:
            print("Error: Count not create a new file ")

    def append_file(self, filename, text):
        self.filename = filename
        self.text = text
        try:
            with open(self.filename, 'a') as f:
                f.write(self.text)
        except IOError:
            print("Error: Count not append to the file :  ", self.filename)

    def rename_file(self, filename, newname):
        self.filename = filename
        self.newname = newname
        try:
            os.rename(self.filename, self.newname)
            print("File " + self.filename  + " renamed to " + self.newname + " successfully.")
        except IOError:
            print("Error: could not rename file " + filename)

    def delete_file(self, filename):
        self.filename = filename
        try:
            os.remove(self.filename)
            print(self.filename + "deleted successfully")
        except IOError:
            print("no such file found")

if __name__ == '__main__':
    obj = Operation()

    filename = "testFile.txt"
    obj.write_file(filename)
    obj.read_file(filename)
    obj.append_file(filename, "New line added")
    obj.read_file(filename)

    new_name = "renameTest.txt"
    obj.rename_file(filename, new_name)
    obj.read_file(new_name)

    obj.delete_file(new_name)




