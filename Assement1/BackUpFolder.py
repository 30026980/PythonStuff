import os
import pathlib
import sys
import shutil
import logging
import datetime
import Logger
import time

#Function - Checks for wether or not the backup file exists or if it needs creating, and creates the folder that will be used to backup everything
def funBackUpFolder():
    #Grabs the path it will be using
    strTemp = "/BackupFolder"
    strFolderPath = os.path.dirname(__file__)
    strFolderPath += strTemp
    
    #checks for if the Backup Folder has been made yet, and if it hasn't just creates it
    if not os.path.exists(strFolderPath):
        print(strFolderPath)
        os.makedirs(strFolderPath, exist_ok=True)
    
    #Creates what will store the backup files in
    os.makedirs(strFolderPath + "/CopyFiles", exist_ok = True)
    
#Function - Grabs the list of files needing to be copied and moves them to the backup folder. after all files are copied, Renames the folder to the data and job number
def funFileBackup(lstFilesToCopy = [], strJobNumber = ""):
    
    #Grabs the path it will be using
    strTemp = "/BackupFolder"
    strFolderPath = os.path.dirname(__file__)
    strFolderPath += strTemp
   
    #Used for later renaming the file as we need 2 varibles one with the folder name to copy and another to create a new folder to hold everything in
    strCopyFolderPath = strFolderPath + "/CopyFiles"
    timVeryStartTime = time.time()
    bolSuccessfulBackup = True
    intFailedItems = 0
    lstFailedItems = ""
    
    #Uses the list that was sent to it and goes through it to see how much elements/items are in it
    for i in range(int(len(lstFilesToCopy))):
        timStartTime = time.time()
        try:#Grabs the link to the folder that needs copying
            
            strTempLink = lstFilesToCopy[i]
            i += 1
            
            if os.path.isfile(strTempLink) == False:
                #Grabs the oringal folder name as copytree just removes this folder
                path = os.path.basename(strTempLink)
                #prints out to the consle all of the files that have beened backed up and there location
                print(shutil.copytree(strTempLink, strCopyFolderPath + "/" + path, dirs_exist_ok=True))
            
            #if the Item is a file
            elif os.path.isfile(strTempLink) == True:
                print(shutil.copy2(strTempLink, strCopyFolderPath))
            
            #if nothing is lost, this will print to the logger that it worked
            timTotalFileTime = timStartTime - time.time()
            print("AddedToLog")
            Logger.funSuccessLogging(timTotalFileTime, " BackupFiles", strTempLink)
        
        
        except FileNotFoundError:
            
            #This is just to tell if a file or folder doesn't exist for later
            timTotalFileTime = timStartTime - time.time()
            bolSuccessfulBackup = False
            lstFailedItems += strTempLink + " - "
            intFailedItems += 1
            
            #Writing to the logger saying the file/folder couldn't be found
            Logger.funFailedLogging(timTotalFileTime, "File Backup", "File Could Not Be Found", strTempLink)
            
    #this changes the name of the Copyfolder Location to the time, date and the job number
    os.replace(strCopyFolderPath, strFolderPath + "/" + datetime.datetime.strftime(datetime.datetime.today(),"%Y_%m_%d-%H:%M:%S") + " Job Number " + strJobNumber)
    
    #Checks if the whole backup worked or if something failed, how much failed and what failed
    if bolSuccessfulBackup == True:
        Logger.funSuccessLogging(time.time() - timVeryStartTime, " Full Backup ", "Job Complete")
    else:
        Logger.funFailedLogging(time.time() - timVeryStartTime, " Full Backup ", str(intFailedItems) + " Have Failed the back", "Items are = " + lstFailedItems)

#Function - Returns that the folder does exist 
#Varible strFolderLocation = what Folder do we want to check exists
def funValidFolder(strFolderLocation = ""):
    
    #For Logging Reasons
    timStartTime = time.time()
    
    #Checks if there isn't a file or folder at the location promted by the user, if True will report back there is no such file
    if not os.path.exists(strFolderLocation):
        Logger.funFailedLogging(timStartTime - time.time(), " Adding Job", "File/Folder Couldn't be found", strFolderLocation)
        return False
    else:
        return True