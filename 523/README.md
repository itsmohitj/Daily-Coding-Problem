Given integers M and N, write a program that counts how many positive integer pairs (a, b) satisfy the following conditions:
<br/>
1. a + b = M
2. a xor b = N
<br/>
This problem was asked by Jane Street.

Note: This solution counts a single pair two times i.e if (a,b) is a pair, then it is also counting (b,a) as a solution pair.
<br/> If we want to count a pair only once, We just have to iterate upto m/2.
