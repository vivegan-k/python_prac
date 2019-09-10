def anagram_detection(s1, s2):
    counter1 = [0] * 26
    counter2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        counter1[pos] = counter1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        counter2[pos] = counter2[pos] + 1

    stillOK = True
    j = 0
    while j < 26 and stillOK:
        if counter1[j] == counter2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK
            
print anagram_detection('heart','earth')
print anagram_detection('heart','eartg')
