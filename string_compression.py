def string_compression(s):
    length = len(s)
    if length == 0:
        return ''
    if length == 1:
        return s + '1'

    i = 1
    count = 1
    op = ''
    while i <length:
        if s[i] == s[i-1]:
            count+=1
        else:
            op = op + s[i-1] + str(count)
            count = 1
        i+=1
    op = op + s[i-1] + str(count) # this line is for last character in the string
    return op

print string_compression('AAABBC')
