#include<stdio.h>

int maxSubarraySum(int arr[], int size){
	int overallSum=0;
	int maxTillNow=0;
	for(int i=0; i<size; i++){
		maxTillNow = maxTillNow + arr[i];
		if(maxTillNow < 0){
			maxTillNow=0;
		}
		else if (overallSum < maxTillNow){
			overallSum=maxTillNow;
		}
	}
	return overallSum;
}

int main(){
	int arr1[]={34,-50,42,14,-5,86};
	int arr2[]={-5,-1,-8,-9};
	printf("%d\n",maxSubarraySum(arr1,6));
	printf("%d\n",maxSubarraySum(arr2,4));
	return 0;
}
