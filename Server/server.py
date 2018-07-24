import copy
import sys
import threading
import time

from Models.Map import Map

player1 = __import__(sys.argv[1][: -3])
player2 = __import__(sys.argv[2][: -3])

interval = 0.2


def get_decisions(game_map, player_map, event_queue):
    while not game_map.check_finish():
        time.sleep(interval)
        timer = int(round(time.time() * 1000))
        p1_decision = player1.decide(player_map)
        p2_decision = player2.decide(player_map)
        if p1_decision is not None:
            event_queue.append([p1_decision, timer, p1_decision.distance()])
        if p2_decision is not None:
            event_queue.append([p2_decision, timer, p2_decision.distance()])


def main():
    game_map = Map()
    game_map.generate_default_map()
    player_map = copy.deepcopy(game_map)
    event_queue = []
    events = []
    thread = threading.Thread(target=get_decisions, args=(game_map, player_map, event_queue))
    thread.start()
    while not game_map.check_finish():
        time.sleep(interval / 10)
        for item in event_queue:
            current_time = int(round(time.time() * 1000))
            if current_time >= time + item[2]:
                events.append(item[0])
                event_queue.remove(item)
        game_map.do_events(events)
    thread.join()


if __name__ == "__main__":
    main()
