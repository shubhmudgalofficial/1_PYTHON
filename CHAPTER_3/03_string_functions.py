name="aeroplane is new" 
"""
This script demonstrates various string functions in Python.

Functions:
- len(): Returns the length of the string.
- endswith(): Checks if the string ends with the specified suffix.
- startswith(): Checks if the string starts with the specified prefix.
- capitalize(): Capitalizes the first character of the string.
- upper(): Converts all characters in the string to uppercase.

Variables:
- name (str): A sample string to demonstrate the functions.

Examples:
- len(name): Returns the length of the string 'name'.
- len("akjhdkjuahkjahsd"): Returns the length of the given string.
- name.endswith("new"): Checks if 'name' ends with the substring "new".
- name.startswith("A"): Checks if 'name' starts with the character "A".
- name.startswith("a"): Checks if 'name' starts with the character "a".
- name.capitalize(): Capitalizes the first character of 'name'.
- name.upper(): Converts all characters in 'name' to uppercase.

"""
print(len(name)) #9 len function
print(len("akjhdkjuahkjahsd"))
print(name.endswith("new"))
print(name.startswith("A"))
print(name.startswith("a")) #case sensitive
print(name.capitalize())
print(name.upper())
print(name.lower()) # Converts all characters in the string to lowercase
print(name.find("plane")) # Returns the lowest index of the substring if found, otherwise -1
print(name.replace("new", "old")) # Replaces all occurrences of a substring with another substring
print(name.split()) # Splits the string into a list of substrings based on whitespace
print(name.strip()) # Removes any leading and trailing whitespace characters
print(name.replace("aeroplane","helicopter")) # Replaces all occurrences of a substring with another substring
s="kjfiudshfiojcjkzn iujshjf9iofiejfiwfjwioefjewiopfjp0eokfpoefjkef"
print(s.find("j")) 
print(s.split())
