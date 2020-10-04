#pip install you-get
#get url of youtube video and with video player

#for URL 
import re 

#for sub process
import subprocess

#put urls from youtube and other social media platform 50+ 
url="https://www.youtube.com/watch?v=rpZxFbtr7j0"

#put cmd on in subprocess
proc = subprocess.Popen([f"you-get -u --itag=22 {url}"], stdout=subprocess.PIPE, shell=True)

#communicate to the URL
(out, err) = proc.communicate()

#Decode the url
out=out.decode("utf-8")

#display the downloading  video url  
print(out);