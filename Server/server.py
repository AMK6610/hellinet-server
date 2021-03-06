# import copy
# import datetime
# import os
# import sys
# import time
# from subprocess import Popen, PIPE
#
# os.chdir("..")
# sys.path.append(os.path.join(os.getcwd()))
# os.chdir("Server")
# print('\n'.join(sys.path))
#
# from Models.Army import Army
# from Models.Map import Map
#
# # f = open("demofile.txt", "w")
# # f.write("Now the file has one more line!")
# # f.write(str(sys.argv))
# # f.close()
#
# player1Str = sys.argv[1]
# player2Str = sys.argv[2]
# player1_id = 1
# player2_id = 2
#
# player1_dir = player1Str.split('/')
# player2_dir = player2Str.split('/')
#
# ############### hypo: python2 is python 2.7 in cmd
#
# cmd1 = 'python'
# cmd2 = 'python'
# if player1_dir[-2] == 'python2':
#     cmd1 = 'python2'
#     player1 = Popen([cmd1, player1Str, str(player1_id)], shell=True, stdout=PIPE, stdin=PIPE)
# elif player1_dir[-2] == 'cpp':
#     cmd1 = 'g++'
#     dir = os.getcwd()
#     # os.chdir('/'.join(player1_dir[:-1]))
#     player1 = Popen([cmd1, player1Str, '-o', player1_dir[-1].split('.')[0] + '.exe'], shell=True, stdout=PIPE, stdin=PIPE)
#     # os.chdir(dir)
#     player1.communicate()
#     player1 = Popen([player1_dir[-1].split('.')[0] + '.exe', str(player1_id)], shell=True, stdout=PIPE, stdin=PIPE)
# else:
#     player1 = Popen([cmd1, player1Str, str(player1_id)], shell=True, stdout=PIPE, stdin=PIPE)
#
# if player2_dir[-2] == 'python2':
#     cmd2 = 'python2'
#     player2 = Popen([cmd2, player2Str, str(player2_id)], shell=True, stdout=PIPE, stdin=PIPE)
# elif player2_dir[-2] == 'cpp':
#     cmd2 = 'g++'
#     dir = os.getcwd()
#     # os.chdir('/'.join(player1_dir[:-1]))
#     player2 = Popen([cmd2, player2Str, '-o', player2_dir[-1].split('.')[0] + '.exe'], shell=True, stdout=PIPE, stdin=PIPE)
#     # os.chdir(dir)
#     player2.communicate()
#     player2 = Popen([player2_dir[-1].split('.')[0] + '.exe', str(player2_id)], shell=True, stdout=PIPE, stdin=PIPE)
# else:
#     player2 = Popen([cmd2, player2Str, str(player2_id)], shell=True, stdout=PIPE, stdin=PIPE)
#
# interval = 0.2
#
#
# def myPrint(player, line):
#     player.stdin.write(bytes(str(line) + "\n", "UTF-8"))
#     player.stdin.flush()
#
#
# def print_map(player, player_id, game_map):
#     myPrint(player, "turn")
#     myPrint(player, len(game_map.nodes))
#     for i, node in enumerate(game_map.nodes):
#         myPrint(player, node.id)
#         myPrint(player, node.ownerID)
#         myPrint(player, node.position[0])
#         myPrint(player, node.position[1])
#         myPrint(player, node.factor)
#         myPrint(player, node.soldier_count)
#         # myPrint(player, node.soldier_count if node.ownerID == player_id else -1)
#
#
# def read_decision(player):
#     result = player.stdout.readline().decode('UTF-8').replace("\r\n", "").split(' ')
#     result = list(map(int, result))
#     print("result is : ", result, player)
#     return result
#     #
#     #
#     #
#     #
#
#
# def get_decisions(game_map, event_queue):
#     timer = int(round(time.time() * 1000))
#     for node in game_map.nodes:
#         print(node.soldier_count, end='\t')
#     print_map(player1, player1_id, game_map)
#     print_map(player2, player2_id, game_map)
#     p1_decision = read_decision(player1)
#     p2_decision = read_decision(player2)
#     print(p1_decision, p2_decision)
#     # player1_map = copy.deepcopy(game_map)
#     # player2_map = copy.deepcopy(game_map)
#     # p1_decision = player1.decide(player1_map, 1)
#     # p2_decision = player2.decide(player2_map, 2)
#     if p1_decision is not None:
#         p1_decision = (p1_decision[0], p1_decision[1])
#         if 0 <= p1_decision[0] < len(game_map.nodes) and game_map.nodes[p1_decision[0]].ownerID == 1:
#             army = Army(1, game_map.nodes[p1_decision[0]], game_map.nodes[p1_decision[1]])
#
#             event_queue.append([army, timer, army.distance()])
#             army.source_node.march(army)
#             print("player 1 decided to attack from ", army.source_node.id, "to",
#                   army.destination_node.id, "by", army.soldier_count, "number of soldiers")
#     if p2_decision is not None:
#         p2_decision = (p2_decision[0], p2_decision[1])
#         if 0 <= p2_decision[0] < len(game_map.nodes) and game_map.nodes[p2_decision[0]].ownerID == 2:
#             army = Army(2, game_map.nodes[p2_decision[0]], game_map.nodes[p2_decision[1]])
#
#             event_queue.append([army, timer, army.distance()])
#             army.source_node.march(army)
#             print("player 2 decided to attack from ", army.source_node.id, "to",
#                   army.destination_node.id, "by", army.soldier_count, "number of soldiers")
#
#
# def main():
#     game_map = Map()
#     game_map.generate_default_map()
#     player_map = copy.deepcopy(game_map)
#     event_queue = []
#     # thread = threading.Thread(target=get_decisions, args=(game_map, player_map, event_queue))
#     # thread.start()
#     interval_count = 0
#     while not game_map.check_finish():
#         events = []
#         # time.sleep(interval / 10)
#         interval_count += 1
#         if interval_count == 20:
#             game_map.populate()
#             interval_count = 0
#         for item in event_queue:
#             current_time = int(round(time.time() * 1000))
#             if current_time >= item[1] + item[2]:
#                 events.append(item[0])
#                 event_queue.remove(item)
#         if len(events) != 0:
#             game_map.do_events(events, logFile, t0)
#
#         if game_map.check_finish():
#             break
#         if interval_count % 10 == 0:
#             get_decisions(game_map, event_queue)
#     # thread.join()
#     # player1.terminate()
#     # player2.terminate()
#     myPrint(player1, "shutdown")
#     myPrint(player2, "shutdown")
#     print("<------------------------- game has finished ------------------------->")
#     print("The winner is", game_map.nodes[0].ownerID)
#
#
# if __name__ == "__main__":
#     main()


