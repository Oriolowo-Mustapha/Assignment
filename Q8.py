conver = ["Enter 1 to convert to Fahrenheit", "Enter 2 to convert to Kelvin"]
for a in conver:
    print(a)

numr= int(input("Enter any operation to be performed: "))
if numr == 1:
    num = int(input("Enter number to be converted: "))
    formula = num * 1.8 + 32
    print(formula)
elif numr == 2:
    num = int(input("Enter number to be converted: "))
    fomula2 = num + 273.15
    print(fomula2)