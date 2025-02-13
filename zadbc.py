from curses.ascii import isdigit

input = "abc123xyz45"

def sum_of_digits(text):
    convert = list(text)
    print(convert)
    total = 0
    for char in convert:
        if char.isdigit():
            value = int(char)
            total += value
    print(total)

 #ätext = input
sum_of_digits(input)

###

#print(longest_word_in_sentence("its a beautiful day")) # Expected: "beautiful" (length 9)
#print((longest_word_in_sentence("can you find the longest word here"))) # Expected: "longest" (length 7)
#print((longest_word_in_sentence("she loves pizza"))) # Expected: "pizza" (length 5)

def longest_word_in_sentence(word):
    word_split = word.split()
    word_list = list(word_split)
    longest_word = ""
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    print (longest_word)

    #print(word_list)
longest_word_in_sentence("its a beautiful day")

#