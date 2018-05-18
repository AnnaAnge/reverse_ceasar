__author__ = 'annaangelogianni'  #http://scottbryce.com/cryptograms/stats.htm
import collections

#from collections import OrderedDict
#import OrderDict
ciphertext = raw_input("Enter encrypted message: ")

#letters = collections.Counter(+ciphertext)
#print " " +letters

#letters = collections.defaultdict(int)
#for letter in OrderDict(ciphertext):
#    letters[letter] += 1
#print letters


freq=collections.Counter(ciphertext)
print freq

key = int(input("Enter key: "))
plaintext = ""

for character in ciphertext:
    if character.isalpha():                         #is it aplphabetic ?!
        if character.isupper():                     #is it uppercase ?!
            is_uppercase = True
            character = character.lower()           #transform to lowercase

        else:
            is_uppercase = False
        character = ord(character) + key            #transform ASCII to Decimal and add key value

        if character > 122:                         #check if character > 122 (z in ASCII)
            character = character - 26
        character = chr(character)

        if is_uppercase:                            #if uppercase
            character = character.upper()
        plaintext = plaintext + character

    else:                                           #if not aplhabetic
        plaintext = plaintext + character



print "Encrypted message: " + plaintext