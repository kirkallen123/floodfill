word = input("Enter a word:")


def palindrome(some_word):
    return some_word == some_word[::-1]


valid = palindrome(word)

if valid:
    print("your word is a palindrome!")
else:
    print("your word is NOT a palindrome.")


