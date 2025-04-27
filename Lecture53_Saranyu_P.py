def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

price = float(input("Please show me your money : "))
print(vatCalculate(price))