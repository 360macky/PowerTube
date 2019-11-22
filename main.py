from pytube import YouTube
from pytube.cli import on_progress

print("-> 🐍 PowerTube 🔻 <-")
url = str(input("> YouTube video URL: "))

yt = YouTube(url, on_progress_callback=on_progress)
yt = yt.streams[0].download()

print("")
print("✅🎥 Video downloading successfully")
