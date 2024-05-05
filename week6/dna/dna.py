from csv import reader, DictReader
from sys import argv, exit


def main():

    # TODO: Check for command-line usage
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit()
    # TODO: Read database file into a variable
    with open(argv[1], "r") as csvF:
        read = DictReader(csvF)
        db = list(read)

    # Store info in string
    # TODO: Read DNA sequence file into a List
    with open(argv[2], "r") as txt:
        sq = txt.read()

    # TODO: Find longest match of each STR in DNA sequence
    matches = {}
    for data in db[0]:
        matches[data] = longest_match(sq, data)

    # Create Dict to to store the seq
    # TODO: Check database for matching profile

    sus = "no match"
    tests = len(matches)
    counter = 1
    for data in range(len(db)):
        counter = 1
        for match in matches:
            if str(matches[match]) == db[data][match]:
                counter += 1
        if counter == tests:
            sus = db[data]["name"]
            print(sus)
            break

    print(sus)
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()