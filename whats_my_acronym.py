# Ask the user to enter the full meaning of an organization
# or concept and you'll provide the acronym to the user.

concept = input("Enter the concept: ")
acronym = concept.upper().split(" ")
final = ""
for word in acronym:
    final = final+word[0]
print(final)




