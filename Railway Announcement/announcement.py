      
import pandas as pd
from time import *
from threading import *
from playsound import playsound


def annnouncementTime(filename):
    while True:
        x = pd.read_excel(filename)
        for index,item in x.iterrows():
            hr = item['Hour']
            mnt = item['Minute']
            lt = localtime()
            if hr == lt.tm_hour and mnt == lt.tm_min:
                trName = item['Train Name']
                print("Announcement For Train : ",trName)
                playsound(f"Announcement_{trName}.mp3")       

annnouncementTime("railwayannouncement.xlsx")                        
