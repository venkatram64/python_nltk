import re
import time

def group_by_name_example():

    pattern = r"(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})(?P<hour>\d{2})?"
    text = "Timestamp=20182112"

    print("Pattern {0}".format(pattern))
    print("Text {0}".format(text))
    match_iter = re.finditer(pattern, text)
    for match in match_iter:
        print("***Match. Text: {0} Index: {1} Length: {2}".format(match.group(0), match.start(), len(match.group(0))))
        print("Access group by name")
        print("  Year: {0}".format(match.group('year')))
        print("  Month: {0}".format(match.group('month')))
        print("  Day: {0}".format(match.group('day')))
        print("  Hour: {0}".format(match.group('hour')))
        print("Access all named groups as dictionary")
        print(" {0}".format(match.groupdict()))


if __name__ == '__main__':
    group_by_name_example()