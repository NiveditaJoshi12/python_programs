# A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet.
# Ignore case. Return either pangram or not pangram as appropriate.
# Complete the function pangrams in the editor below. It should return the string pangram if the input string is a pangram.
# Otherwise, it should return not pangram.

def pangram(s):
    lst = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lower_s = set(s.lower())
    lst_s = sorted(list(lower_s))
    if lst == lst_s:
        return "pangram"
    else:
        return "not pangram"


s = input("Enter the string: ")
print(pangram(s))
