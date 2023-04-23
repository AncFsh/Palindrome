def palindrome_check(word):
    return word == word[::-1]

word = input("Please provide the word: ")
palindrome = palindrome_check(word)

print(palindrome)
