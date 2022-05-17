
def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

lst = [11,13,1,2,4,14,15,2,55]
even, odd = count(lst)

print(odd)
print(even)

print("Even : {} and Odd : {}".format(even,odd))