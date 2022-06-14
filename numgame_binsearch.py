# # Number Guessing using Binary Search

# Func to guess the num in defined range of num
def guessNumber(startRange, endRange):
    if startRange > endRange:
        return True
    mid = (startRange + endRange)//2
    # Ask usr
    print(f'Is the num is {mid}? ')
    usr = input()
    print(usr)
    # condition Check if the typed num is correct
    if usr == "y" or usr =="Y":
        print("Suffer from Success \n (c) Rick Ross")
        return False
    # condition Check if the typed num is incorrect
    elif usr == "n" or usr == "N":
        print(f'Actual num is greater than {mid}? ')
        usr = input()
        print(usr)
        if usr == "y" or usr == "Y":
            return guessNumber(mid+1, endRange)
        elif usr == "n" or usr == "N":
            return guessNumber(startRange, mid-1)
        else:
            print("invalid input. print 'Y'/'N'")
            return guessNumber(startRange, endRange)
    # condition Check if usr input is valid
    else:
        print("Invalid input. Print 'Y'/'N'")
        return guessNumber(startRange, endRange)

# Driver code
if __name__ == "__main__":
    print('Number Guessing Game in Snake Language!')
    startRange = 1
    endRange = 1000000
    print(f'Guess The Number in Range ({startRange} to {endRange})')

    out = guessNumber(startRange, endRange)

    if out:
        print('Unlucky,mate')