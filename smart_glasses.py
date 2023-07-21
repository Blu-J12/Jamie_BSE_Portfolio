from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import os
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
import time
import datetime
import wolframalpha
# import speech_recognition as sr
# import pyaudio
import wikipedia

# WOLFRAM
app_id = ''
# Put your app id here (You can sign up for one at the Wolfram Alpha website.)

client = wolframalpha.Client(app_id)
res = client.query('What is the temperature in ______')
# Put any place here.
answer = next(res.results).text
str1 = answer
str2 = str1.split('(', 1)[0]

bad_chars = [';', '|', '(', ')', '+', '=', '1']

num = ["05", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55", "0"]

def dateTime():
  cdt = datetime.datetime.now()
  min1 = str(cdt.minute)
  hour = str(cdt.hour)

  with canvas(device) as draw:
    draw.text((0, 0), hour, fill = "blue")
    draw.text((11, 0),":", fill = "blue")
    draw.text((15, 0), min1, fill = "blue")
    draw.text((0, 0), "___________", fill = "yellow")
    draw.text((33, 0), str2, fill = "white")
    draw.text((0, 115), "...", fill = "white")
def listen():
  print('listening...')
  time.sleep(5)
  dateTime()
  global val
  val = input()
  #os.system('arecord -d 4 -f cd -t wav -D bluealsa:DEV=00:00:00:00:00:00,PROFILE=sco test.wav') #Replace the MAC address with that of your hedset


def say(statement):
  statement1 = statement.replace(" ", "_")
  os.system('espeak ' + str(statement1) + ' -ven+f3 -k5 -s130 --stdout | aplay -D bluealsa:DEV=00:00:00:00:00:00,PROFILE=sco') #Change the MAC address here as well

def query(query):
  client = wolframalpha.Client(app_id)
  res = client.query(query)
  answer = next(res.results).text
  answer1 = answer.partition('\n')[0]
  print(answer1)

def start_up():
  hour1 = int(datetime.datetime.now().hour)
  if hour1 >= 0 and hour1 < 12:
      print('Good morning.')
      #say('good morning')
  elif hour1 >= 12 and hour1 < 20:
      print('Good afternoon.')
      #say('good afternoon')
  else:
      print('Good evening.')
      #say('good evening')
  print('How may I help you?')
  # say('how may i help you)

serial = i2c(port=1, address=0x3C)
# Put in the address of your display instead of 0x3C, it may be 0x3C.
device = ssd1306(serial, rotate=0)

text = ("What would you like to say? ")
text1 = ('\n'.join([text[i:i+11] for i in range(0, len(text), 11)]))

cdt = datetime.datetime.now()

start_up()

def utilitys():
  cdt = datetime.datetime.now()
  min1 = str(cdt.minute)
  hour = str(cdt.hour)

  with canvas(device) as draw:
    draw.text((0, 0), hour, fill = "blue")
    draw.text((11, 0),":", fill = "blue")
    draw.text((15, 0), min1, fill = "blue")
    draw.text((0, 0), "___________", fill = "yellow")
    draw.text((33, 0), str2, fill = "white")
    if min1 in num:
      client = wolframalpha.Client(app_id)
      res = client.query('What is the temperature in San Fransisco')
      answer = next(res.results).text
      str1 = answer
      str3 = str1.split('(', 1)[0]
      draw.text((33, 0), str3, fill = "white")

def util(func1):
  cdt = datetime.datetime.now()
  min1 = str(cdt.minute)
  hour = str(cdt.hour)

  with canvas(device) as draw:
    draw.text((0, 0), hour, fill = "blue")
    draw.text((11, 0),":", fill = "blue")
    draw.text((15, 0), min1, fill = "blue")
    draw.text((0, 0), "___________", fill = "yellow")
    #draw.text((0, 9), date, fill = "white")
    draw.text((33, 0), str2, fill = "white")
    draw.text((0, 64), func1, fill = "white")

while True:
  utilitys()
  listen()
  try:
    if len(val) >= 2:
      if 'news' in val:
        news_url="https://news.google.com/news/rss"
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        i = 0
        util('news...')
        for news in news_list:
          print(news.title.text + "\n")
          print(news.link.text)
          i += 1
          time.sleep(1)
          if i == 3:
            break
        del val
        util("news...")
        time.sleep(3)

      if 'exit program' in val:
        os.system('pkill -f edited.py')
        del val

      if 'time' in val:
        cdt1 = datetime.datetime.now()
        h = cdt1.hour
        m = cdt1.minute
        print(str(h) + ':' + str(m))
        say(str(h))
        say(str(m))

        del val
        util("time...")
        time.sleep(3)

      if 'play my music' in val:
        util("music...")
        time.sleep(2)

# Replace the 00:00:00:00:00:00 with the MAC address of your headset
        os.system('aplay -D bluealsa:DEV=00:00:00:00:00:00,PROFILE=sco /home/pi/Desktop/Imagine.wav')
        del val
        say('Would you like me to play the next song')
        listen()
        if 'Yes' in val:
          os.system('aplay -D bluealsa:DEV=00:00:00:00:00:00,PROFILE=sco /home/pi/Desktop/BeautifulName.wav')
          del val
          say('would you like me to play the next song')
          listen()
          if 'Yes' in val:
            os.system('aplay -D bluealsa:DEV=00:00:00:00:00:00,PROFILE=sco /home/pi/Desktop/Oceans.wav')
            del val
        if 'No' in val:
          del val
          continue

      try:
        client1 = wolframalpha.Client(app_id)
        res1 = client1.query(val)
        answer1 = next(res1.results).text
        answer2 = answer1.partition('\n')[0]
        for i in bad_chars:
          answer2 =  answer2.replace(i, '')
        print(answer2)
      except:
        try:
          print(wikipedia.summary(val, sentences = 1))
        except:
          print('')
      del val
  except:
    print(' ')
