# YouTube Video and Audio Downloader

A YouTube video and audio downloader using Pytube, Flask and Docker.

 ---

![alt text](https://github.com/anaghamoosad/youtube_video_downloader/blob/main/yt_downloader.gif "Youtube downloader")

---

**Features**

 - Download youtube video as mp4 files
 - Convert and download as youtube video as mp3 files
 - Shows progress as file downloads
 - Currently saves file in Download folder
---
**To create docker image and run container, run the following commands**

1. Create docker image

   `docker image build -t youtube_video_downloader .`
   
2. Run docker container

	  `docker run -p 5000:5000 -d youtube_video_downloader `
	  
3. open browser and type the following url

	  `http://localhost:5000/`

---
**Additional features to be added**

 - Option to enter folder path for download
 - Option to disable buttons while downloading 
 - Show the details of files before downloading
