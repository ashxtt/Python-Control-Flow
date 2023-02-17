"""
 EX 1
"""
#Prompts user to enter letter
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
# statement to check if letter is a vowel or not
if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("This letter is a vowel")
else:
    print("The letter is not a vowel")


"""
 EX 3
"""
# checks if the letter the user enters if from a vowel from the string or a constant
if letter in 'aeiou':
    print(f"The letter {letter} is a vowel.")
else:
    print(f"The letter {letter} is a constant")


"""
 Length of Phrase
"""

while True:
    phrase = input("please enter a word or phrase: ")
    if phrase.lower() == "quit":
        break;
    else:
        #checks length of characters entered by user
        length = len(phrase)
        print(f"what you entered is {length} characters Long")



"""
 Calculate Dog Years
"""
human_years = int(input("input a dog's age in human years: "))
if human_years <= 2:
    dog_years = human_years* 10
else:
    dog_years = 20 + (human_years - 2) * 7

print(f"The dog's age in dog years is {dog_years}")

"""
 What kind of Traingle
"""
print("enter the lengths of three sides of a triangle: ")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a == b == c:
    triangle_type = "equilateral"
elif a != b != c != a:
    triangle_type = "scalene"
else:
    triangle_type = "isosceles"

print(f"A triangle with sides of {a}, {b}, and {c} is a {triangle_type} triangle.")

"""
Fibi seconce
"""

a, b = 0, 1

#printing the fiesrt 2 terms
print(f"terms: 0 / number: {a}")
print(f"terms: 1 / number: {b}")


for i in range(2, 50):
    c = a +b 
    print(f"term: {i} / number: {c}")
    a, b = b, c


"""
 What the season
"""

#prompst user to enter month and day
month = input("Enter the month of the season ( jan - dec):")
day = int(input("Enter thw day of the month: "))

# Cal the season based on month and day
if month in ('Jan', 'Feb', 'Mar'):
    season = 'Winter'
elif month in ('Apr', 'May', 'Jun'):
    season = 'Spring'
elif month in ('jul', 'Aug', 'Sep'):
    season = 'Summer'
else:
    season = 'Fall'

# do the day fall on equinox or solstice
if month == 'Mar' and day >= 20:
    seasin = 'Spring'
elif month == 'Jun' and day >= 21:
    season = 'Summer'
elif month == 'Sep' and day >= 22:
    season = 'Fall'
elif month == 'Dec' and day >= 21:
    season = 'Winter'

#output the month day and the season it in
print(f"{month} {day} is in {season}")
