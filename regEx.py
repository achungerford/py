""" Script will search text for phone number
in pattern xxx-xxx-xxx using regular expressions.
"""
# import regular expressions module
import re

# phoneNumRegex variable stores a Regex object returned from compile method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# search() method looks for a match object, stores in mo
mo = phoneNumRegex.search('My number is 987-654-3210.')

# group() method on match object returns the
# matched text pattern from the searched string
print('Phone number found: ' + mo.group())

# using Regex shortcuts
phoneNumRegex2 = re.compile(r'\d{3}-\d{3}-\d{4}')
mo2 = phoneNumRegex2.search('My number is 012-345-6789.')
print('Phone number two: ' + mo2.group())