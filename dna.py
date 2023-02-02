import csv
import sys


def main():

    if len(sys.argv) != 3:
        print('ERROR')
        exit(1)

    with open(sys.argv[1], 'r') as data:

        csvreader = csv.reader(data, delimiter=',')

        header = next(csvreader)

        database = []

        for row in csvreader:
            entry = {}
            for i in range(len(header)):
                entry[header[i]] = row[i]
            database.append(entry)

    with open(sys.argv[2], 'r') as seq:
        csvreader = csv.reader(seq)
        sequence = next(csvreader)

    strs = list(database[0].keys())[1:]

    counts = []
    for each in strs:
        counts.append(longest_match(sequence[0], each))

    str_counts = {}

    for i in range(len(strs)):
        str_counts[strs[i]] = counts[i]

    for person in database:
        match = 0
        for key in list(person.keys())[1:]:
            if int(person[key]) == str_counts[key]:
                match += 1
            else:
                break

            if match == len(counts):
                print(person['name'])
                exit(0)
                
    print('No match')


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
