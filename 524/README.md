# Problem 524

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
<br/>
<br/>
For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
<br/>
<br/>
Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
<br/>
<br/>
Do this in O(N) time.
<br/>
<br/>

# Solution

This can be done by Kadane's Algorithm

1. Initialize a variable overallMax=0 which keep tracks of maximum sum contiguous segment among all segments.
2. Initialize another variable maxTillNow=0 which will contain sum till now for current segment
3. Loop over every element of the array 
	1. update maxTillNow = maxTillNow + array[i]
	2. check if maxTillNow is less than 0, if it is , then assign a value of zero to it, i.e. make maxTillNow=0.
	3. Otherwise, Check if maxTillNow is greater than overallMax, if it is, then update the value of overallMax to maxTillNow.
4. finally return overallMax

