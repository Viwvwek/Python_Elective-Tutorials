"""
    "Return of investment"(ROI) calculator
    
    It  return ((current_value - investment_amount) / investment_amount) * 100
    reads both:
        current_value and investment_amount
"""
#reading the current_value
current_value = input("Enter the Current_Value:")
#reading the investment_amount
investment_amount = input("Enter the Investment_Amount:")
#calculating the ROI  
roi = ((float(current_value)-float(investment_amount))/float(investment_amount))*100
print("ROI is:", roi)