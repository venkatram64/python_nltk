import re
import time

def group_by_number_example():

    pattern = r"(\d{4})(\d{2})(\d{2})(\d{2})?"
    text = "Timestamp=20182112"

    print("Pattern {0}".format(pattern))
    print("Text {0}".format(text))
    match_iter = re.finditer(pattern, text)
    for match in match_iter:
        print("***Match. Text: {0} Index: {1} Length: {2}".format(match.group(0), match.start(), len(match.group(0))))

        for i, value in enumerate(match.groups()):
            print('   Group: {0}, Value: {1}'.format(i+1, value))


if __name__ == '__main__':
    group_by_number_example()