from pytube import YouTube
link = "https://www.youtube.com/watch?v=rGGLINL6xfc"
YouTube_1 = YouTube(link)
print(YouTube_1.title)#it will give title of this video
print(YouTube_1.thumbnail_url)#it will give the first poster of the video
videos = YouTube_1.streams.all()#it is gives all format 
#only audio
#videos =  YouTube_1.streams.filter(only_audio=True)
vid = list(enumerate(videos))#it will gives index number of all streming
for i in vid:
    print(i)

print()
print()

stre = int(input("enter :- "))
videos[stre].download()
print("successefuly")



#for download full playlist
from pytube import Playlist
py = Playlist("url")
print(f"Downloading : {py.title}")
for video in py.videos:
    video.streams.first().download()