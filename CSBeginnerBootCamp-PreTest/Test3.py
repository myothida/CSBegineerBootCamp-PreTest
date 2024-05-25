def is_palindrome(string):
    # Convert the string to lowercase and remove non-alphanumeric characters
    clean_string = ''.join(char for char in string.lower() if char.isalnum())

    # Reverse the clean string
    reversed_string = clean_string[::-1]

    # Check if the clean string is equal to its reverse
    return clean_string == reversed_string


print("A man a plan a canal Panama :",is_palindrome("A man a plan a canal Panama")) 
print("Hello World:",is_palindrome("Hello World")) 
print("12321:",is_palindrome("12321")) 
print("Step on no pets:",is_palindrome("Step on no pets")) 