def hcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
num1 = 12
num2 = 12
print('The hcf is ', hcf(num1,num2))