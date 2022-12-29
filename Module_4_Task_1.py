def check_palindrome(word):

    """ 
    This function checks if the given word is a palindrome or not 
    :param: string 
    :return: boolean 
    """

    new_word = word[::-1]
    if new_word == word:
        return True
    
if check_palindrome(input ("Insert a word: ")):
    print("Palindrome")
else:
    print("No Palindrome")

#help(check_palindrome)
