import re

string = "abc sddfmklsf vivegan.k@gmail.com fhcffg"

a = re.search(r'([\w.-]+)@([A-Za-z]+).([A-Za-z]{1,3})', string)

if a:
    print(a.group())
    print(a.group(1))
    print(a.group(2))
    print(a.group(3))


"""
Output:
vivegan.k@gmail.com
vivegan.k
gmail
com
"""

new_str = "vivek dsfnlasjnf jnjlsndlfjn  12 345 90 877 hsdfhbdbhfj 12   345  90  877"

match = re.findall(r'\d{2}\s*\d{3}\s*\d{2}\s*\d{3}', new_str)

print(match)

"""
Output:
['12 345 90 877', '12   345  90  877']
"""

ip_str = '01.168.1.1'

pattern = r'^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.' \
          r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.' \
          r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.' \
          r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'

ip_match = re.search(pattern, ip_str)

if ip_match:
    print(ip_match.group())


with open('regex_cont.txt', 'r') as f:
    print(re.findall(r'([\w.-]+)@([A-Za-z]+).([A-Za-z]{1,3})', f.read(), re.M))
    for line in f.readlines():
        match = re.search(r'([\w.-]+)@([A-Za-z]+).([A-Za-z]{1,3})', line)
        if match:
            print(match.group())
    print(re.findall(r'([\w.-]+)@([A-Za-z]+).([A-Za-z]{1,3})', f.read(), re.M))

