import os
import pathlib
import sys
import shutil
import logging
import Logger
import datetime
import time

#function - Readds all of the new list spit out by funRemoveJobItem, and puts it in the new list in the Job List
def funRemoval(intJobNumber, lstFilesToCheck = []):
    strTemp = "/Jobs/Job" + intJobNumber + ".txt"
    #Grabs the Job file
    strFolderPath = os.path.dirname(__file__)
    strFolderPath += strTemp
    with open(strFolderPath, "w") as filReFiles:
        for i in range(int(len(lstFilesToCheck))):
            print(lstFilesToCheck[i], file = filReFiles)

#function - Checks through the jobs list to find the file we want to remove
def funRemoveJobItem(lstFilesToCheck = [], strRemovalItem = ""):
    
    bolWish = False
    timTimeStart = time.time()
    
    #Checks every Item to see if it is the same as the requested removal file
    for i in range(int(len(lstFilesToCheck))):
        
        strHoldingItem = lstFilesToCheck[i]
        
        if strRemovalItem == strHoldingItem:
            
            #will Remove the item if it is the same
            lstFilesToCheck.pop(i)
            print("Removal Item Found")
            print("Item Removed Successfuly")
            
            #Log that it has been found
            Logger.funSuccessLogging(time.time() - timTimeStart, " Removal of a Item", strRemovalItem)
            bolWish = True
            
            #will force out of the loop so we don't get prombles with it getting out of the indexs of the array
            break
        else:
            
            #if we can't find that item in the string just moves to the next one
            i += 1
    
    if bolWish == False:
        
        print("Item Does not Exist in current Job")
        time.sleep(2)
        
    return(lstFilesToCheck)