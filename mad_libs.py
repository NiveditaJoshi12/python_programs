# Mad libs generator
# Loop back to this point once the code finishes

loop = 1

while loop < 10:
    noun = input("Choose a noun: ")
    p_noun= input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place= input("Name a place: ")
    adjective = input("Choose an adjective: ")
    noun3 = input("Choose a noun: ")

    # Displays the story based on user's input
    print("----------------------------------")
    print("Be kind to your", noun, "- footed", p_noun)
    print("For a duck may be somebody's", noun2, ",")
    print("Be kind to your", p_noun, "in", place)
    print("Where the weather is always", adjective, ".")
    print()
    print("You may think that is this the", noun3, ",")
    print("Well it is.")
    print("------------------------------------------")

    # Loop back to "loop = 1"
    loop = loop + 1