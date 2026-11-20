def palindrome(text): 
    letters = []
    for c in text:
        letters.append(c.lower())
    
    left = 0 
    right = len(letters) - 1
    
    while left < right: 
        if letters[left] != letters[right]: 
            return False 
        left += 1
        right -= 1
    return True 

print(palindrome("radar")) #returns True


        