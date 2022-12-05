from youtube_transcript_api import YouTubeTranscriptApi
import progressbar
import time
import sys
import os

id = input("Enter the Video ID here then press ENTER: ")
lang = input("Enter the language code you want and hit ENTER '(English = en)': ")
srt = YouTubeTranscriptApi.get_transcript(id,languages=[lang])
def progressbar(it, prefix="", size=14, out=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("{}{}{} {}/{}".format(prefix, "█"*x, "-"*(size-x), j, count), 
                end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)
for i in progressbar(range(100), "Take a Coffee ♥ :", 30):
    time.sleep(0.1)

print("IMPORTANT: MAKE SURE THE FILE WITH '(.TXT)' FORMAT")

file_name = input("Enter file name '(filename.txt)': ")
with open(file_name, "w") as f:
    for i in srt:
        f.write("{}\n".format(i))
print(f"Your file {file_name} have been created ♥")
os.startfile(file_name)
os.system(file_name)
