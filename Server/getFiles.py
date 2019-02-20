import urllib.request
import requests
import time
import os
from subprocess import Popen, PIPE


class Result:
    def __init__(self):
        self.out = 1
        self.time = 20


randomClient = '../Uploads/python3/client_tester.py'


def runCodesTogether(fileAddress, otherfileAddress):
    current_milli_time = int(round(time.time() * 1000))
    print("SALAM", os.path.join(fileAddress), os.path.join(otherfileAddress))
    fight = Popen(['python', 'server.py', os.path.join(fileAddress), os.path.join(otherfileAddress)],
                  shell=True,
                  stdout=PIPE, stdin=PIPE)
    out, err = fight.communicate()
    print(out, err)
    # fight.wait()
    current_milli_time2 = int(round(time.time() * 1000))
    processTime = current_milli_time2 - current_milli_time

    result = Result()
    result.out = int(out.decode('UTF-8').replace("\r\n", "").split(' ')[-1])
    print(result.out)
    result.time = processTime
    return result
    # print(out)


# while True:
t1 = time.time()
url = 'http://gamestep.firststep.ir/upload-hellinet/'
files = requests.get(url + "check-new-files.php").text.split('####')
# print(files, requests.get(url + "check-new-files.php"))
for file in files:
    # print(file)
    if file == "":
        continue
    response = urllib.request.urlretrieve(file, "../Uploads/python3/" + file.split("/")[-1])

    wins = 0
    times = [0, 0, 0, 0, 0]
    for i in range(5):
        res = runCodesTogether("../Uploads/python3/" + file.split("/")[-1], randomClient)
        if res.out == 1:
            wins += 1
        times[i] = res.time
    data = {'id': (file.split('/')[-1]).split('.')[0],
            'wins': wins,
            'time1': times[0],
            'time2': times[1],
            'time3': times[2],
            'time4': times[3],
            'time5': times[4]}
    # print(data)
    t = requests.post(url + "set-score.php", json=data)
    print(t.text)

time.sleep(5 - (time.time() - t1))
