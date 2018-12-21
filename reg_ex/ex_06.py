import re
import time

def find_iter_example():

    pattern = r"\b\d{5}\b"
    text = "NY Postal Codes are 10001, 10002, 10003, 1004"

    print("Pattern {0}".format(pattern))
    print("Text {0}".format(text))
    match_iter = re.finditer(pattern, text)
    for match in match_iter:
        print("***Match. Text: {0} Index: {1} Length: {2}".format(match.group(0), match.start(), len(match.group(0))))


if __name__ == '__main__':
    find_iter_example()