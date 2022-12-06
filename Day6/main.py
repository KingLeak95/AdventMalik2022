verbose = False
length = 14

def main(input_file):
    # Read File Input
    with open(input_file)  as input_fs:
        lines = input_fs.readlines()
    
    input_text = ''.join(lines)
    if verbose:
        print(f"Text is {input_text}")

    for i in range(len(input_text) - length - 1):
        possible_output = input_text[i:i+length]
        if verbose:
            print(f"Checking {possible_output}")
        if len(set(possible_output)) == length:
            print(f"Input is {possible_output}")
            print(f"First marker is {i+length}")
            break

if __name__ == "__main__":
    main("input.txt")
