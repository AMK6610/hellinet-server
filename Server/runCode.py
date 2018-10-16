import os
from subprocess import Popen , PIPE

def runCodesTogether(file,otherfile,fileAddress,otherfileAddress):
    os.chdir(directory + "\Server")
    # print(os.path.join(fileAddress, file))
    fight = Popen(['python', 'server.py', os.path.join(fileAddress, file), os.path.join(otherfileAddress,otherfile)], shell=True,
                    stdout=PIPE, stdin=PIPE)
    out, err = fight.communicate()
    fight.wait()
    # print(out)

os.chdir("..")
directory = os.getcwd()

for file in os.listdir(directory + "\Uploads\python"):
    os.chdir(directory + "\Uploads\python")
    fileAddress = os.getcwd();
    if file.endswith(".py"):
        for otherfile in os.listdir(directory + "\Uploads\python"):
            os.chdir(directory + "\Uploads\python")
            otherfileAddress = os.getcwd()
            if otherfile.endswith(".py") and otherfile != file:
                runCodesTogether(file,otherfile,fileAddress,otherfileAddress)
        for otherfile in os.listdir(directory + "\Uploads\c++"):
            os.chdir(directory + "\Uploads\c++")
            otherfileAddress = os.getcwd()
            if otherfile.endswith(".exe"):
                runCodesTogether(file, otherfile,fileAddress,otherfileAddress)
        for otherfile in os.listdir(directory + "\Uploads\pascal"):
            os.chdir(directory + "\Uploads\pascal")
            otherfileAddress = os.getcwd()
            if otherfile.endswith(".pas"):
                runCodesTogether(file, otherfile, fileAddress, otherfileAddress)

for file in os.listdir(directory + "\Uploads\c++"):
    os.chdir(directory + "\Uploads\c++")
    fileAddress = os.getcwd();
    if file.endswith(".exe"):
        for otherfile in os.listdir(directory + "\Uploads\python"):
            os.chdir(directory + "\Uploads\python")
            otherfileAddress = os.getcwd()
            if otherfile.endswith(".py"):
                runCodesTogether(file,otherfile,fileAddress,otherfileAddress)
        for otherfile in os.listdir(directory + "\Uploads\c++"):
            os.chdir(directory + "\Uploads\c++")
            otherfileAddress = os.getcwd()
            if otherfile.endswith(".exe") and otherfile != file:
                runCodesTogether(file, otherfile,fileAddress,otherfileAddress)
        for otherfile in os.listdir(directory + "\Uploads\pascal"):
            os.chdir(directory + "\Uploads\pascal")
            otherfileAddress = os.getcwd()
            if otherfile.endswith(".pas"):
                runCodesTogether(file, otherfile, fileAddress, otherfileAddress)

for file in os.listdir(directory + "\Uploads\pascal"):
    os.chdir(directory + "\Uploads\pascal")
    fileAddress = os.getcwd();
    if file.endswith(".pas"):
        for otherfile in os.listdir(directory + "\Uploads\python"):
            os.chdir(directory + "\Uploads\python")
            otherfileAddress = os.getcwd()
            if otherfile.endswith(".py"):
                runCodesTogether(file,otherfile,fileAddress,otherfileAddress)
        for otherfile in os.listdir(directory + "\Uploads\c++"):
            os.chdir(directory + "\Uploads\c++")
            otherfileAddress = os.getcwd()
            if otherfile.endswith(".exe"):
                runCodesTogether(file, otherfile,fileAddress,otherfileAddress)
        for otherfile in os.listdir(directory + "\Uploads\pascal"):
            os.chdir(directory + "\Uploads\pascal")
            otherfileAddress = os.getcwd()
            if otherfile.endswith(".pas") and otherfile != file:
                runCodesTogether(file, otherfile, fileAddress, otherfileAddress)