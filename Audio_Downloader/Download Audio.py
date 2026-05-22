import os
from pytubefix import YouTube
from moviepy.editor import AudioFileClip

youtube_url = "https://www.youtube.com/watch?v=9ujy-YtDgWQ"

yt = YouTube(youtube_url)

audio_stream = yt.streams.filter(only_audio=True).first()

temp_file = audio_stream.download(output_path="D:/mini tasks/Audio_Downloader")

audio_clip = AudioFileClip(temp_file)

mp3_file = os.path.join("D:/mini tasks/Audio_Downloader", "audio.mp3")

audio_clip.write_audiofile(mp3_file)

audio_clip.close()

os.remove(temp_file)

print("Audio extracted and saved as MP3 file to", mp3_file)