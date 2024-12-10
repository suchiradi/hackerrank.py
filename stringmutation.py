def mutate_string(string, position, character):  #defining a function and taking 3 arguments
                                                 #string, position(position of any value in a string)#character(any specific letter from the string)
    return string[:position] + character + string[position + 1:]  
#here, string[:position] returns the string one index before the position given by the user. character is the string
# to be added. string[position:] returns all the character of the strings after the index value which was given by the user.
original_string = "abracadabra"
position = 5
character= 'k'

result = mutate_string(original_string, position, character)  #calling the function