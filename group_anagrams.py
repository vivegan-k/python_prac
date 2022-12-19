import imp


import collections

def groupAnagrams(strs):
    ans = {}

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        print(count)
        if tuple(count) not in ans:
            ans[tuple(count)] = [s]
        else:
            ans[tuple(count)].append(s)
        print(ans)
    return ans.values()

strings = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strings))