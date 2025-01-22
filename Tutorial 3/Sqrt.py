"""
    To find the Square_Root of an Inout Number
    using the math function 
    


"""
#Importing the header file for impporting the function SQRT
import math

#Taking the input from the user
number = input("Enter the number to find the Square_Root ")
#Typecasting to perform the function
"""
    Since the reading input is a String,
    We need to convert it into a real number
    for performing the operations

"""
 
number = int(number)
#printing the Square_Root of the function 
print(math.sqrt(number))