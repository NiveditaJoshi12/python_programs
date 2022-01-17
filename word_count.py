# Ask the user what's on their mind. Then after the user responds,
# count the number of words in the sentence and print that as an output.
with open("word-count", 'r') as f:
    words = f.read()
    count = 0
    for word in range(len(words)):
        count +=1
    print("The number of characters in the file are ",count)

