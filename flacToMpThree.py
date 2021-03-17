from tkinter.filedialog import askopenfilenames
from pydub.utils import mediainfo
from pydub import AudioSegment
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


file = getFile()

sound = AudioSegment.from_file(file)
sound.export(file,
             format="mp3",
             bitrate="320k",
             tags=mediainfo(file)["TAG"])


# with open('image.jpg', 'wb') as img:
#    img.write(artwork) # write artwork to new image


from mutagen.flac import FLAC, Picture


var = FLAC(file)
pics = var.pictures
# print(pics)

for p in pics:
    if p.type == 3:  # Front cover
        print("\nFound front cover") 
        with open("cover.jpg", "wb") as f:
            f.write(p.data)
