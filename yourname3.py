#example of a continue statement
spam = 0
while spam < 5: 
    spam = spam + 1
    if spam == 3:
        continue #jumps back to the start of the while loop
    print('spam is ' + str(spam))