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

# Complexity O(2n)

# Solution general idea:
# use the given string to generate another string to return.
# for the given string, read one by one each element
# if the element is equal to ".", concatenate the other string with "[.]"
# else, concatenate the other string with the readed character

def foo(input):
    # defines the output empty string
    output = ""

    # search for "."
    for i in range(len(input)):
        # if finds it, concatenate "[.]" with the output string
        if input[i] == ".":
            output = output + "[.]"
        
        # else, concatenate the original element with the output string
        else:
            output = output + input[i]

    return output






# tests
ip = "255.100.50.0"
print(ip)
print(foo(ip))