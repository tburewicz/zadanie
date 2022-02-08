import sys
from zipfile import *
import os
from datetime import datetime

# Params
setZipName = sys.argv[1]
setVersion = sys.argv[2]
if len(sys.argv) == 3:
    update = "n"
else:
    update = sys.argv[3]

# Check if *.ZIP
if not setZipName.endswith('.zip'):
    setZipName = setZipName + ".zip"

# Current day and time
now = datetime.now()
currentDay = datetime.today().strftime('%Y-%m-%d')
currentTime = now.strftime("%H:%M:%S")
currentDate = currentDay + " " + currentTime

# Check if *.ZIP
if setVersion.endswith('.zip'):
    setZipName = setZipName + ".zip"


def createZipFile(zipname, version, updated):
    zipobject = ZipFile(zipname, 'w')
    zipobject.write(version)
    if updated != 0:
        zipobject.write(updated)
        os.remove(updated)
    os.remove(version)


def unzipFile(source, finish):
    try:
        with ZipFile(source, 'r') as zip:
            zip.extractall(finish)
    except (IOError, BadZipFile) as e:
        print("File corrupted")
        exit(1)


def checkExist(name):
    if os.path.isfile(str(name)):
        print("File " + str(name) + " status:  ALREADY EXISTS.")
        unzipFile(name, "./")
        if os.path.isfile("VERSION.txt"):
            f = open("VERSION.txt", "r")
            return f.read()
        else:
            print("File 'VERSION.txt' deosnt exist, but it will be soon.")


check = checkExist(setZipName)

with open('VERSION.txt', 'w') as f:
    f.write("Actual version: " + str(setVersion))
if update == "y":
    with open('updated.txt', 'w') as f:
        f.write(str(currentDate))
    update = "updated.txt"
    print("\nFile name: " + str(setZipName) + "\nFile version: " + str(setVersion) + "\nUpdate date: " + str(
        currentDate) + "\n")
else:
    update = 0
    #os.remove("updated.txt")
    print("\nFile name: " + str(setZipName) + "\nFile version: " + str(setVersion) + "\n")

createZipFile(setZipName, 'VERSION.txt', update)
