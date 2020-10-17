def reverse_word(sentence):
  words = sentence.split()
  return ' '.join(words[::-1])

print reverse_word('Hello World')
  
