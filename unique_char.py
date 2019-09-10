def unique_char(s):
    seen = []
    for char in s:
        if char not in seen:
            seen.append(char)
        else:
            return False
    return True

print unique_char('abccde')
