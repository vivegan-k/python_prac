import re

number = '+91-94888 90877'

num_pattern = re.compile("^(\D*)(\d{2})(\D*)(\d{5})(\D*)(\d{5})$")

print num_pattern.search(number).groups()

str = "I am vivek"

print 'search---> %r' %(re.search("vivek",str))
print 'match---> %r' %(re.match("vivek",str))
