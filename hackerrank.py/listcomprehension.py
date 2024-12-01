x = int(input())
y = int(input())
z = int(input())
n = int(input())
result = [[i, j, k]
    for i in range(x + 1)   #checks if i is within the given constraint 
    for j in range(y + 1)   #checks if j is within the given constraint 
    for k in range(z + 1)   #checks if k is within the given constraint 
    if i + j + k != n  ]

print(result)