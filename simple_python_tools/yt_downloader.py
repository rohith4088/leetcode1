from sys import argv
from pytube import YouTube
link = argv[1]
yt = YouTube(link)
print("Title: ", yt.title)
print("Number of views: ",yt.views)
yd = yt.streams.get_highest_resolution()
yd.download("/Users/rohithr/Desktop/leetcode")
