#program to check if a string is palindrome





def check_palindrome(value):
    
    if value == value[::-1] :
        print('the string is palindrome')
    else:
        print('the string is not palindrome')  



value = input('enter the string to check whether it is palindrome or not: ')
check_palindrome(value)          