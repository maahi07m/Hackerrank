'''
Input Format

N, where N is the number of tests.
This will be followed by N lines containing N phone numbers in the format specified above.

Constraints

1 <= N <= 20
There might either be a hyphen, or a space between the segments
The country and local area codes can have 1-3 numerals each and the number section can have 4-10 numerals each.

Output Format

Your output will contain N lines.
CountryCode=[Country Code],LocalAreaCode=[Local Area Code],Number=[Number]
'''
import re
for i in range(int(input())):
    string = input()
    pattern = re.compile(r'(\d{1,3})[\s-](\d{1,3})[\s-](\d{4,10})')
    match = pattern.match(string)
    print("CountryCode=" + match.group(1) + ",LocalAreaCode=" + match.group(2) + ",Number=" + match.group(3))
