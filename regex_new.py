
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
192.168.2.1
17.230.120.22
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
bat

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

sentence = 'Start a sentence and then bring it to an end'

matches = re.findall(r'start', sentence, re.I)

print(matches)

matches = re.findall(r'\d\d\d.\d\d\d.\d\d\d', text_to_search, re.I) # To search all strings in pattern 123{anychar}456{anychar}789
print(matches)

matches = re.findall(r'\d\d\d[-*]\d\d\d[-*]\d\d\d', text_to_search, re.I) # To search all strings in pattern 123{- or * char}456{- or * char}789

print(matches)


matches = re.findall(r'[89]00[-*]\d\d\d[-*]\d\d\d', text_to_search) # To search all strings in pattern starts_with_800_900{- or * char}456{- or * char}789

print(matches)

matches = re.findall(r'[^b]at', text_to_search) # To search all strings in pattern not_starts_with_b and ends_with_at

print(matches)

matches = re.findall(r'Mr\.?\s[A-Z][a-z]*', text_to_search) # All names starts with Mr
print(matches)

ip_pattern = r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])'
matches = re.findall(ip_pattern,text_to_search)
print(matches)

email_pattern = r'([a-zA-Z][a-zA-Z1-9-_.]+)@([a-zA-Z]+).([a-zA-Z-.]+)'
matches = re.finditer(email_pattern,text_to_search)
for match in matches:
    print(match)
