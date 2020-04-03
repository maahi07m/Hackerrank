'''
Task

You have a test string s.
Your task is to write a regex that will match s using the following conditions:

s should begin with  1 or 2 digits.
After that,  should have  3 more letters (both lowercase and uppercase).
Then s should end with up to 3 . symbol(s). You can end with 0 to 3 . symbol(s), inclusively.
'''
Regex_Pattern = r'^\d{1,2}[a-zA-Z]{3,}[.]{0,3}$'
