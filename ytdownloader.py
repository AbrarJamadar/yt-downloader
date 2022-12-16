from pytube import YouTube


def Download(link):
    yt_obj = YouTube(link)
    # yt_obj = yt_obj.streams.get_by_resolution("720p", "144p")
    yt_obj = yt_obj.streams.get_highest_resolution()
    try:
        yt_obj.download()
        print("Download completed!!")
    except Exception as e:
        print("Error!!!")
        print(e)


link = input("input the yt-link URL:")
Download(link)
