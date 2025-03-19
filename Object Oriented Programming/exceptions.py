try:
    x = int(input("Enter the numerator : "))
    y = int(input("Enter the denominator : "))
    q = x/y

except ZeroDivisionError:
        print("Zero Error")
except ValueError:
        print("Value Error")
else:
    print("Quotient : ", q)
finally:
    print("Computation Done!!!")
