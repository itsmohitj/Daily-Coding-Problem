# Problem 526

You are given a string of length N and a parameter k. The string can be manipulated by taking one of the first k letters and moving it to the end.
<br/>
<br/>
Write a program to determine the lexicographically smallest string that can be created after an unlimited number of moves.
<br/>
<br/>
For example, suppose we are given the string **daily** and k = 1. The best we can create in this case is **ailyd**.

This problem was asked by Yahoo.

# Solution

- Take a new string X and initialize it to empty string i.e. X=" "
- Find the smallest character in the first k characters in the string str.
- Delete the smallest character found.
- Append the smallest character found to the new string X.
- Repeat the above steps till the string is empty.
