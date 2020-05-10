import requests
from bs4 import BeautifulSoup

url = 1
while(url != 'quit'):
    url = str(input("Paste the link of the playlist or type 'quit' to close: "))
    try:
        timeList = []
        hours = []
        minutes= []
        seconds = []

        r = requests.get(url)

        bs = BeautifulSoup(r.text, 'html.parser')

        videoTime = bs.find_all('span', {'aria-label': True}, class_= False)

        for i in range(len(videoTime)):
            timeList.append(videoTime[i].get_text())
            
            if(len(timeList[i]) >= 7):
                hours.append(int(timeList[i].split(':')[0]))
                minutes.append(int(timeList[i].split(':')[1]))
                seconds.append(int(timeList[i].split(':')[2]))

            if(len(timeList[i]) >= 3 and len(timeList[i]) < 7):
                hours.append(0)
                minutes.append(int(timeList[i].split(':')[0]))
                seconds.append(int(timeList[i].split(':')[1]))
                
        calcSeconds =sum(seconds)%60 
        calcMinutes =  (sum(minutes) + int(sum(seconds)/60) )% 60
        calcHours = int((sum(minutes) + sum(seconds)/60)/ 60 ) + sum(hours)
        print("......TIME.......")
        print("{}H:{}M:{}S".format(calcHours,calcMinutes,calcSeconds))
        print(".................")
        
    except:
        if(url == 'quit'):
            print("Bye! :) ")
        else:
            print("Sorry. I can't analyse this. Please, check this a youtube playlist link.")
