sentence = input("Please enter a sentence: ")
count = 0
sentence_list = list(sentence)
for value in sentence_list:
    if value == "e" or value == "E":
        count += 1
print(f"There are {count} e's in your sentence")
