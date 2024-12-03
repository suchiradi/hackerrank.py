n = int(input())  #taking the total number of inputs
scores = list(map(int, input().split()))  # taking the values

unique_scores = list(set(scores))  #set() removes all the duplicates 
unique_scores.sort(reverse=True)    #reverse=True is used to print the list in reverse

runner_up_score = unique_scores[1] #calling the first index which will contain the second highest score
print(runner_up_score)