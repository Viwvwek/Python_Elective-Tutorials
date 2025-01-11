"""
    To find the Square_Root of an Input Number
    without using the "Math" function.

    Logic:
            Sqrt(number) ===  number**0.5
            Eg;
                 Sqrt(4) ===  4**0.5
"""

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
print(number**0.5)