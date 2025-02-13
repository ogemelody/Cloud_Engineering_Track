"""def average_value_of_list(list_numbers):
    if len(list_numbers) == 0:
        return "List cannot be empty"
    total = 0
    for n in list_numbers:
        total += n
    return total / len(list_numbers)


   # if len(nums) == 0:
  #      return 0


print(average_value_of_list([]))"""

"""Write a function count_vowels(sentence) that counts the total number of vowels (a, e, i, o, u) in the given sentence.
- Capital letters (A, E, I, O, U) should also be included.
print(count_vowels("Mondays are not so bad"))  # Expected: 7
print(count_vowels("Apple is an amazing fruit"))  # Expected: 9
print(count_vowels("I am a Software Engineer"))  # Expected: 10"""

def count_vowels(sentence):
    sentence = sentence.lower().split()
    count = 0
    for word in sentence:
        for  letter in word:
            if  letter in ["a", "e","i", "o", "u"]:
                count +=1
    return count


print(count_vowels("Mondays are not so bad"))  # Expected: 7
print(count_vowels("Apple is an amazing fruit"))
print(count_vowels("I am a Software Engineer"))