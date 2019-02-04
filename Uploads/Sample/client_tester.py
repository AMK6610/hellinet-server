import random

MAP_DETAIL_LENGTH = 7

game_map = None

def read_map():
	nodes_count = int(input())
	
	if map == None:
		map = [[int(input()) for j in range(MAP_DETAIL_LENGTH)] for i in range(nodes_count)]
	

def main(client_id):
	inp = ''
	while inp != 'shutdown':
		inp = input()
		
		if inp == 'turn':
			read_map()
		
		source_id = -1
		dest_id = -1
		
		p = random.random()
		if p < 0.1:
			source_id = random.randint(0, len(game_map))
			while game_map[source_id][1] != client_id:
				source_id = random.randint(0, len(game_map))
			
			dest_id = random.randint(0, len(game_map))
		
		print(source_id, dest_id)

if __name__ == "__main__":
	id = 1
	main(id)