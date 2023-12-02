#largest/smallest no in a list/tuple
def fn(x):
    max_value=max(x)
    print("The largest number : ",max_value)
    min_value=min(x)
    print("The smallest number : ",min_value)

print("Use [] for LIST and ()for TUPLE ")
var=eval(input("Enter the list/tuple : "))
fn(var)

    
