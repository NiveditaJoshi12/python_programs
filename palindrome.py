# Ask the user to give you five words. Then check if any of the five words is a palindrome.

def string_list():
    raw_input = list(input("Enter a word or sentence to check if palindrom: ").lower())
    return raw_input

def remove_extra_chars(dirtyList):
    analphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""]
    newlist = []
    for char in dirtyList:
        if char not in analphabeticList:
            newlist.append(char)
    return newlist

def ifpalindrome(main_list):
    newstring = "".join(main_list)
    if main_list==main_list[::-1]:

        print(f'{newstring} is a palindrome')
    else:
        print(f'{newstring} is not a palindrome')
original = string_list()
new1=remove_extra_chars(original)
ifpalindrome(new1)
