import os
import Logger
import time
#Function - Grabs all of the jobs from the jobs text file
#Varible strDirection - just the number of what job they want to do
def funFindJobList(strDirection = ""):
    
    #Adds that Job number to the url of the job file
    strTemp = "/Jobs/Job" + strDirection + ".txt"
    
    #Grabs the Job file
    strFolderPath = os.path.dirname(__file__)
    strFolderPath += strTemp
    
    #our Temp Storage of all the jobs links
    recJobListing = []
    
    #Opens this job file
    with open(strFolderPath) as objJobFile:
        
        print("-Job File Opened")
        
        #Reads the job files
        tempLines = objJobFile.readlines()
        
        #see how much jobs are needed to be completed
        intLinesNeedingToOpen = len(tempLines)
        print("-Amount of Jobs Found", intLinesNeedingToOpen)
        
        #Loops for how much Jobs there are
        for i in range(int(intLinesNeedingToOpen)):
            
            #a string that contains the job
            strTempLine = tempLines[i]
            
            #removes the \n at the end of it
            recTemp = strTempLine.strip('\n')
            
            #Adds the job to the list of job links
            recJobListing.append(recTemp)
            i += 1
            
        #Returns the listing of Job Links
        return recJobListing

#Function - checks to see if the job is a vaild job
def funFindJob(strDirection = ""):
    
    #Adds that Job number to the url of the job file
    strStartTime = time.time()
    strTemp = "/Jobs/Job" + strDirection + ".txt"
    strFolderPath = os.path.dirname(__file__)
    strFolderPath += strTemp
    
    #if job file can't be found then it will return false
    if not os.path.exists(strFolderPath):
        
        print("-Job File could not be found")
        Logger.funFailedLogging(strStartTime - time.time(), "-Task - Finding Job file-", "Could Not Find Job File", strFolderPath)
        return False
    
    else:
        
        print("-Job File Found")
        Logger.funSuccessLogging(strStartTime - time.time(), " -Task - Finding Job file- Found Job File ", strFolderPath)
        return True

#Function - Adds the url to the new job
def funAddsJob(strDirection = "", NewUrl = ""):
    
    timStartTime = time.time()
    
    #Adds that Job number to the url of the job file
    strTemp = "/Jobs/Job" + strDirection + ".txt"
    
    #Grabs the Job file
    strFolderPath = os.path.dirname(__file__)
    strFolderPath += strTemp
    
    #This way will create stuff with out Overriding the file
    with open(strFolderPath, "a") as filWeapons:
        print(NewUrl, file = filWeapons)
        Logger.funSuccessLogging(timStartTime, " Adding Job", strFolderPath)