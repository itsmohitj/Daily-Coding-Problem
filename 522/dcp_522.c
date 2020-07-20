#include<stdio.h>
#include<stdbool.h>
#include<string.h>

void allOccurrence(char str[], char substr[]){
	int lenstr=strlen(str);
	int lensubstr=strlen(substr);
	int j=0;
	int current_len=0;
	for(int i=0;i<lenstr;i++){
		if((str[i]==substr[j]) && current_len<lensubstr){
			if(current_len==lensubstr-1){
				printf("%d",i);
			}
			current_len++;
			j++;
		}
		else{
			current_len=0;
			j=0;
		}
	}
}

int main(){
	char s1[]="abracadabra";
	char s2[]="abra";
	allOccurrence(s1,s2);
	return 0;
}

