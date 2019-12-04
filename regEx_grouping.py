""" This demonstrates grouping regular expressions using
parenheses and searching the groups for patterns.
"""

import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 012-345-6789.')

# demonstrate grouping
print('Phone number: 012-345-6789\n')
print('mo.group():  ' + mo.group())
print('mo.group(0): ' + mo.group(0))
print('mo.group(1): ' + mo.group(1))
print('mo.group(2): ' + mo.group(2))