import copy
import datetime
import os
import sys
import time
from subprocess import Popen, PIPE

os.chdir("..")
sys.path.append(os.path.join(os.getcwd()))
os.chdir("Server")
print('\n'.join(sys.path))

from Models.Army import Army
from Models.Map import Map

# f = open("demofile.txt", "w")
# f.write("Now the file has one more line!")
# f.write(str(sys.argv))
# f.close()

player1Str = sys.argv[1]
player2Str = sys.argv[2]
player1_id = 1
player2_id = 2

player1_dir = player1Str.split('/')
player2_dir = player2Str.split('/')

############### hypo: python2 is python 2.7 in cmd

cmd1 = 'python'
cmd2 = 'python'
if player1_dir[-2] == 'python2':
    cmd1 = 'python2'
    player1 = Popen([cmd1, player1Str, str(player1_id)], shell=True, stdout=PIPE, stdin=PIPE)
elif player1_dir[-2] == 'cpp':
    cmd1 = 'g++'
    dir = os.getcwd()
    # os.chdir('/'.join(player1_dir[:-1]))
    player1 = Popen([cmd1, player1Str, '-o', player1_dir[-1].split('.')[0] + '.exe'], shell=True, stdout=PIPE, stdin=PIPE)
    # os.chdir(dir)
    player1.communicate()
    player1 = Popen([player1_dir[-1].split('.')[0] + '.exe', str(player1_id)], shell=True, stdout=PIPE, stdin=PIPE)
else:
    player1 = Popen([cmd1, player1Str, str(player1_id)], shell=True, stdout=PIPE, stdin=PIPE)

if player2_dir[-2] == 'python2':
    cmd2 = 'python2'
    player2 = Popen([cmd2, player2Str, str(player2_id)], shell=True, stdout=PIPE, stdin=PIPE)
elif player2_dir[-2] == 'cpp':
    cmd2 = 'g++'
    dir = os.getcwd()
    # os.chdir('/'.join(player1_dir[:-1]))
    player2 = Popen([cmd2, player2Str, '-o', player2_dir[-1].split('.')[0] + '.exe'], shell=True, stdout=PIPE, stdin=PIPE)
    # os.chdir(dir)
    player2.communicate()
    player2 = Popen([player2_dir[-1].split('.')[0] + '.exe', str(player2_id)], shell=True, stdout=PIPE, stdin=PIPE)
