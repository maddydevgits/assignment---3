def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            next_num = fib_seq[-1] + fib_seq[-2]
            fib_seq.append(next_num)
        return fib_seq

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_nums = fibonacci(n)

print("Fibonacci sequence:")
for num in fib_nums:
    print(num, end=" ")
