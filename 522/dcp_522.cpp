#include<iostream>
using namespace std; 

void allOccurrence(string str, string substring){ 
    for (int i = 0; i < str.length(); i++) { 
        if (str.substr(i, substring.length()) == substring) { //substr is a predefined function which takes two arguments, first is the position from where to start and second is the length of the substring
	       // It returns a new string which is substring of the other string
		// for example if string str is "example", then str.substr(2,3) will return "amp".
            cout << i << " "; 
        } 
    } 
} 

int main()
{
    string str ="abracadabra";
    string substring = "abr";
    allOccurrence(str, substring);
    return 0;
}
