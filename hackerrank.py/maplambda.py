def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
n=int(input("enter a number : \n"))
cube = list(map(lambda a: a ** 3, fibonacci(n)))
print(cube)
