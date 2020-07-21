#include<stdio.h>

int plusXorPairs(int m, int n){
	int count=0;
	for(int i=1;i<m;i++){
		int a=i;
		int b=m-a;
		if((a^b)==n){
			printf("%d\n",a^b);
			count++;
		}
	}
	return count;
}

int main(){
	printf("%d",plusXorPairs(11,11));
	return 0;
}
