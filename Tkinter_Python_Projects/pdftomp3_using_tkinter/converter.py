from tkinter import Tk
from tkinter.filedialog import askopenfilename

import pdftotext

from gtts import gTTS

import os

# todo : Allow user to pick a file
'''
iconify() Turns the window into an icon (without destroying it). To redraw the window, use deiconify. Under Windows, the window will show up in the taskbar. When the window has been iconified, the state method returns “iconic”.

withdraw() Removes the window from the screen (without destroying it). To redraw the window, use deiconify. When the window has been withdrawn, the state method returns “withdrawn”.

Source: Tkinter -- Toplevel Window Methods

As far as use-cases go, you would normally use iconify() in situations where you want the user to be able to easily gain access to a window that was "minimized" (via iconify()) for whatever reason. For example, say a user clicks a button that "minimizes" a window and opens up a new one. Using iconify() lets the user do whatever they need to do in the new window and then return to the previous one easily since it appears to them as an icon.

On the other hand, withdraw() is useful to "hide" windows. For example, I have developed some applications that automatically created multiple windows on start-up of the application. If I had used iconify() the user would be aware of all the windows that had been created because they'd see them as icons. Imagine the shock of a user seeing 10 windows by simply starting up an application! Therefore, I used withdraw() so that each window would appear (via deiconify()) only if the user triggered the right event.


'''

# https://stackoverflow.com/questions/22834150/difference-between-iconify-and-withdraw-in-python-tkinter/31992065#:~:text=withdraw()%20Removes%20the%20window,state%20method%20returns%20%E2%80%9Cwithdrawn%E2%80%9D.

Tk().withdraw()
# https://pythonspot.com/tk-file-dialogs/
filelocation = askopenfilename()


# todo 2 : Convert the file into a string
'''
https://pypi.org/project/pdftotext/
This also says how to install pdftotext on system
'''
with open(filelocation, "rb") as f:
    pdf = pdftotext.PDF(f)

# todo 3: convert the file into one string
# print(pdf)
string_to_text = ""
for text in pdf:
    string_to_text += text

# todo 4: output as mp3 file
'''
https://gtts.readthedocs.io/en/latest/module.html
'''
final_file = gTTS(text = string_to_text,lang='en')

output_file_name = os.path.splitext(filelocation)[0]+'.mp3'
final_file.save(output_file_name)



