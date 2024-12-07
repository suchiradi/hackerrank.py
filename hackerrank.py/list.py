n = int(input())  #takes number of inputs
arr = []          #creating an empty list

for i in range(n):  #running a for loop through the list
    command = input().split() #taking the input from the user of which operation to perform
    operation = command[0]    #operation will first in the list 
    
    
    if operation == "insert":  
        i, e = int(command[1]), int(command[2])  # insert keyword will be in index 0 followed by the position where the value should be stored followed by the element
        arr.insert(i, e)  # i= index and e= element
    elif operation == "print":
        print(arr)   #printing the list
    elif operation == "remove":
        e = int(command[1])  #removing the first element of the list
        arr.remove(e)
    elif operation == "append":    #adding an element to the list 
        e = int(command[1])
        arr.append(e)
    elif operation == "sort":   #sorting the list in ascending order 
        arr.sort()
    elif operation == "pop":    #removing the last element of the list 
        arr.pop()
    elif operation == "reverse":   #reversing the list
        arr.reverse()

