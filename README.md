# Get subtitles for YouTube videos
## By Abdel Moubine Missaoui

[![Abdel Moubine Missaoui](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilZws84M8hf_NVRzgm1gAPNjI90laEmpQmdbRbpF4xmqiSIEfvqmf_YdqWgyTyVUloM3-0GIT9vJxnE19bQg2woXmOsXBWh2KpsW6JcqXV_f_sEt4CEvpIwJNcXQzObvpXfsuy7gIdw9BrpzjP9VuaEwjrzCrKErmEiVhR-rllIKIcdAu1gzP3h9wu/w640-h245/TheA2M-Company.png)](https://www.linkedin.com/in/abdelmoubine/)

Sometimes, we need to get transcripts/subtitles of YouTube videos, but to do this, we would have to go to the YouTube video and manually generate the transcript. In Python, we have a package named youtube_transcript_api that can be used to automatically give you a transcript that you can use as plain text.

## Installation
First, let us install this package by running:
```sh
pip install youtube_transcript_api
pip progressbar
```
import the required package
```sh
from youtube_transcript_api import YouTubeTranscriptApi
import progressbar
import time
import sys
import os
```

## Run the code , Enjoy ♥