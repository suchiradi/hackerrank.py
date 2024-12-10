def mutate_string(string, position, character):
    
    return string[:position] + character + string[position + 1:]
#string[:positon]- will return the characters until 1 index before the position where is new character should be added
#position- the position/index of the string where the character should be added
#string[position+1]-will return all the characters after the index value given by the user
original_string = "abracadabra"
position = 5
character= 'k'

result = mutate_string(original_string, position, character)