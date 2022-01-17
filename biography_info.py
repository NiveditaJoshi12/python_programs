# Ask a user for their personal information one question at a time.
# Then check that the information they entered is valid.
# Finally, print a summary of all the information they entered back to them.

name = input("Enter the name: ")
date_of_birth = input("Enter date of birth in format month day, year: ")
address = input("Enter the address: ")
personal_goals = input("Enter personal goals: ")
if name.isalpha() == True:
    print("-Name: ", name)
else:
    print("You have entered wrong input. Please enter valid name.")

print("-Date of Birth: ", date_of_birth)
print("-Address: ", address)
print("-Personal Goals: ", personal_goals)
