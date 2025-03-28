import logging
import time
import os
import BackupCfg
import BackUpFolder
import Remover


#Function, Moves everthing up
def funClear():
    for i in range(30):
        print('-\n-')
        time.sleep(0.01)

#Function types out the welcome Text with little breaks between each type
def funWelcome():
    
    print("- Welcome to the backup App")
    time.sleep(0.5)
    
    print("- if you wish to backup type 1")
    time.sleep(0.2)
    
    print("- if you wish to add a item type 2")
    time.sleep(0.2)
    
    print("- if you wish to remove a item type 3")
    time.sleep(0.2)
    
    print("- if you wish to view all current items type 4")
    
#Keeps the Loop Going so you never have to close the console
bolKeepUpLoop = True

while bolKeepUpLoop == True:
    #Creates a varible that we will use to hold peoples input
    
    strUserInput = ""
    #1 = Backup, 2 = Add Item, 3 = Remove Item, 4 = View Items
    funClear()
    
    funWelcome()
    #a Varible we will use later to check if the number the user enter earlier is a number and is a vaild use case
    bolWrong = False
    while bolWrong == False:
        
        #Grabs what the user has typed
        strUserInput = input()
        
        #if the user choiced 1 Starts the Backup Process
        if strUserInput == "1":
            
            funClear()
            print("-Job Number Wanting to run (Type back if you wish to go back")
            strJob = input().lower()
            
            #If the users wants to go back they can
            if strJob == "back":
                bolWrong = True
            
            else:
                
                while bolWrong == False:
                   
                    #See if the job is a vaild job
                    if BackupCfg.funFindJob(strJob) == True:
                        
                        #Gets the list of files needing to be copied
                        lstNeedCopyFiles = BackupCfg.funFindJobList(strJob)
                        
                        bolWrong = True
                        #Creates the backup Folder
                        BackUpFolder.funBackUpFolder()
                        #Puts all the files that need copying in, and the job number and copys the files over
                        
                        BackUpFolder.funFileBackup(lstNeedCopyFiles, strJob)
                        input("-Press enter to return to the start of the program")
                        
                    else:
                        
                        print("-Job could not be found try a job that exist")
                        strJob = input()
                        #If we want to go back here is our way
                        
                        if strJob == "back":
                            bolWrong = True
                            
        #if the user wants to add a item to the job with 2
        elif strUserInput == "2":
            
            funClear()
            print("-Job Number Wanting to add too")
            strJob = input().lower()
            
            if strJob == "back":
                bolWrong = True
            else:
                while bolWrong == False:
                    
                    #if the job exists
                    if BackupCfg.funFindJob(strJob) == True:
                        
                        bolVaildUrl = False
                        while bolVaildUrl == False:
                            
                            #find all the current jobs in the file to display to the user
                            lstNeedCopyFiles = BackupCfg.funFindJobList(strJob)
                            print(lstNeedCopyFiles)
                            
                            strTempHoldUrl = input("-file you wish to add \n")
                            bolGoBack = False
                            
                            #Checks to see if our Url is a vaild url to the file
                            bolVaildUrl = BackUpFolder.funValidFolder(strTempHoldUrl)
                            
                            if strTempHoldUrl.lower() == "back":
                                
                                print("Going Back")
                                bolGoBack = True
                                bolVaildUrl = True
                                bolWrong = True
                            
                            if bolVaildUrl == False:
                                
                                print("-Url is not Vaild")
                        
                        if bolGoBack == False:
                            
                            print("-File Found")
                            time.sleep(0.1)
                            
                            #the Function that adds our job to the job list
                            BackupCfg.funAddsJob(strJob, strTempHoldUrl)
                            print("-Added File to list")
                            time.sleep(0.1)
                            
                            strAnotherFile = input("-do you wish to add another file -'y' or 'n'\n")
                            if strAnotherFile.lower() == "n":
                                bolWrong = True
                    
                    else:
                        
                        print("-Job could not be found try a job that exist")
                        strJob = input()
                        
                        if strJob == "back":
                            bolWrong = True
        
        #if the user wants to remove a item they use 3
        elif strUserInput == "3":
            
            funClear()
            print("-Job Number That contains Url Removal")
            strJob = input().lower()
            
            if strJob == "back":
                bolWrong = True
            else:
                
                while bolWrong == False:
                    
                    #to see if the job is vaild
                    if BackupCfg.funFindJob(strJob) == True:
                        
                        #finding the list for our jobs
                        lstNeedCopyFiles = BackupCfg.funFindJobList(strJob)
                        print(lstNeedCopyFiles)
                        strTempHoldUrl = input("-file you wish to Remove \n")
                        
                        if strTempHoldUrl.lower() == "back": 
                            bolWrong = True
                        else:
                            
                            #Will try to remove the item, if the item does not exist this will handle it still
                            lstTemp = Remover.funRemoveJobItem(lstNeedCopyFiles, strTempHoldUrl)
                            
                            #this will re add the jobs to the files
                            Remover.funRemoval(strJob,lstTemp)
                            strAnotherFile = input("-do you wish to Remove another item -'y' or 'n'\n")
                            
                            if strAnotherFile.lower() == "n":
                                bolWrong = True
                    else:
                        
                        print("-Job could not be found try a job that exist")
                        strJob = input()
                        
                        if strJob == "back":
                            bolWrong = True
        
        #if the user wishes to see all that is in a job they use 4
        elif strUserInput == "4":
            
            funClear()
            print("-Job Number That you wish to see elements")
            strJob = input().lower()
            
            if strJob == "back":
                bolWrong = True
            
            else:
                
                while bolWrong == False:
                    
                    #if the jobs exist will find and print everything in the file
                    if BackupCfg.funFindJob(strJob) == True:
                        
                        lstNeedCopyFiles = BackupCfg.funFindJobList(strJob)
                        print(lstNeedCopyFiles)
                        
                        bolWrong = True
                        print("-Press enter when you wish to return to start")
                        
                        strJob = input()
                        
                    else:
                        
                        print("-Job could not be found try a job that exist")
                        strJob = input()
                        
                        if strJob == "back":
                            bolWrong = True
        
        else:
            print("-\n- Not a Vaild Function Please use the Functions above to select one")