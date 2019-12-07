""" Functions don't have to display output directly.

The return statement takes a value from inside a function
and sends it back to the line that called the function.
"""

def format_name(first_name, last_name):
    """Return a full name formatted correctly."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# calling format_name
person = format_name('brad', 'pitt')
print(person)

person = format_name('matt', 'damon')
print(person)