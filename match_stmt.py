def checkVowel(n):
    match n:
        case "a" : return "Vowel"
        case "i" : return "Vowel"
        case "e" : return "Vowel"
        case "o" : return "Vowel"
        case "u" : return "Vowel"
        case _ : return "Consonant"

n = str(input("Enter a Alphabet : \n"))
print(checkVowel(n))
n = str(input("Enter a Alphabet : \n"))
print(checkVowel(n))
n = str(input("Enter a Alphabet : \n"))
print(checkVowel(n))
n = str(input("Enter a Alphabet : \n"))
print(checkVowel(n))
n = str(input("Enter a Alphabet : \n"))
print(checkVowel(n))