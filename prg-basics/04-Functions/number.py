def f(number): 
    number = str(number)
    outcome = 0 
    seen = {}
    
    for x in number:
        if x in seen:
            seen[x] += 1
        else:
            seen[x] = 1

    for digit, count in seen.items():
        if count >= 2:
            outcome = count * int(digit)
    
    return outcome

if __name__ == "__main__": 
    print(f(1027))