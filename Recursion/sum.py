def sums(lower,upper):
    if (lower <= upper):
        return lower + sums(lower+1,upper)
    else:
        return 0

print(sums(10,20))
