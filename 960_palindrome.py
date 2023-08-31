def is_palindrome(s):
    s= s.replace(" ","").lower()
    return s == s[::-1]

user_input_string = input("enter a word")
if is_palindrome(user_input_string):
    print("it is palindrome")
else:
    print("word is not palindrome")