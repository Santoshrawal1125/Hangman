print("Welcome to the tip calculator")

bill=float(input("what was the total bill?"))

spilt=int(input("how many people do you want to split the bill into?"))

tip=int(input("what percentage tip would you like to give?"))

bill_with_tip= (tip/100 * bill) + bill

print("Each person should pay ", bill_with_tip/spilt)