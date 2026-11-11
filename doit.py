Python 3.15.2 (tags/v3.15.2:5e58eaa, Oct 25 2026, 17:27:03) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
def isEven(number):
    return number % 2 == 0
def isOdd(number):
    return not isEven(number)

# main program
if isEven(10):
    print('Even!')
else:
    print('Odd!')
