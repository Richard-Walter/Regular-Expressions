import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

# pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')   # match first email
# pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)')  # match first and second email
pattern = re.compile(r'[a-zA-Z.0-9-]+@[a-zA-Z-]+\.(com|edu|net)')  # match all

matches = pattern.finditer(emails)

for match in matches:
    print(match)

