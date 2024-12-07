n = int(input())  #taking n values
t = tuple(map(int, input().split())) #taking n values and storing them in tuple t
print(hash(t))  #hashing the elements of the tuple