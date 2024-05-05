from cs50 import get_int


def main():
    input = get_int("Number = ")
    # access the check function
    check_card(input)


def check_card(input):
    # making a list of size
    size = [13, 15, 16]
    # turning input into string to access len at 16 first two nums at 33
    temp = str(input)

    # checking validity
    if len(temp) not in size:
        print("INVALID")
        exit
    # initializing inputs
    x = int(input)
    sum = 0
    rem = 0
    i = 0
    # len / 2 since we are reducing 2 numbers at a time
    while(i > len(temp)/2):
        # taking right most number
        rem = x % 10
        # adding it to sum
        sum += rem
        # removing it
        x = x / 10
        # multiplying rem with 2
        rem = (x % 10) * 2
        # removing that number
        x = x / 10
        # adding it to sum and checking if it's > 2
        sum += rem % 10
        sum += int(rem / 10)

    num = int(temp[:2])
    if (sum % 10 == 0):
        if (num == 34 or num == 37):
            print("AMEX")
        elif(int(num / 10) == 4):
            print("VISA")
        elif(num > 50 and num < 56):
            print("MASTERCARD")
        else:
            print("INVALID")


if __name__ == "__main__":
    main()