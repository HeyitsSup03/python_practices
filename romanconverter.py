def int_to_roman(num):
    if num < 1 or num > 10:
        return 'invalid input. Do enter a number that is in between 1 and 10'
    roman_numbers = {1:'I',2: 'II',3:'III',4: 'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X'}
    return roman_numbers[num]
try:
    user_input = int(input("enter a number that is in between 1 and 10"))
    print(f"{user_input} = {int_to_roman(user_input)}")
except ValueError:
    print("invalid input. Do enter a number that is in between 1 and 10")