 
from flask_socketio import SocketIO, emit
from flask import *
import os
from pytube import YouTube

__author__ = 'Anagha Moosad'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)



file_size = 0

@app.route("/", methods=['GET', 'POST']) 
def index():
    if request.method == "POST":
        if request.form.get('download_video') == 'Download Video':
            yt_url=request.form["url"]
            result= Download(yt_url) 
        elif  request.form.get('download_audio') == 'Download Audio':
            yt_url=request.form["url"]
            result= DownloadAudio(yt_url) 
              
    return render_template("index.html")
  
def progress_function(stream, chunk, bytes_remaining):
    progress_perct=round((1 -bytes_remaining/stream.filesize)*100, 2)
    print(progress_perct, '% done...')  
    socketio.emit('test_response', {'data':int(progress_perct)})
    
   

    

#Grabs the file path for Download
def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    return download_path

def Download(link):
    print("Your video will be saved to: {}".format(file_path()))
    #Input 
 
    print(link)
    print ("Accessing YouTube URL...")

    # Searches for the video and sets up the callback to run the progress indicator. 
    try:
        video = YouTube(link, on_progress_callback=progress_function)
    except:
        print("ERROR. Check your:n  -connectionn  -url is a YouTube urlnnTry again.")
        redo = Download(link)

    #Get the first video type - usually the best quality.
    video_type = video.streams.filter(progressive = True, file_extension = "mp4").first()

    #Gets the title of the video
    title = video.title

    #Prepares the file for download
    print ("Fetching: {}...".format(title))
    global file_size
    file_size = video_type.filesize
    #Starts the download process
    video_type.download(file_path())

 
def DownloadAudio(link):
    
    print("Your audio will be saved to: {}".format(file_path()))
    #Input 
    print(link)
    print ("Accessing YouTube URL...")

    # Searches for the video and sets up the callback to run the progress indicator. 
    try:
        video = YouTube(link, on_progress_callback=progress_function)
    except:
        print("ERROR. Check your:n  -connectionn  -url is a YouTube urlnnTry again.")
        redo = DownloadAudio(link)

    #Get the first video type - usually the best quality.
    video_type = video.streams.filter(progressive = True, file_extension = "mp4").first()
    # extract only audio
    audio = video.streams.filter(only_audio=True).first()

    #Gets the title of the video
    title = video.title

    #Prepares the file for download
    print ("Fetching: {}...".format(title))
    print ("Downlaoding audio.....")
    global file_size
    file_size = audio.filesize
    #Starts the download process
    out_file =audio.download(file_path())
    
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

 
 

@socketio.on('connect')
def test_connect():
    # need visibility of the global thread object
    
    print('Client connected')

 

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)