#Modules - a file containing Python definitions and statements. 
# The file name is the module name with the suffix .py added. 
# Within a module, the module’s name (as a string) is available as the value of the global variable __name__.
# To use a module, you import it, which gives you access to the definitions (functions, variables, etc.) in that module.
# Encourages code reuse and organization.

# import - used to import a module into the current namespace.
# from - used to import specific attributes from a module into the current namespace.
# as - used to give a module or an attribute a different name in the current namespace.

import random as r
# heads_counter = 0
# tails_counter = 0
# for i in range(100):

#     a = choice(["heads","tails"])
#     if a == "heads":
#         print(a)
#         heads_counter += 1
#     else:
#         print(a)
#         tails_counter +=1
#     i += 1
# print(heads_counter, tails_counter)

# random.choice - returns a random element from a non-empty sequence.
# random.randint - returns a random integer N such that a <= N <= b.

'''
number = r.randint(1,10)
print(number)
'''
# random.shuffle - shuffles the sequence x in place.
cards = ['jack', 'queen', 'king']
r.shuffle(cards)
for card in cards:
    print(card)


