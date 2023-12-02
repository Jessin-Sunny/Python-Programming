temperature=eval(input("Enter the magnitude of temperature : "))
unit=input("Enter the unit of temperature : ")
if(unit=="Fahrenheit" or unit=="fahrenheit"):
    C=(temperature-32)*5/9
    print("The equivalent temperature in Celsius is",C)
if(unit=="Celsius" or unit=="celsius"):
    F=temperature*9/5+32
    print("The equivalent temperature in Fahrenheit is",F)
