import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?\w+\.\w+')   # match all URLs

# Now, lets capture domain name (and top level) only by creating a group to extract (\w+)
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

print(pattern)

matches = pattern.finditer(urls)

for match in matches:
    print(match.group((0)))  # prints all the groups
    print(match.group((1)))  # prints the first group
    print(match.group((2)))  # prints the 2nd group
    print(match.group((3)))  # prints the 2nd group

# shorthand for access group modules
subbed_urls = pattern.sub(r'\2\3', urls)  # replace each match with just group 2 and group 3
print((subbed_urls))


