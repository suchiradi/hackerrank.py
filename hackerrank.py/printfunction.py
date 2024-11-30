#Print the list of integers from 1 through n as a string, without spaces.
#this program uses print function
n = int(input())
if 1<=n<=150:
        for i in range(1,n+1):
            print(i,end='')
            