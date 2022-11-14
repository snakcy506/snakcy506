import itertools
import sys
import argparse



name1 = "ana"
name2 = "luis"

str_1 = list(name1.lower())
str_2 = list(name2.lower())

print('Permutaciones de', str_1)

for char1 in itertools.permutations(str_1):
    if char1 == char1[::-1]:
        print(char1, "palindromo")
    else:
        print(char1)

for char2 in itertools.permutations(str_2):
    if char2 == char2[::-1]:
        print(char2, "palindromo")
    else:
        print(char2)
        print(char2)
