from tkinter.filedialog import askopenfilenames
from pydub import AudioSegment
import tkinter as tk


def getFile():
    """
        Uses tkinter to open a file dialog box and allows user to selec file(s).
        @return File paths tuple of seslected items through tkinter GUI 
    """
    root = tk.Tk()
    files = askopenfilenames(parent=root, title="Select file(s)")
    root.quit()
    root.destroy()

    return(files)


# file = getFile()[0]
# print(file)

sound = AudioSegment.from_file("............", format="flac")
# sound.export("........mp3", format="mp3", bitrate="320k")