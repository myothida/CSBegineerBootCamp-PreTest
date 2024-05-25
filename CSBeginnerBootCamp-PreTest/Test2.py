
input_string = input("Enter a string: ")

def count_characters(input_string):
   
    char_count = {}

   
    for char in input_string:
       
        if char in char_count:
            char_count[char] += 1
       
        else:
            char_count[char] = 1
    
    return char_count



result = count_characters(input_string)
print(result)
