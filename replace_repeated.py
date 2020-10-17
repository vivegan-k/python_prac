import re

a = re.sub(r'(.)\1+', r'-', 'abaaadf')
print a
