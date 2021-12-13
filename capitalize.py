# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
# For example, alison heck should be capitalised correctly as Alison Heck.

def capitals(s):

    old_strings = s.split(" ")
    new_strings = []
    new_word = ''
    for word in old_strings:
        for i in range(len(word)):
            if i == 0:
                new_word += word[0].upper()
            else:
                new_word += word[i]
        new_strings.append(new_word)
        new_word = ''
    capitalized = " ".join(new_strings)
    print(capitalized)

capitals('alison heck')