"""
 EX 1
"""
letter = input("Enter a letter from the alphabet (a-z or A-Z): ")

"""
* The `len` function checks if length of letter is 1
"""
if len(letter) == 1 and letter.isalpha():
    print("Valid letter entered:", letter)
else:
    print("Invalid letter entered:", letter)


"""
 EX 2
"""


