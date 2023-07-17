#!/usr/bin/env python3
"""Alta3 Challenge"""

def main():
    line_counter = 0

    with open("dracula.txt", "r") as foo:
        print("+++++++++++++++++++++ part1 +++++++++++++++++++")
        for lines in foo:
            print(lines)

        print("+++++++++++++++++ part3 and part4 +++++++++++++")
        for lines in foo:
            if "vampire" in lines.lower():
                print(lines)
                line_counter += 1
        print("++++++++++++++++ part5 +++++++++++++++++++++++++")
        print("vampire appears " + str(line_counter) + " times")

        print("++++++++++++++++ part6 +++++++++++++++++++++++++")
    
        with open("vampytimex.txt", "w") as fang:
            for lines in foo:
                if "vampire" in lines.lower():
                    fang.write(lines)

if __name__ == "__main__":
    main()
