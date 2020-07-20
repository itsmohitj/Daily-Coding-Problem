#include <iostream>
#include <string>
using namespace std;

// Function to print given string in zig-zag form in k rows
void printZigZag(string str, int k)
{
	// base case
	if (k == 1){
		cout << str;
		return;
	}

	// In first row, first letter will be at position i= 0 and then next will be add i+(k-1)*2
	for (int i = 0; i < str.length(); i += (k-1)*2){
		cout << str[i];
	}	
	// To print middle rows, we have to iterate from 1 to k-1
	for (int j = 1; j < k - 1; j++){
		bool down = true;
		int i=j;
		while(i<str.length()){
			cout << str[i];
			if (down) // going down
				i += (k-j-1)*2;
			else // going up
				i += (k-1)*2 - (k-j-1)*2;

			down = !down;
		}
	}

	// In last row, first letter will be at position i=k-1 and then next will be add i+(k-1)*2
	for (int i = k - 1; i < str.length(); i += (k-1)*2)
		cout << str[i];
}

int main(){
	printZigZag("thisiszigzag",4);
	return 0;
}
