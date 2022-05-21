def rec_fact(n):
    if n == 1:
        return n
    else:
        return n*rec_fact(n-1)
num = 5
if num < 0:
    print('fact does not exist for negative no')
elif num == 0:
    print('factorial of zero is 1')
else:
    print('factorial of ', num, 'is', rec_fact(num))
