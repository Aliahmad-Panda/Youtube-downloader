from pytube import YouTube
from sys import argv

link = input("Enter the link: ")

yt= YouTube(link)

print("Title: ", yt.title)

yd = yt.streams.get_highest_resolution()

yd.download('E:\Study\Coding\FOP\Projects\Youtube downloader')