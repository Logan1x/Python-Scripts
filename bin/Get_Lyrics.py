from mutagen.easyid3 import EasyID3
import os
from os import listdir
from os.path import isfile,join
import lyricwikia
import requests

cwd = os.getcwd()
result_file = open('lyrics.txt','w')

for f in listdir(cwd):
    ext = f[f.rfind('.'):]
    try:
        if(not (ext == '.mp3' or ext == '.MP3')):
            raise Exception()
        audio = EasyID3(f)
        title = audio['title'][0]
        flag = title.find('-')
        if(flag>title.find('(') and not title.find('(') == -1 or flag == -1):
            flag = title.find('(')
        title = title[:flag if(flag>-1) else len(title)]
        artist = audio['artist'][0]
        flag = artist.find('(')
        if(flag>artist.find('-') and not artist.find('-') == -1 or flag == -1):
            flag = artist.find('-')
        artist = artist[:flag if(flag>-1) else len(artist)]
        artist = artist.split('&')[0]
        artist = artist.split(',')[0]
        print(artist)
        print(title)
        lyrics = lyricwikia.get_lyrics(artist,title)
        result_file.write('Artist:'+artist+' '+'Title: '+title+'\n\n'+'Lyrics:\r\n'+lyrics+'\n\n-------\n\n\n')
    except:
        print "Error"
        pass
result_file.close()

