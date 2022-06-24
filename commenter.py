# imports modules
from os.path import exists
import shutil

# defines commenter subroutine
def commenter():

    # gets the file to comment from the user
    filelocation = str(input("##############################################\nPlease enter the complete file path of the file you wish to comment for\n##############################################\n"))

    # if it exists and is a python file then
    if exists(filelocation) and filelocation.endswith(".py"):

        # creates a coppy of the file ith the same name + coppy.py
        newlocation = filelocation.split('\\')
        newlocation[-1] = newlocation[-1][:-3] + "coppy.py"
        newlocation = "\\".join(newlocation)
        print(newlocation)
        shutil.copyfile(filelocation, newlocation)

        # opens the new file and reads the data
        file = open(newlocation,"a")
        content = file.readlines()
        file.close()

    # if file path doesnt match criteria prints appropriate message and re-runs subroutine
    else:
        print("##############################################\nSorry this file path isn't valid!\nPlease ensure your file path exsits and is a .py python file before re-entering!")
        commenter()

# runs commenter subroutine
commenter()
