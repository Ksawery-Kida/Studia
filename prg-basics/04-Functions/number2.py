def f(n): 
    numbers = []
    x = 2

    while len(numbers) < n:
        is_prime = True
        for d in range(2, x):
            if x % d == 0:
                is_prime = False

        if is_prime: 
            numbers.append(x)
        x += 1

    return numbers[n - 1]

if __name__ == "__main__": 
    print(f(1))
