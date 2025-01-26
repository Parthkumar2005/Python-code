character = input("Enter a character: ")
if len(character) == 1 and character.isalpha():
    if character.lower() in "aeiou":
        print("The character entered is a vowel.")
    else:
        print("The character entered is a consonant.")
else:
    print("Please enter a valid alphabetic character.")
