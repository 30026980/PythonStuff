import os
import pathlib
import sys
import shutil
import logging
import datetime
import time
import smtplib

Api = ""
Key = ""

smtp = {"sender": "u", # mailjet.com verified sender
    "recipient": "", # mailjet.com verified recipient
    "server": "in-v3.mailjet.com", # mailjet.com SMTP server
    "port": 587, # mailjet.com SMTP port
    "user": Api, # mailjet.com user
    "password": Key} # mailjet.com password

#Function - Logs that the process was completed successfuly
def funSuccessLogging(timTimeTaken, strJob = "", strFileBackedUp = ""):
    
    #Grabs the path it will be using
    strTemp = "/LogFile.txt"
    strFolderPath = os.path.dirname(__file__)
    strFolderPath += strTemp
    
    #checks for if the Backup Folder has been made yet, and if it hasn't just creates it
    with open(strFolderPath, "a") as filLogFile:
        print(datetime.datetime.strftime(datetime.datetime.today(),"%Y_%m_%d-%H:%M:%S") + strJob + " SUCCESS " + str(timTimeTaken), strFileBackedUp, file = filLogFile)
  
#Function - Logs that the process was not completed and failed      
def funFailedLogging(timTimeTaken, strJob = "", strErrorCode = "", strFileNotFound = ""):
    
    #Grabs the path it will be using
    strTemp = "/LogFile.txt"
    strFolderPath = os.path.dirname(__file__)
    strFolderPath += strTemp
    
    #checks for if the Backup Folder has been made yet, and if it hasn't just creates it
    with open(strFolderPath, "a") as filLogFile:
        if strFileNotFound == "":
            
            #Checks if the error is caused by a missing file or not
            strTemp = datetime.datetime.strftime(datetime.datetime.today(),"%Y_%m_%d-%H:%M:%S") + strJob + strErrorCode + "FAILED " + str(timTimeTaken)
            
            print(strTemp, file = filLogFile)
            funEmail(str(strTemp))
            
        else:
            
            strTemp = datetime.datetime.strftime(datetime.datetime.today(),"%Y_%m_%d-%H:%M:%S ") + strJob + " " + strErrorCode + " - " + strFileNotFound + "- Could not be found - FAILED " + str(timTimeTaken), 
            
            print(strTemp, file = filLogFile)
            funEmail(str(strTemp))
            

def funEmail(message):
    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] + '\n' + 'Subject: Backup Error\n\n' + message + '\n'

    # connect to email server and send email
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
        smtp_server.close()
    except Exception as e:
        print("ERROR: An error occurred.")