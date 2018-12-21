import re
import time

def validation_example_three():

    pattern = r"^\d+$"
    positiveTest = ["123456", "456", "321882", "0820102"]
    negativeTest = ["ABCD", "A1234", "1234AB", "  123", "321  ", " 111   ", "123 4567", "123\n456"]
    print("Pattern {0}".format(pattern))

    for text in positiveTest:
        match = re.search(pattern, text)
        if match:
            print("***Match. Text:{0} Index: {1} Length: {2}".format(text, match.start(), len(match.group(0))))
        else:
            print("***No Match. Text {0}".format(text))
            raise ValueError("Positive Test. Expected successful match but failed {0}".format(text))

    for text in negativeTest:
        match = re.search(pattern, text)
        if match:
            print("***Match. Text:{0} Index: {1} Length: {2}".format(text, match.start(), len(match.group(0))))
            raise ValueError("Negative Test. Expected failed match but failed {0}".format(text))
        else:
            print("***No Match. Text {0}".format(text))




if __name__ == '__main__':
    validation_example_three()