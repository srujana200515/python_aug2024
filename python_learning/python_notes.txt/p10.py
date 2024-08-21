#program to check if the alphabet is a Vowel or Consonant
alphabet=input("Enter the alphabet:").lower()
if alphabet in ('a','e','i','o','u'):
    print(alphabet, "is an vowel")
else:
    print( alphabet," is an Consonant")