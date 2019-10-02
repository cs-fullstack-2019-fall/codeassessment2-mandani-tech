# ### Problem 4
# Write a program that allows users to compare words by their length. Implement a function called chk_strings that accepts 2 strings entered by the user and compares them by length
# The function should return true if the first string parameter has more characters (i.e. longer) than the second string passed into the function, otherwise, the function should return false.
# DO NOT print the result in the function, print the result using the return value provided by the function. 

# Example Input/Output:
# ```
# Enter the first string: BIRD
# Enter the second string: COW

# BIRD is longer than COW
# ```
# KEY: Achieved result *but* 'DO NOT print the result in the function, print the result using the return value provided by the function. '
# Function called chk_strings that accepts 2 strings entered by the user and compares them by length
def compareString() :
    string1=input("Please enter first string: ")
    string2=input("Please enter second string: ")
    if len(string1)>len(string2):
        return f'{string1} is longer than {string2}'
    else:
        return f'{string2} is longer than {string1}'

 # Printed the result using the return value provided by the function
print(compareString())