else:
    player2 = Popen([cmd2, player2Str, str(player2_id)], shell=True, stdout=PIPE, stdin=PIPE)

interval = 0.2


def myPrint(player, line):
    player.stdin.write(bytes(str(line) + "\n", "UTF-8"))
    player.stdin.flush()


def print_map(player, player_id, game_map):
    myPrint(player, "turn")
    myPrint(player, len(game_map.nodes))
    for i, node in enumerate(game_map.nodes):
        myPrint(player, node.id)
        myPrint(player, node.ownerID)
        myPrint(player, node.position[0])
        myPrint(player, node.position[1])
        myPrint(player, node.factor)
        myPrint(player, node.soldier_count)
        # myPrint(player, node.soldier_count if node.ownerID == player_id else -1)


def read_decision(player):
    result = player.stdout.readline().decode('UTF-8').replace("\r\n", "").split(' ')
    result = list(map(int, result))
    return result
    #
    #
    #
    #


def get_decisions(game_map, event_queue, logFile, t0):
    timer = int(round(time.time() * 1000))
    #for node in game_map.nodes:
    #    print(node.soldier_count, end='\t')
    print_map(player1, player1_id, game_map)
    print_map(player2, player2_id, game_map)
    p1_decision = read_decision(player1)
    p2_decision = read_decision(player2)
    #print(p1_decision, p2_decision)
    # player1_map = copy.deepcopy(game_map)
    # player2_map = copy.deepcopy(game_map)
    # p1_decision = player1.decide(player1_map, 1)
    # p2_decision = player2.decide(player2_map, 2)
    if p1_decision is not None:
        p1_decision = (p1_decision[0], p1_decision[1])
        if 0 <= p1_decision[0] < len(game_map.nodes) and game_map.nodes[p1_decision[0]].ownerID == 1:
            army = Army(1, game_map.nodes[p1_decision[0]], game_map.nodes[p1_decision[1]])

            event_queue.append([army, timer, army.distance()])
            army.source_node.march(army)

            logFile.write(str(timer-t0) + ':started_attacking ' + str(army.source_node.id) + ',' +
                          str(army.source_node.soldier_count) + ',' + str(army.source_node.ownerID) +
                          ',' + str(army.destination_node.id) + ',' + str(army.destination_node.soldier_count) +
                          ',' + str(army.destination_node.ownerID) + '\n')

    if p2_decision is not None:
        p2_decision = (p2_decision[0], p2_decision[1])
        if 0 <= p2_decision[0] < len(game_map.nodes) and game_map.nodes[p2_decision[0]].ownerID == 2:
            army = Army(2, game_map.nodes[p2_decision[0]], game_map.nodes[p2_decision[1]])

            event_queue.append([army, timer, army.distance()])
            army.source_node.march(army)

            logFile.write(str(timer-t0) + ':started_attacking ' + str(army.source_node.id) + ',' +
                          str(army.source_node.soldier_count) + ',' + str(army.source_node.ownerID) +
                          ',' + str(army.destination_node.id) + ',' + str(army.destination_node.soldier_count) +
                          ',' + str(army.destination_node.ownerID) + '\n')


def main():
    logFile = open('log.txt', "w")
    logFile.write('0:-gamestart-\n')
    t0 = int(time.time() * 1000)
    game_map = Map()
    game_map.generate_default_map()
    player_map = copy.deepcopy(game_map)
    event_queue = []
    # thread = threading.Thread(target=get_decisions, args=(game_map, player_map, event_queue))
    # thread.start()
    interval_count = 0
    while not game_map.check_finish():
        events = []
        # time.sleep(interval / 10)
        interval_count += 1
        if interval_count == 20:
            game_map.populate(logFile, t0)
            interval_count = 0
        for item in event_queue:
            current_time = int(round(time.time() * 1000))
            if current_time >= item[1] + item[2]:
                events.append(item[0])
                event_queue.remove(item)
        if len(events) != 0:
            game_map.do_events(events, logFile, t0)

        if game_map.check_finish():
            break
        if interval_count % 10 == 0:
            get_decisions(game_map, event_queue, logFile, t0)
    # thread.join()
    # player1.terminate()
    # player2.terminate()
    myPrint(player1, "shutdown")
    myPrint(player2, "shutdown")
    # print("<------------------------- game has finished ------------------------->")
    t = int(time.time() * 1000)
    logFile.write(str(t - t0) + ":winner_is " + str(game_map.nodes[0].ownerID) + '\n')
    logFile.write(str(t - t0) + "-endgame-\n")
    print("winner is", str(game_map.nodes[0].ownerID))
    logFile.close()

if __name__ == "__main__":
    main()
