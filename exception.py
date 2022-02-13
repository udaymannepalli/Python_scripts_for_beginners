try:
    # code that may cause exception
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    
    result = numerator / denominator
    print(result)
    
except:
    # code to run when exception occurs
    print("Denominator cannot be 0. Please try again.")
print("program ends")

#ZeroDivisionError after except