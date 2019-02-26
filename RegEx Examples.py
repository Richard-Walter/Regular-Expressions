import re

"""
From https://www.youtube.com/watch?v=K8L6KVGG-7o
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character  
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

ANCHORS (don't match any characters)
\b      - Word Boundary (whitespace or non-alphanumeric character)
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
"""
print('\tTab')
print(r'\tTab')  # raw string - interprets string literally

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''


def printMatches(pattern):

    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)

def printMatchesSentence(pattern):

    matches = pattern.finditer(sentence)
    for match in matches:
        print(match)

sentence = 'Start a sentence and then bring it to an end'

# printMatches(re.compile(r'abc'))
# printMatches(re.compile(r'coreyms\.com'))   # Must add escape character for metacharacters
# printMatches(re.compile(r'\bHa'))  # match at start of each word bdry
# printMatches(re.compile(r'\BHa'))  # match not at word bdry
# printMatches(re.compile(r'[^a-zA-Z]')) # match a character NOT a-zA-Z
# printMatches(re.compile(r'[^b]at')) # match a character NOT a-zA-Z
#
# printMatchesSentence(re.compile(r'start', re.IGNORECASE))  # Flag to ignore case
#
# printMatchesSentence(re.compile(r'^Start'))  # Find at start of a sentence.  match
# printMatchesSentence(re.compile(r'^a'))  # No match
# printMatchesSentence(re.compile(r'end$'))  # Find at end of a sentence.  match
# printMatchesSentence(re.compile(r'a$'))  # Find at end of a sentence.  match

# printMatches(re.compile(r'\d\d\d.\d\d\d.\d\d\d\d'))
# printMatches(re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d'))    # Character set: match ONE '-' or '.'
# printMatches(re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d'))

# # use quantifers to match multiple characters * = ? {,}
# printMatches(re.compile(r'[89]00[-.]\d{3}[-.]\d{4}'))   # demo using {} -  number of characters
#
# printMatches(re.compile(r'Mr\.'))
# printMatches(re.compile(r'Mr\.?'))    # demo using ? - match zero or one of proceeding character
# printMatches(re.compile(r'Mr\.?\s[A-Z]\w*'))    # demo using * - zero or more

# Demo using groups
printMatches(re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*'))    # demo using ()  match group of characters

# # Find data in a text file
# with open('data.txt', 'r') as f:
#     pattern = (re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d'))
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)


