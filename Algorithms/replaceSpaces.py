# Write a method to replace all spaces in a string with
# '%20'. You may assume that the string has sufficient space
# at the end of the string to hold the additional characters,
# and that you are given the 'true' length of the string.

# Example:
# Input:  "Mr John Smith    "
# Output: "Mr%20John%20Smith"

input = "Mr John Smith    "

def replace_spaces( given_string ):
    buffer = ""

    for char in input:
        if len(buffer) < len(given_string):
            if char != " ":
                buffer += char
            else:
                buffer += "%20"
        else:
            break

    return buffer

print replace_spaces(input)

