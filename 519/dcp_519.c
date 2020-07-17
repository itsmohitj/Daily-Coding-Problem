#include<stdio.h>
#include<stdint.h>
#include<inttypes.h>
int32_t solution(int32_t x, int32_t y, int32_t b){
	b=-b;
	return(x & b) | (y & ~b);
}
int main(){
	int32_t x=solution(111111111,13233432,0);
	printf("%" PRIi8 "\n ",x);
	return 0;
}

