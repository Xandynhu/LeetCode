# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# Given a valid IP address (IPV4) returns a defanged version of that IP.
# A 'defanged' IP address replaces all "." for "[.]".

# example 1:
# input: = "1.1.1.1"
# output: "1[.]1[.]1[.]1"

# example 2:
# input: = "255.100.50.0"
# output: "255[.]100[.]50[.]0"

# Complexity O(n)

# Solution general idea:
# use the given string to update itself and return.
# for the given string, read one by one each element
# if the element is equal to ".", replace "[.]"

def foo(input):
    # replace all "." for "[.]"
    input = input.replace(".", "[.]")        

    return input






# Tests
ip = "255.100.50.0"
print(ip)
print(foo(ip))