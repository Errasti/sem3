def neg_fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        yield -a

        a, b = b, a + b


result = [0]
result += list(neg_fib(8))
print(sorted(result))
