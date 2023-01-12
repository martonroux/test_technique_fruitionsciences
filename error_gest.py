import os.path
import re
import sys

class ErrorGest:
    def __init__(self):
        pass

    def len_gest(self):
        if len(sys.argv) < 2:
            print("Not enough arguments provided. -h for more info", file=sys.stderr)
            sys.exit(1)

        if len(sys.argv) > 2:
            print("Too much arguments provided. -h for more info", file=sys.stderr)
            sys.exit(1)

    def h_flag(self):
        if sys.argv[1] != "-h":
            return
        print("Usage:\n\t./aspirateur <file_name>\nThe file needs to have:")
        print("\t- size of map on the first line")
        print("\t- initial position on the second line")
        print("\t- sequence of directions on the third line.")
        sys.exit(0)

    def file_check(self):
        def check_file_exists(file):
            return os.path.exists(file)

        def check_first_line(file_content):
            list_values = file_content.split(" ")

            if len(list_values) != 2:
                print("Not enough/too much data on first line", file=sys.stderr)
                return 0

            if not list_values[0].isnumeric() or not list_values[1].isnumeric():
                print("Found non-numeric characters on first line of file", file=sys.stderr)
                return 0

            nums = re.findall(r'\d+', file_content)
            if len(nums) < 2:
                print("Not enough numbers found on first line", file=sys.stderr)
                return 0

            if len(nums) > 2:
                print("Too much numbers found on first line", file=sys.stderr)
                return 0
            return 1

        def check_second_line(file_content):
            list = file_content.split(" ")

            if len(list) != 3:
                print("The data on the second line is incorrect", file=sys.stderr)
                return 0

            if not list[0].isnumeric() or not list[1].isnumeric():
                print("One of the numbers on the second line is not an integer", file=sys.stderr)
                return 0

            if not list[2] in ['N', 'W', 'E', 'S']:
                print("The direction on the second line is incorrect", file=sys.stderr)
                return 0
            return 1

        def check_third_line(file_content):
            for i in file_content:
                if i != 'A' and i != 'D' and i != 'G':
                    print("Found character other than A or D on third line", file=sys.stderr)
                    return 0
            return 1

        file = sys.argv[1]

        if check_file_exists(file) == 0:
            print("File doesnt exist", file=sys.stderr)
            sys.exit(1)

        file_content = open(file).read()
        file_content = file_content.split("\n")

        if len(file_content) != 3:
            print("Too much/not enough lines in file", sys.stderr)
            sys.exit(1)

        if check_first_line(file_content[0]) == 0:
            sys.exit(1)

        if check_second_line(file_content[1]) == 0:
            sys.exit(1)

        if check_third_line(file_content[2]) == 0:
            sys.exit(1)
