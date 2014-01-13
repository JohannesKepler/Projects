"""
Check if Palindrome - Checks if the string entered
by the user is a palindrome. That is that it reads
the same forwards as backwards like "racecar"
"""

string = raw_input('Enter a string: ')
new_string = ''.join(e for e in string if e.isalnum())
new_string = new_string.lower()

if new_string == new_string[::-1]:
    print '%s is a palindrome' % string
else:
    print '%s is not a palindrome' % string
