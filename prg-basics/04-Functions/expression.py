def f(expression): 
    total, sign = 0, 1
    for c in expression: 
        
        if c == "+": 
            sign = 1
        
        elif c == "-": 
            sign = -1
        
        else: 
            total += sign * int(c)
        
    return total





if __name__ == "__main__": 
    print(f("2+3"))