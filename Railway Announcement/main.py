import os
import pandas as pd
from pydub import AudioSegment
from playsound import playsound
from gtts import gTTS


def textToSpeech(text,file):
    mytext = str(text)
    myobj = gTTS(text = mytext,lang = 'en',slow = False)
    myobj.save(file)
def mergeAudio(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio) 
    return combined
def createAnnouncement(filename):
    ex = pd.read_excel(filename)
    for index,item in ex.iterrows():
        trNo = item['Train No']
        trFrom = item['From']
        trVia = item['Via']
        trTo = item['To']
        trPlno = item['Platform No']
        trName = item['Train Name']
        textToSpeech(f"Passenger! ,may  i  have your attention please. Train Number : {trNo}, {trName} from   , {trFrom}  ,  to ,{trTo}   ,via {trVia} ,  is   expected   within   15   mins  ,at   platform   nnmber  , {trPlno}",'2_rail.mp3') 
        audios = [f"{i}_rail.mp3" for i in range(1,4)]
        announcement  = mergeAudio(audios)  
        announcement.export(f"Announcement_{trName}.mp3",format="mp3")  
        print(f"Announcement is ready for train name {trName}")
createAnnouncement("railwayannouncement.xlsx")