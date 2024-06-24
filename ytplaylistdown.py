from pytube import Playlist

playlist_url= input("Enter the Url of the playlist: ")

p = Playlist(playlist_url)

for video in p.videos:
    prefix = 0
    yd = video.streams.filter(adaptive=True)
    yd.download(output_path='D:\Study\FOP\Projects\Youtube downloader\Playlists', filename_prefix=str(prefix)+" ")
    prefix+=1
