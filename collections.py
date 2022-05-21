# # Lists are collections of items(can be no's, strings, another list as well etc..)
# # Lists store anything, store anytype and ordering matters
# names = ['uday', 'bunny', 'rishi', '123' , ['uday' , 'bunny', 'rishi']]
# scores = []
# scores.append(98) # add new item to the end for above variable value
# scores.append(99)

# print(names)
# print(scores)
# print(scores[1]) # Collections are zero-indexed

# # ----------------

# # arrays are also collection of numeric data types, must all be the same type
# from array import arr
# scores = arr('d')
# scores.append(97)
# scores.append(98)
# print(scores)
# print(scores[1])

# #---------------------------------------
# #common operations

# names = ['uday', 'bunny']
# print(len(names)) # get the number of items
# names.insert(0, 'rishi') # insert before the index value 
# print(names)
# names.sort() # give alphabetical order, low to high values for numbers.
# print(names)


# #------------------------------
# # retrieving ranges

# names = ['uday', 'bunny', 'rishi', 'kavya', 'puja']
# presenters = names[1:3] # start and end with index # we can give [:4]
# # 0 start with opening [ and the numbers will be sitting on the , and ends with
# #final value on closing ]

# print(names)
# print(presenters)


# #------------------------------------------------------
# # Dictionaries
# person = {'first': 'udaykumar'} # key value pairs -- notice the curly brackets
# person['last'] = 'mannepalli' # to add a new key value pair to dictionary

# print(person)
# print(person['first'])

# # Dictionaries - key/value pairs and storage order not guaranteed
# # Lists - Zero-based index and storage order guaranteed

# uday = {}
# uday['first'] = 'Udaykumar'
# uday['last'] = 'Mannepalli'

# bunny  = {}
# bunny ['first'] = 'Veedeeth'
# bunny ['last'] = 'Kuntamukkala'

# people = []
# people.append(uday)
# people.append(bunny)
# people.append({'first' : 'Rishi', 'last': 'Bodepudi'
# })

# print(people)