import re
import time

def find_all_example():

    pattern = r"\b\d{5}\b"
    text = "NY Postal Codes are 10001, 10002, 10003, 1004"

    print("Pattern {0}".format(pattern))
    match = re.findall(pattern, text)
    print(match)


if __name__ == '__main__':
    find_all_example()