#include <iostream>
#include <string>
#include <time.h>
#include <fstream>

using namespace std;
const int MAP_DETAIL_LENGTH = 7;

int** map = nullptr;
int nodes_count = 0;

void read_map()
{
	cin >> nodes_count;
	bool must_alloc = false;
	
	if (map == nullptr)
	{
		map = new int*[nodes_count];
		must_alloc = true;
	}
	for (int i = 0; i < nodes_count; i++)
	{
		if (must_alloc)
			map[i] = new int[MAP_DETAIL_LENGTH];
		for (int j = 0; j < MAP_DETAIL_LENGTH; j++)
		{
			cin >> map[i][j];
		}
	}
}

int main(int argc, char** argv)
{
	srand(time(NULL));

	int client_id = 0;
	if (argc > 1)
		 client_id = atoi(argv[1]);

	string input = "";
	while (input != "shutdown")
	{

		cin >> input;

		if (input == "turn")
		{
			read_map();
		}
		int source_id = -1, dest_id = -1;

		// decide whether to attack or not. 
		// if you decided to attack, place destination id and source id in two variables dest_id and source_id
		// attack will be lunched in order : source -> dest
		// if you decided not to attack set source_id to be -1
		// write your code here ....
		
		int p = rand() % 10;
		if (p < 1)
		{
			do
			{
				source_id = rand() % nodes_count;
			} while (map[source_id][1] != client_id);

			dest_id = rand() % nodes_count;
		}
		
		// write your code here ....
		
		cout << source_id << " " << dest_id << endl;
	}
}