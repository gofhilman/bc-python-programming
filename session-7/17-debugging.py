# We will fix the following code with python debugging feature

# The sum of consecutive numbers exercise
# Source: https://programming-25.mooc.fi/part-3/1-loops-with-conditions

# Please write a program which asks the user to type in a limit. 
# The program then calculates the sum of consecutive 
# numbers (1 + 2 + 3 + ...) until the sum is at least equal 
# to the limit set by the user. In addition to the result 
# it should also print out the calculation performed.

limit = int(input("Limit: "))
i = 1
number_sum = 0
string_sum = ""
while number_sum <= limit:
    string_sum += str(i)
    number_sum += i
    i += 1
    if number_sum <= limit:
        string_sum += " + "

print(f"The consecutive sum: {string_sum} = {number_sum}")
