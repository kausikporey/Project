import smtplib
import pandas as pd
from datetime import date
import os
os.chdir(r"C:\Users\USER\Desktop\Project\Automatic Birthday Wisher")

GMAIL_ID = 'kousikporey0000@gmail.com'
GMAIL_PSWD = 'kausik@590'

def sendEmail(to,sub,msg):
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PSWD)
    s.sendmail(GMAIL_ID,to,f"Subject: {sub}\n\n{msg}")
    s.quit()


if __name__ == '__main__':
    df = pd.read_excel("BirthdayWisher.xlsx")
    today = date.today().strftime("%d-%m")
    yearNow = date.today().strftime("%Y")
    writeInd = []


    for index,item in df.iterrows():
        bday = item['Birthday'].strftime("%d-%m")
        if today == bday and yearNow not in str(item['Year']):
            to = item['Email']
            msg = item['Dialogue']
            print(f"Sending Email to {to}")
            sendEmail(to,"Happy Birthday",msg)
            name = item['Name']
            print(f"Email to {name} sended successfully.")
            writeInd.append(index) 

      
    for i in writeInd:
        yr = df.loc[i,'Year']
        df.loc[i,'Year'] = str(yr) +',' +str(yearNow)
    df.to_excel("BirthdayWisher.xlsx",index=False)    

        
