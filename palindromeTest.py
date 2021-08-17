def is_palindrome(word):
    converted_word = list(word)
    copied_word = converted_word.copy()

    converted_word.reverse()

    print(copied_word)
    print(converted_word)

    list_length = len(copied_word)
    index = 0

    while index < list_length:
        position1 = copied_word[index]
        position2 = converted_word[index]

        if position1 == position2:
            if index == list_length-1:#if the index is at the very last position
                print(True)
                print("It is a palindrome.")
                break #to stop and prevent an infinite loop
            else:
                index += 1
        else:
            print(False)
            print("It is not a palindrome.")
            break

is_palindrome("level")