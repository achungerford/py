""" Sometimes it is useful to make function arguments optional.

Give the argument an empty default value and
move it to the end of the list of parameters.
"""

def format_name(first_name, last_name, middle_name = ''):
    """Return a properly formatted name. Middle name optional."""

    # making middle_name optional
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    
    # formatting the full_name and returning it
    return full_name.title()

person = format_name('matt', 'damon')
print(person)

person2 = format_name('matt', 'damon', 'loser')
print(person2)