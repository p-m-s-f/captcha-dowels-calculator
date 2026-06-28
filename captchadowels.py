import sys # importing sys so we can use sys.exit() when parsing input
CAPTCHA_VALS = []

def get_input():
    '''
    Prompts the user to paste the image URL for today's Flash
    Gordon strip, and returns their input as a string.
    '''
    print("Type or paste your captchalogue code:")
    inputString = str(input())

    return inputString

def create_list_of_captcha_values():
    '''
    Creates a list of characters comprising Homestuck's captcha code cipher,
    representing numbers 0-63 in ascending order.
    The first 62 characters -- actually the complete list of alphanumeric
    characters in lexicographically ascending order  (i.e.
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    -- represent numeric values 0-61. The final two characters ("?" and "!")
    represent numbers 62 and 63.

    We can retrieve the numerical value associated with a given character by
    retrieving that character's list index, e.g. 0=0, 1=1... A=10, and so on.
    '''
    numericalChars = [str(n) for n in list(range(0,10))]

    from string import ascii_uppercase as upCaseAlphabet
    lowCaseAlphabet = upCaseAlphabet.casefold()
    alphabeticalChars = list(upCaseAlphabet + lowCaseAlphabet + "?!")

    listOfCaptchaVals = numericalChars + alphabeticalChars
    return listOfCaptchaVals

def process_input(input):
    '''
    check input is correct, and if it is, return input as list of characters-as-strings
    '''
    #Check that input is correct length
    lenInput = len(input)
    if lenInput != 8:
        if lenInput > 8:
            print("Error: Your captchalogue code is too long. Check your code and try again.")
        else:
            print("Error: Your captchalogue code is too short. Check your code and try again.")
        sys.exit(1)

    listOfInput = list(input)
    for char in listOfInput:
        if char not in CAPTCHA_VALS:
            print("Error: Your captchalogue code contains an imcompatible character. Check your code and try again.")
            sys.exit(1)

    return listOfInput


def get_dowel_seg_widths(input):
    '''
    Takes captchalogue code as list of characters (strings), creates
    a list of ints corresponding to each character's captcha cipher value,
    uses said list to calculate widths of carved dowel segments,
    returns list of segment widths
    '''
    inputCaptchaVals = [CAPTCHA_VALS.index(char) for char in input]
    dowelSegWidths = [((63-captchaVal) / 63 ) * 100 for captchaVal in inputCaptchaVals]

    return dowelSegWidths


def main():
    '''
    TODO:
    - maybe just write an error message function? 
    - write a print function
    - consider rewriting process_input so it's not repeating error code (kind of same as prev. todo)
    - maybe add length-checking etc. to get_input, so the computer does less work
    '''
    global CAPTCHA_VALS
    CAPTCHA_VALS = create_list_of_captcha_values()

    input = get_input()
    input = process_input(input)

    dowelSegWidths = get_dowel_seg_widths(input)
    for width in dowelSegWidths: print(width) #TODO: write a proper print function, erase this later.

if __name__ == "__main__":
    main()