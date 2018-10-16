//#include <iostream>
//#include <string>
//
//using namespace std;
//
//int main(int argc, char** argv)
//{
//	int client_id = atoi(argv[1]);
//	cout << "client " << client_id << " started";
//	cout.flush();
//	/*
//	string input, id;
//	while (input != "shutdown")
//	{
//		getline(cin, input);
//		cout << "client " << client_id << " got a messege : " << input << endl;
//	}
//	*/
//}

#include <iostream>
#include <string>
using namespace std;

int main(int argc, char** argv){
    int a = atoi(argv[1]);
    for( int ii=0; ii<10; ++ii ){
        int input;
        cin >> input;
        cout << "client " << a << " : " << input << endl;
        cout.flush();
    }
}
