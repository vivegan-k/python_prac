from collections import Counter

li = [1,2,3,4,3,2,1,6,6,7,8,8,9,9,9,10]

count_li = Counter(li)

print count_li
print dict(count_li)
print list(count_li)

string = 'asdfasfgsfgfsgvdsfdcfsvqwdfadzcv'
counter_str = Counter(string)
print counter_str, type(counter_str)

sent = 'this is to check how many time the word word occurs in sentence of set of word'
counter_sent = Counter(sent.split())
print counter_sent
print counter_sent.most_common(2)
print sum(counter_sent.values()) # To identify number of words
print counter_sent.items()
#print counter_sent[:-n-1:-1] #To get least common word
