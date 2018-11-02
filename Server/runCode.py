import os
import openpyxl
from openpyxl.styles import Font
from subprocess import Popen , PIPE

def runCodesTogether(file,otherfile,fileAddress,otherfileAddress):
    os.chdir(directory + "\Server")
    # print(os.path.join(fileAddress, file))
    fight = Popen(['python', 'server.py', os.path.join(fileAddress, file), os.path.join(otherfileAddress,otherfile)], shell=True,
                    stdout=PIPE, stdin=PIPE)
    out, err = fight.communicate()
    fight.wait()
    return out
    # print(out)

os.chdir("..")
directory = os.getcwd()
excelDir = directory

wb = openpyxl.load_workbook('OutputExcel.xlsx')
sheet = wb['Sheet1']
sheet.row_dimensions[1].height = 20
sheet.row_dimensions[1].width = 500

sheet['A1'] = 'Team 1'
sheet['B1'] = 'Team 2'
fontObj1 = Font(name='Times New Roman', bold=True)
sheet['A1'].font = fontObj1
sheet['B1'].font = fontObj1

columncounter = 2;

wb.save('OutputExcel.xlsx')

for file in os.listdir(directory + "\\Uploads\python"):
    os.chdir(directory + "\\Uploads\python")
    fileAddress = os.getcwd();
    if file.endswith(".py"):
        for otherfile in os.listdir(directory + "\\Uploads\python"):
            os.chdir(directory + "\\Uploads\python")
            otherfileAddress = os.getcwd()
            if otherfile.endswith(".py") and otherfile != file:
                result = runCodesTogether(file,otherfile,fileAddress,otherfileAddress)
                if result == 1:
                    sheet.cell(row=columncounter, column=1).value = "Winner"
                    sheet.cell(row=columncounter, column=2).value = "Loser"
                else:
                    sheet.cell(row=columncounter, column=1).value = "Loser"
                    sheet.cell(row=columncounter, column=2).value = "Winner"
                columncounter += 1
        for otherfile in os.listdir(directory + "\\Uploads\exe"):
            os.chdir(directory + "\\Uploads\exe")
            otherfileAddress = os.getcwd()
            if otherfile.endswith(".exe"):
                result = runCodesTogether(file, otherfile,fileAddress,otherfileAddress)
                if result == 1:
                    sheet.cell(row=columncounter, column=1).value = "Winner"
                    sheet.cell(row=columncounter, column=2).value = "Loser"
                else:
                    sheet.cell(row=columncounter, column=1).value = "Loser"
                    sheet.cell(row=columncounter, column=2).value = "Winner"
                columncounter += 1
        for otherfile in os.listdir(directory + "\\Uploads\pascal"):
            os.chdir(directory + "\\Uploads\pascal")
            otherfileAddress = os.getcwd()
            if otherfile.endswith(".pas"):
                result = runCodesTogether(file, otherfile, fileAddress, otherfileAddress)
                if result == 1:
                    sheet.cell(row=columncounter, column=1).value = "Winner"
                    sheet.cell(row=columncounter, column=2).value = "Loser"
                else:
                    sheet.cell(row=columncounter, column=1).value = "Loser"
                    sheet.cell(row=columncounter, column=2).value = "Winner"
                columncounter += 1

for file in os.listdir(directory + "\\Uploads\exe"):
    os.chdir(directory + "\\Uploads\exe")
    fileAddress = os.getcwd();
    if file.endswith(".exe"):
        for otherfile in os.listdir(directory + "\\Uploads\python"):
            os.chdir(directory + "\\Uploads\python")
            otherfileAddress = os.getcwd()
            if otherfile.endswith(".py"):
                result = runCodesTogether(file,otherfile,fileAddress,otherfileAddress)
                if result == 1:
                    sheet.cell(row=columncounter, column=1).value = "Winner"
                    sheet.cell(row=columncounter, column=2).value = "Loser"
                else:
                    sheet.cell(row=columncounter, column=1).value = "Loser"
                    sheet.cell(row=columncounter, column=2).value = "Winner"
                columncounter += 1
        for otherfile in os.listdir(directory + "\\Uploads\exe"):
            os.chdir(directory + "\\Uploads\exe")
            otherfileAddress = os.getcwd()
            if otherfile.endswith(".exe") and otherfile != file:
                result = runCodesTogether(file, otherfile,fileAddress,otherfileAddress)
                if result == 1:
                    sheet.cell(row=columncounter, column=1).value = "Winner"
                    sheet.cell(row=columncounter, column=2).value = "Loser"
                else:
                    sheet.cell(row=columncounter, column=1).value = "Loser"
                    sheet.cell(row=columncounter, column=2).value = "Winner"
                columncounter += 1
        for otherfile in os.listdir(directory + "\\Uploads\pascal"):
            os.chdir(directory + "\\Uploads\pascal")
            otherfileAddress = os.getcwd()
            if otherfile.endswith(".pas"):
                result = runCodesTogether(file, otherfile, fileAddress, otherfileAddress)
                if result == 1:
                    sheet.cell(row=columncounter, column=1).value = "Winner"
                    sheet.cell(row=columncounter, column=2).value = "Loser"
                else:
                    sheet.cell(row=columncounter, column=1).value = "Loser"
                    sheet.cell(row=columncounter, column=2).value = "Winner"
                columncounter += 1

for file in os.listdir(directory + "\\Uploads\pascal"):
    os.chdir(directory + "\\Uploads\pascal")
    fileAddress = os.getcwd();
    if file.endswith(".pas"):
        for otherfile in os.listdir(directory + "\\Uploads\python"):
            os.chdir(directory + "\\Uploads\python")
            otherfileAddress = os.getcwd()
            if otherfile.endswith(".py"):
                result = runCodesTogether(file,otherfile,fileAddress,otherfileAddress)
                if result == 1:
                    sheet.cell(row=columncounter, column=1).value = "Winner"
                    sheet.cell(row=columncounter, column=2).value = "Loser"
                else:
                    sheet.cell(row=columncounter, column=1).value = "Loser"
                    sheet.cell(row=columncounter, column=2).value = "Winner"
                columncounter += 1
        for otherfile in os.listdir(directory + "\\Uploads\exe"):
            os.chdir(directory + "\\Uploads\exe")
            otherfileAddress = os.getcwd()
            if otherfile.endswith(".exe"):
                result = runCodesTogether(file, otherfile,fileAddress,otherfileAddress)
                if result == 1:
                    sheet.cell(row=columncounter, column=1).value = "Winner"
                    sheet.cell(row=columncounter, column=2).value = "Loser"
                else:
                    sheet.cell(row=columncounter, column=1).value = "Loser"
                    sheet.cell(row=columncounter, column=2).value = "Winner"
                columncounter += 1
        for otherfile in os.listdir(directory + "\\Uploads\pascal"):
            os.chdir(directory + "\\Uploads\pascal")
            otherfileAddress = os.getcwd()
            if otherfile.endswith(".pas") and otherfile != file:
                result = runCodesTogether(file, otherfile, fileAddress, otherfileAddress)
                if result == 1:
                    sheet.cell(row=columncounter, column=1).value = "Winner"
                    sheet.cell(row=columncounter, column=2).value = "Loser"
                else:
                    sheet.cell(row=columncounter, column=1).value = "Loser"
                    sheet.cell(row=columncounter, column=2).value = "Winner"
                columncounter += 1