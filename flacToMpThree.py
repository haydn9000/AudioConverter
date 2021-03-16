from tkinter.filedialog import askopenfilenames
from pydub import AudioSegment
from mutagen.mp3 import MP3
import tkinter as tk
import mutagen


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

sound = AudioSegment.from_file("2 Chainz - We Own It (Fast & Furious).flac", format="flac")
soundMetadata = mutagen.File("2 Chainz - We Own It (Fast & Furious).flac")

sound.export("2 Chainz - We Own It (Fast & Furious).mp3", format="mp3", bitrate="320k")
sound = MP3("2 Chainz - We Own It (Fast & Furious).mp3")
sound = soundMetadata