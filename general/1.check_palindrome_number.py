# Create by Dien Dang https://www.facebook.com/diendang.01

"""
1 - Check a number is palindrome
A palindromic number or numeral palindrome is a number that remains the same when its digits are reversed. Like 16461,
for example, it is "symmetrical". The term palindromic is derived from palindrome, which refers to a word
 (such as rotor or racecar) whose spelling is unchanged when its letters are reversed.
"""

"""
Function: is_palindrome
Parameter: Integer: Number
Output: Boolean: A number is a palindrome or not
"""


def is_palindrome(number:int):
    return str(number) == str(number)[::-1]

"""
Test Function
"""
print("14641 is palindrome number " + is_palindrome(14641)) # Should return True
print("22222 is palindrome number " + is_palindrome(14641)) # Should return True
print("13531 is palindrome number " + is_palindrome(14641)) # Should return True
print("14600 is palindrome number " + is_palindrome(14641)) # Should return False
print("2 is palindrome number " + is_palindrome(14641)) # Should return True
