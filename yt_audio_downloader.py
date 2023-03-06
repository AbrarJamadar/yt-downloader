# from pytube import YouTube
# import os
# yt = YouTube(str(input("Enter URL of youtube video: \n ")))
# video = yt.streams.filter(only_audio=True).first()
# print("Enter the destination address (leave blank to save in current directory)")
# destination = str(input(" ")) or '.'
# out_file = video.download(output_path=destination)
# base, ext = os.path.splitext(out_file)
# new_file = base + '.mp3'
# os.rename(out_file, new_file)
# print(yt.title + " has been successfully downloaded.")


from pytube import YouTube

# where to save.
# replce /home/balasundar/Downloads/ with the path where you want to store the dowload file
destination = "/yt"
# link of the video to be downloaded
# Replace with the Youtube video link you want to download.
video_link = "https://www.youtube.com/watch?v=Qs8JfVqx9WA"

try:
    video = YouTube(video_link)
    # filtering the audio. File extension can be mp4/webm
    # You can see all the available streams by print(video.streams)
    audio = video.streams.filter(only_audio=True, file_extension='mp4').first()
    audio.download()
    print('Download Completed!')

except:
    print("Error")  # to handle exception
