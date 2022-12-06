import re
verbose = False
sections_regex = r"(\d+)-(\d+),(\d+)-(\d+)"
overlaps_complete = False
def main(input_file):
    count = 0
    # Read File Input
    with open(input_file)  as input_fs:
        lines = input_fs.readlines()

    for l in lines:
        m = re.match(sections_regex, l)
        r1_1 = int(m.group(1))
        r1_2 = int(m.group(2))

        r2_1 = int(m.group(3))
        r2_2 = int(m.group(4))

        range1 = [*range(r1_1, r1_2+1)]
        range2 = [*range(r2_1, r2_2+1)]

        if verbose:
            print(range1)
            print(range2)

        if overlaps_complete:
            if set(range1).issubset(range2) or set(range2).issubset(range1) :
                count += 1
                if verbose:
                    print(l)
        else:
            if set(range1) & set(range2):
                count += 1
                if verbose:
                    print(l)

    print(f"The number of pairs are {count}")


if __name__ == "__main__":
    main("input.txt")
