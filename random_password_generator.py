# For this challenge, we will use a Python script to generate a random password of 8 characters.
# Each time the program is run, a new password will be generated randomly.
# The passwords generated will be 8 characters long and will have to include the following characters in any order:
# 2 uppercase letters from A to Z,
# 2 lowercase letters from a to z,
# 2 digits from 0 to 9,
# 2 punctuation signs such as !, ?, “, # etc.

import random

# A function to shuffle all the characters of the string
def shuffle_string(string):
    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)

#Main program starts here

uppercase1 = chr(random.randint(65,90))
uppercase2 = chr(random.randint(65,90))
lowercase1 = chr(random.randint(97,122))
lowercase2 = chr(random.randint(97,122))
digit1 = chr(random.randint(48,57))
digit2 = chr(random.randint(48,57))
punc1 = chr(random.randint(33,47))
punc2 = chr(random.randint(33,47))

passwd = uppercase1+uppercase2+lowercase1+lowercase2+digit1+digit2+punc1+punc2
print(shuffle_string(passwd))

