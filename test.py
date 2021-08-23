# libs
import pytube as pt
import os
import moviepy.editor as mp

# Download for Youtube
url = str(input('URL: '))
stream = pt.YouTube(url = url).streams.get_audio_only()
stream.download()
title = str(stream.title)

# Converter of mp4 to mp3
clip = mp.AudioFileClip(title + '.mp4')
clip.write_audiofile(f'musics/'+ title + '.mp3')

# Remove mp4
os.remove(title + '.mp4')
