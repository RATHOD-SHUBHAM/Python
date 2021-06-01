"""
Sound Device: https://python-sounddevice.readthedocs.io/en/0.4.1/usage.html
Sound File: https://pypi.org/project/SoundFile/
Tkinter:
https://www.tutorialspoint.com/python/tk_grid.htm
http://effbot.org/tkinterbook/label.htm




Sound Device:
This Python module provides bindings for the PortAudio library
and a few convenience functions to play and record NumPy arrays containing audio signals

fs (in the most cases this will be 44100 or 48000 frames per second)






Sound File:
SoundFile can read and write sound files.
File reading/writing is supported through libsndfile, which is a free, cross-platform, open-source (LGPL) library
for reading and writing many different sampled sound file formats that runs on
many platforms including Windows, OS X, and Unix.




Steps:
1] Import the library.
2] Set frequency and duration.
3] Record voice using rec().
4] Store in a file using soundfile.write().

"""


# dont need to install anything extra for tkinter.
from tkinter import *
import soundfile as sf
import sounddevice as sd


def voice_recording():
    fs = 48000
    duration = 10.5
    # change channel according to your system 1 or 2
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    return sf.write('audio_recording.flac', myrecording, fs)


def main():
    master = Tk()
    Label(master, text=" Voice Recorder: ").grid(row=0, sticky=W, rowspan=5)

    b = Button(master, text="Start", command=voice_recording)
    b.grid(row=0, column=5, columnspan=2, rowspan=2, padx=5, pady=5)

    # mainloop is necessary
    mainloop()


if __name__ == '__main__':
    main()
