"""
    This module is for converting FLAC to MP3 with all the metadata available
"""

from tkinter.filedialog import askopenfilenames
from pydub.utils import mediainfo
from pydub import AudioSegment
from datetime import datetime
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


def convertFlacToMpthree(file, format="mp3", bitrate="320k", outFileLocation=""):
    if not outFileLocation:
        outPath = os.path.join(os.path.dirname(file) + "/converted")
    else:
        outPath = outFileLocation

    # Create folder is it doesn't already exist.
    if not os.path.exists(outPath):
        os.makedirs(outPath)

    audioName = os.path.splitext(os.path.basename(file))[0]
    fileName = os.path.join(outPath + f"/{audioName}." + format)
    # print("-----", fileName)

    # Convert audio
    sound = AudioSegment.from_file(file)

    sound.export(fileName,
                format=format,
                bitrate=bitrate,
                tags=mediainfo(file)["TAG"])

    # Add album cover
    audiofile = eyed3.load(fileName)
    if (audiofile.tag == None):
        audiofile.initTag()

    var = FLAC(file)
    pics = var.pictures

    for p in pics:
        if p.type == 3:  # Front cover
            # print("\nFound front cover")
            # print(p.data)
            audiofile.tag.images.set(3, p.data, "image/jpeg")

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


def addCoverArtToMpthree(fileName):
    # Add album cover
    audiofile = eyed3.load(fileName)
    if (audiofile.tag == None):
        audiofile.initTag()
    
    """
    You have to set the ID3 version to "V2.3", otherwise the photo won't show up for the file icon.
    https://stackoverflow.com/questions/38510694/how-to-add-album-art-to-mp3-file-using-python-3#39316853
    """
    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)



if __name__ == "__main__":
    files = getFile()

    for file in files:
        if file.lower().endswith(".flac"):
            try:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                print(f"{now} - Processing: {file}")
                convertFlacToMpthree(file)
            except Exception as e:
                # print(e)
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{now} - ERROR, skipped: {file}")
                continue