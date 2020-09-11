def lexSmallString(s, k): 
      
    # new string 
    X = "" 
  
    # Remove characters until 
    # the string is empty 
    while (len(s) > 0): 
        temp = s[0] 
  
        # Traverse to find the smallest  
        # character in the first k characters 
        i = 1
        while(i < k and i < len(s)): 
            if (s[i] < temp): 
                temp = s[i] 
  
            i += 1
          
        # append the smallest character 
        X = X + temp 
  
        # removing the lexicographically  
        # smallest character from the string 
        for i in range(k): 
            if (s[i] == temp): 
                s = s[0:i] + s[i + 1:] 
                break
          
    return X 
print(lexSmallString("daily",1))
print(lexSmallString("gaurang",3))
