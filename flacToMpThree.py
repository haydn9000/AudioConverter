from pydub import AudioSegment

sound = AudioSegment.from_file("/input/file")
sound.export("/output/file", format="mp3", bitrate="320k")