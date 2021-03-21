"""
    This module is for converting FLAC to MP3 with all the metadata available
"""

from tkinter.filedialog import askopenfilenames
from pydub.utils import mediainfo
from pydub import AudioSegment
from mutagen.flac import FLAC
import tkinter as tk
import eyed3
import os


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


def convertFlacToMpthree(file, outExtension=".mp3"):
    fileName = os.path.splitext(file)[0] + outExtension
    print(fileName)

    sound = AudioSegment.from_file(file)

    sound.export(fileName,
                format="mp3",
                bitrate="320k",
                tags=mediainfo(file)["TAG"])

    # Add album cover
    audiofile = eyed3.load(fileName)
    if (audiofile.tag == None):
        audiofile.initTag()

    audiofile.tag.images.set(3, open('cover.jpg','rb').read(), 'image/jpeg')

    """
    You have to set the ID3 version to "V2.3", otherwise the photo won't show up for the file icon.
    https://stackoverflow.com/questions/38510694/how-to-add-album-art-to-mp3-file-using-python-3#39316853
    """
    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)


def getFlacAudioCoverArt(file):
    """ Get sound front cover """
    var = FLAC(file)
    pics = var.pictures
    # print(pics)

    for p in pics:
        if p.type == 3:  # Front cover
            print("\nFound front cover") 
            with open("cover.jpg", "wb") as f:
                f.write(p.data)



if __name__ == "__main__":
    pass