import re
import time

def validation_example_two():

    pattern = r"\d+"
    text = "1234"
    match = re.search(pattern, text)
    print("Pattern {0}".format(pattern))

    if match:
        print("***Match. Text:{0} Index: {1} Length: {2}".format(text, match.start(), len(match.group(0))))
    else:
        print("***No Match. Text {0}".format(text))

    text = "Hello World"
    match = re.search(pattern, text)

    if match:
        print("***Match. Text:{0} Index: {1} Length: {2}".format(text, match.start(), len(match.group(0))))
    else:
        print("***No Match. Text {0}".format(text))





if __name__ == '__main__':
    validation_example_two()