from pytube import YouTube

link = input("Please provide link to the file: ")
check = input("Press V for video and A for audio: ")

if check == "v":
    youtube_1 = YouTube(link)
    videos = youtube_1.streams.filter(progressive=True)
    vid = list(enumerate(videos))
    for i in vid:
      print(i)
    strm = int(input("What quality do you want?:"))
    videos[strm].download()
    print("Your video has been downloaded")

elif check == "a":
    youtube_2 = YouTube(link)
    audio = youtube_2.streams.filter(only_audio=True)
    aud = list(enumerate(audio))
    for i in audio:
      print(i)
    strm2 = int(input("Quality of audio: "))
    audio[strm2].download()
    print("Your audio has been downloaded")
