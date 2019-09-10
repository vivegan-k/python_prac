def sentence_reversal(s):

    i = 0
    spaces = [' ']
    words = []
    length = len(s)
    print s[i]
    while i < length:
        print i
        if s[i] != ' ':
            start_letter_index = i
            while i < length and s[i] not in spaces:
                i+=1
            words.append(s[start_letter_index:i])
        i += 1
    print words
    return " ". join(reversed(words))

print sentence_reversal('   Hey vivek!   How are  you ')
                
