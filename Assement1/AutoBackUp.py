import os
import pathlib
import sys
import shutil
import logging
import datetime
import Logger
import time
import BackupCfg
import BackUpFolder
    
#to run use 'python3 AutoBackUp.py 1' #tho Make sure the terminal is already on the BackupFolder or the whole path from where you are at to the file
#How it works 'python3 "This Files Location" "The Job Number"'


timStartTime = time.time()

#if there is nothing added for the auto backup, this will ecsape into the excepts and say no job number was added
try:
    dicJobs = sys.argv[1]
except:
    Logger.funFailedLogging(time.time() - timStartTime, "Auto Backup", "Job File not Added", "No Locations was Added")
    
#If something is type this will run but if a job doesn't exist that is type reports back that the job file couldn't be found
try:
    strJob = dicJobs
    if BackupCfg.funFindJob(strJob) == True:
        #Will run the same thing as Backup.py 1 does but will not promt to keep it runing
        lstNeedCopyFiles = BackupCfg.funFindJobList(strJob)
        bolWrong = True
        BackUpFolder.funBackUpFolder()
        BackUpFolder.funFileBackup(lstNeedCopyFiles, strJob)
except:
    Logger.funFailedLogging(time.time() - timStartTime, "Auto Backup", "Job File could not be found", dicJobs)