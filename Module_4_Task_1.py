def check_palindrom(word):
    new_word = word[::-1]
    if new_word == word:
        return True
    
if check_palindrom(input ("Insert a word: ")) == True:
    print("Palindrom")
else:
    print("No Palindrom")
