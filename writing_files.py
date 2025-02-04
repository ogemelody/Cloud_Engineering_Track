from fontTools.varLib.interpolatableHelpers import transform_from_stats

data = "asdfgh"
file_to_write = open ("file.txt", "w")
file_to_write.write(data)
file_to_write.close()

#but a better way
#with open ("file2.txt", "w")

contact_file = open("contact.txt", "w")
contact_file.write("Alice - 555-5050-0000")
contact_file.close()

#
with open("contact.txt", "w") as contact_file:
    contact_file.write("Alice - 555-5050-0000 \n")
    contact_file.write("bon - 555-5050-0000 \n")
    contact_file.write("carlo - 555-5050-0000 \n")


"""#create function to make it better
def contact_file(input_file, output_file):
    with open(input_file, "r") as file:
        name = file.readlines()

    contacts = []

    for contact in contacts:
        contacts.append(name.upper())

    with open(output_file, "w") as file:
        file.writelines(contacts)


contact_file("contact.txt", "new_contact.txt")

"""
"""Group Exercise
def new_file( input_file, output_file):
    with open(input_file, "r") as file:
        replace_name = file.readlines()
       # replace_name = file.replace("ROMEO", "JACK")
        new_names = []

        for new_name in new_names:
            new_names.append(file.replace("ROMEO", "JACK"))

    with open(output_file, "w"):
        file.write()

new_file("")"""

##

"""text_modified = text.replace("ROMEO", "JACK").replace("JULIET", "ROSE")
text_modified_2 = text_modified.replace("romeo", "jack").replace("juliet", "rose")
text_modified_3 = text_modified_2.replace("Romeo", "Jack").replace("Juliet", "Rose")
print(text_modified_3)"""


def replace(text):
    replacement = {
        "ROMEO": "JACK",
        "JULIET": "ROSE",
        "romeo": "jack",
        "juliet": "rose",
        "Romeo": "Jack",
        "Juliet": "Rose"
    }
    previous_text = ""
    while previous_text != text:
        previous_text = text
        for old_word, new_word in replacement.items():
            text_modified = text.replace(old_word, new_word)
    return text_modified

with open("romeoandjuliet.txt", "r") as file:
    text = file.read() # put entire file into a variable

replaced_text = replace(text) # saved file
with open("jack_and_rose.txt", "w") as new_file:
    new_file.write(replaced_text)

