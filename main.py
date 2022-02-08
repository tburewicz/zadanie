from zipfile import *
import os
from datetime import datetime

def createZipFile(zipName,version,updated):
    zipObject = ZipFile(zipName, 'w')
    zipObject.write(version)
    if updated != 0:
        zipObject.write(updated)
        os.remove(updated)
    os.remove(version)

def unzipFile(source,finish):
    try:
        with ZipFile(source, 'r') as zip:
            zip.extractall(finish)
    except (IOError, BadZipFile) as e:
        print("File corrupted")
        exit(1)

def checkExist(name):
    if os.path.isfile(str(name)):
        print(str(name) + " already exists.")
        unzipFile(name, "./")
        if os.path.isfile("VERSION.txt"):
            f = open("VERSION.txt", "r")
            return f.read()
        else:
            print("File 'VERSION.txt' deosn't exist, but it will be soon.")

print("Parameters\nSet zip file name:")
setZipName = input()
setZipName = setZipName + ".zip"

check = checkExist(setZipName)
if check == None:
    print("Set new file version")
else:
    print("\n" + str(check) + "\nSet new version:")
setVersion = input()

print("Do you want to save update date? (y/n)")
update = input()

with open('VERSION.txt', 'w') as f:
    f.write("Actual version: " + str(setVersion))
if update == "y":
    actualDate = datetime.today().strftime('%Y-%m-%d')
    with open('updated.txt', 'w') as f:
        f.write(str(actualDate))
    update = "updated.txt"
else:
    update = 0
    if os.path.isfile("updated.txt"):
        #if user dont want to have update file it can be deleted if exists
        os.remove("updated.txt")

createZipFile(setZipName, 'VERSION.txt', update)
