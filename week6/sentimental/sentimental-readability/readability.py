from cs50 import get_string


def main():
    # getting input
    input = get_string("Text: ")
    # applying function defined below
    grade(input)


def grade(input):
    # initializing letters, words, sentences
    let = 0
    word = 1
    sen = 0
    # looping thru all list
    for i in range(len(input)):
        # to collect data for colemen liau index
        if input[i].isalpha():
            let += 1
        elif input[i].isspace():
            word += 1
        elif input[i] == '.' or input[i] == '?' or input[i] == '!':
            sen += 1
    # Applying Colemen Liau Index
    grade = round((0.0588 * let / word * 100) - (0.296 * sen / word * 100) - 15.8)
    # Printing out the grade
    if grade < 1:
        print("Before Grade 1")
    elif grade > 15:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")
    return


if __name__ == "__main__":
    main()