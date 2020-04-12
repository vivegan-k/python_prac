def word_split(phrase, list_of_words, output =None):
    print 'list_of_words: ', list_of_words
    if output is None:
        output = []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            print word, phrase[len(word):]
            return word_split(phrase[len(word):], list_of_words, output)
    return output
        

print word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
