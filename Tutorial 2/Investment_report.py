"""
    "Return on Investment" (ROI) Calculator
    
    It calculates ROI as:
        ((current_value - investment_amount) / investment_amount) * 100
    Reads both:
        current_value and investment_amount
"""

# Reading the current_value
current_value = input("Enter the Current Value: ")

# Reading the investment_amount
investment_amount = input("Enter the Investment Amount: ")

# Calculating the ROI
roi = ((float(current_value) - float(investment_amount)) / float(investment_amount)) * 100

# Displaying the ROI
print("ROI is: {:.2f}%".format(roi))
