#In this function, we have two strings as the input for checking as anagram
#As item assignment is not allowed in string, second string is coverted to list.
#Each character from the first string is compared with the second list and replace list value to None if found. And also stillOK condition maintained as True

def anagram_detection(s1, s2):
    alist = list(s2) #Converted to list for supporting assignment of None value
    pos1 = 0
    stillOK = True
    while pos1 < len(alist) and stillOK: 
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found: #In this loop, each value of the string is compared to all the values in list
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else: #If not found, sets the stillOK value as False
            stillOK = False
        pos1 = pos1 + 1

    return stillOK

print anagram_detection('heart','earth')
print anagram_detection('heart','eartg')
        
