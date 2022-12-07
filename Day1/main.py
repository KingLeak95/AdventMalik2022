verbose = False
top_3 = True

def main(input_file):
    with open(input_file) as f:
        lines = f.readlines()

    calories = 0
    if top_3:
        max_calories = [0,0,0]
    else:
        max_calories = 0

    #Adding Extra Line for Logic 
    lines.append("")

    for l in lines:
        if len(l.rstrip()) > 0:
            calories += int(l.rstrip())
        else:
            if verbose:
                print(f"Current Caloreis {calories}")
            if top_3:
                max_of_list(max_calories, calories)
            else:
                if max_calories < calories:
                    max_calories = calories
            calories = 0
    if top_3:
        if verbose:
            print(f"Top 3 is {max_calories}")
        print(f"Total needed calories is {sum(max_calories)}")
    else:
        print(f"Max Calories Needed {max_calories}")

def max_of_list(input_list, replacement):
    for i in range(len(input_list)):
        if replacement > input_list[i]:
            input_list[i] = replacement
            input_list.sort()
            break

if __name__ == "__main__":
    main("input.txt")

