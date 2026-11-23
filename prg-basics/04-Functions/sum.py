def f(x, y):
    numbers = []
    for x in range(x, y + 1): 
        if x % 2 == 0 and x % 3 == 0 and x % 4 != 0:
            numbers.append(x)

    return sum(numbers)

if __name__ == "__main__": 
    print(f(1, 20)) 
    print(f(10, 30))

        

