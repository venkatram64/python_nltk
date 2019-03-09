import re
import time



def substitution_example():

    pattern = r"(?P<value>\d+(,\d{3})*(\.\d{2})?)\s+dollar(s)?"
    replacement_pattern = r'***USD \g<value>**'
    text = '''Widget Unit cost: 12,000.56 dollars Taxes: 234.00 dollars Total: 12,234.56 dollars...'''

    print("Pattern {0}".format(pattern))
    print("...Text {0}".format(text))

    new_text = re.sub(pattern, replacement_pattern, text)

    print('---New Text:\n{0}'.format(new_text))


if __name__ == '__main__':
    substitution_example()