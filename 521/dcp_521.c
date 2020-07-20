#include<stdio.h>
#include<stdbool.h>
#include<string.h>
void printZigzag(char arr[],int k){
	if(k==1){
		printf("%s",arr);
		return;
	}
	int len=strlen(arr);
	bool down; //It will be true if we are moving down in row and false otherwise
	int row=0;
	char new_arr[len][len]; //a new 2d character array is declared to store the values of the string
	for(int i=0;i<len;i++){
		
		new_arr[row][i]=arr[i]; //stores the value in a string new_arr
		//Now, we will check the value of the integer row. If its value is less than k-1, means we are in the last row, then we have to move up and down will be false
		//If the value of row is 0, it means we are in the first row and we have to move down. So, down will be true
		if(row==k-1){
			down=false;
		}
		else if(row==0){
			down=true;
		}// If down is true, then we will keep increasing the row integer and if down is false, then we have to move upwards , thus we will keep decreasing the value of row.
		if(down==false){
			row--;
		}
		else{
			row++;
		}
	}
	for(int i=0;i<k;i++){
		for(int j=0;j<len;j++){
			printf("%c",new_arr[i][j]);
		}
	}
}

int main(){
	char str[]="thisiszigzag";
	int k=4;
	printZigzag(str,k);
	return 0;
}
