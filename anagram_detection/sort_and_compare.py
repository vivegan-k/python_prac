#Sorts the string and compares
def anagram_detection(s1, s2):
    l1 = sorted(list(s1))
    l2 = sorted(list(s2))
    matches = True
    i = 0
    while i < len(l1) and matches:
        if l1[i] == l2[i]:
            i = i + 1
        else:
            matches = False
    return matches

print anagram_detection('heart','earth')
print anagram_detection('heart','eartg')

#At first glance you may be tempted to think that this algorithm is O(n),
#since there is one simple iteration to compare the n characters after the sorting process.
#However, the two calls to the Python sort method are not without their own cost.
#As we will see in a later chapter, sorting is typically either O(n2) or O(nlogn), so the sorting operations dominate the iteration.
#In the end, this algorithm will have the same order of magnitude as that of the sorting process.
