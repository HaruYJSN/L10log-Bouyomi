import os
import sys
import time
import logging
import requests
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import xml.etree.ElementTree as ET
path="C:\\Users\\Haru\\AppData\\Local\\WEATHERNEWS INC\\The Last 10-Second\\flash\\xml\\"
datefile="date.xml"
eq_dt="rt_eq.xml"
print(path+datefile)

def bouyomi(text='', voice=0, volume=-1, speed=-1, tone=-1):
    res = requests.get(
        'http://localhost:50080/Talk',
        params={
            'text': text,
            'voice': voice,
            'volume': volume,
            'speed': speed,
            'tone': tone})
    return res.status_code

def command():
    print("dateupdated")
    with open(path+eq_dt, encoding="shift_jis") as file:
        xml = file.read()
        with open(".\\rt_eq.xml",mode="w" , encoding="utf-8") as file1:
            file1.write(xml)
    #root = ET.fromstring(xml)
    tree = ET.parse(eq_dt)
    root = tree.getroot()
    a=1
    #print(root)
    for data in root:
        for eq_count in data:
            for eq in eq_count:
                #print(eq.tag,eq.text)
                for report in eq:
                    print(report.text)
                    a=a+1
                    if a==7:
                        shingen=report.text
                    elif a==16:
                        reachtime=report.text
                    elif a==19:
                        maxshindo=report.text
                    elif a==20:
                        estshindo=report.text
                    elif a==21:
                        occtime=report.text
                        talktext=shingen+"で地震.推定される"+maxshindo+".現在地の"+estshindo+""
                        bouyomi(talktext,2,150,100,125)
                        print(talktext)
                    #print(report.tag,report.text)
    #print(eq.find("comment").text)
    


def main():
    before=open(path+datefile, "r").readlines()
    #print(before)
    while True:
        after=open(path+datefile, "r").readlines()
        #print(after)
        if before!=after:
            command()
        before=after
        time.sleep(1)

main()



        