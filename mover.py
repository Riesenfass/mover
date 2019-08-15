#This program will transfer files from a specified directory and place them in
#a destination directory based on file extension - if the file is a RAW image
#it will be moved to a subfolder named 'RAW', otherwise the image will be placed
#in the root of the destination directory.
#
#Author: Shane Myers
#Date: 9/10/15

import os
import shutil

#This function will return a list of files matching the extension pattern provided
def getMatchingFiles(sourceList, extensionPatterns):
    resultList =[]
    for file in sourceList:
        for extensionPattern in extensionPatterns:
            if extensionPattern in file:
                resultList.append(file)
    return resultList

#This function will grab a subset of files from the list, based on range inclusive
def inRange(sourceList, begin, end):
    #sourceList.sort() #Python apparently grabs file names already sorted, so there is no need to do this. Kept for future use.
    finalList=[]
    indexStart = sourceList.index(begin)
    indexEnd = sourceList.index(end)
    for item in sourceList:
        if sourceList.index(item) >= indexStart and sourceList.index(item) <= indexEnd:
            finalList.append(item)
    return finalList

#This function will remove files passed in as a list.
def deleteFromSource(listOfItems, sourceDirectory):
    for file in listOfItems:
        os.remove(sourceDirectory + file)

        
print("About to begin processing.")

#Defining variables
sourceDir = "C:\python-tests\source\\"
destDir = "C:\python-tests\dest\\"
deleteFromSrc = False
rawFileExtensions = [".cr2",".CR2"]
standardFileExtensions = [".jpeg", ".jpg",".JPG",".JPEG"]
startFileName = "IMG_2514.cr2"
endFileName = "IMG_2515.JPG"

#Open source directory
srcFileList=os.listdir(sourceDir)
srcFileList = inRange(srcFileList, startFileName,endFileName)

#verify dest directory exits, if it doesn't create it
destPath = os.path.dirname(destDir)
if not os.path.exists(destPath):
    print("Destination directory doesn't exist, creating...")
    os.mkdir(destDir, 777)
destRawPath = os.path.dirname(destDir+"RAW\\")
if not os.path.exists(destRawPath):
    print("Creating RAW folder")
    os.mkdir(destRawPath, 777)

#iterate over file list and copy from source to dest
tempList = getMatchingFiles(srcFileList, standardFileExtensions)
for srcFile in tempList :
    shutil.copy2(sourceDir+srcFile, destDir)
if deleteFromSrc == True:
        deleteFromSource(tempList, sourceDir)
tempList = getMatchingFiles(srcFileList, rawFileExtensions)
for srcFile in tempList :
    shutil.copy2(sourceDir+srcFile, destDir+"RAW\\")
if deleteFromSrc == True:
        deleteFromSource(tempList, sourceDir)
print("Processing complete, exiting.")
