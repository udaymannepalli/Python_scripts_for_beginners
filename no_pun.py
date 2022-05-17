punctuations = '--()@'
my_str = input('enter the string: ')

no_punc = ""
 
for i in my_str:
    if i not in punctuations:
        no_punc = no_punc + i
    
print(no_punc)





