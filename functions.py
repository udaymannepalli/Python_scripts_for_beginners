def count_even_odd(lst):
    even = 0
    odd = 0 

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

lst = [10,11,12,13,14,25,55]
even, odd = count_even_odd(lst)
print('Even : {} and Odd : {}'.format(even,odd))
