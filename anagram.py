l1 = [0] * 26
l2 = [0] * 26

def check_anagram(s1, s2):
    for char in s1:
        pos = ord(char) - ord('a')
        l1[pos] += 1
    for char in s2:
        pos = ord(char) - ord('a')
        l2[pos] += 1
    stillOK = True
    i = 0
    while i < len(l1):
        if l1[i] == l2[i]:
            i += 1
        else:
            return False

    return True

print(check_anagram('garden', 'dangerg'))
