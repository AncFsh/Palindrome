def palindrome_check(word):
    return word == word[::-1]

'Za pomocą tej funkcji program sprawdza czy po odwróceniu słowa, jest takie samo'

word = input("Please provide the word: ")
palindrome = palindrome_check(word)

if palindrome:
    print(True)
else:
    print(False)