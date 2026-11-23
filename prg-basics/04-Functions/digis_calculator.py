def f(password): 
    
    seen = {}
    # base case 
    if len(password) < 6: 
        return False 
    
    for x in password: 
        if x in seen: 
            seen[x] += 1
        else: 
            seen[x] = 1
    
    for c in seen.values(): 
        if c != 1: 
            return False
    
    return True 
        

if __name__ == "__main__": 
    print(f("ax15"))      # False
    print(f("book123"))   # False
    print(f("A2water3"))  # True
    print(f("qwerty"))    # True
    print(f(""))          # False