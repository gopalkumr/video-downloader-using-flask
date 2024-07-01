This python file is used as a backend for downloading video from different websites. It uses youtube-dl library to download video. It is used in the main.py file.

To run this you'll need to install 

```
Flask
pytube
```
Now run the 

```
app.py
```
Then Go the server. 
for eg. http://127.0.0.1:5000/

eg for flask api
``` 
curl -X POST http://127.0.0.1:5000/download -H "Content-Type: application/json" -d '{"url":"https://www.youtube.com/watch?v=dQw4w9WgXcQ"}' -o cool-video.mp4
```
Video will be downloaded in the current directory.