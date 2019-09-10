input = "who am i"

def reverse_words(input):
	li = input.split()
	return ' '.join(li[::-1])
	#output_li = [li[i] for i in range(len(li)-1, -1, -1)]
	#return ' '.join(output_li)
	
print reverse_words(input)
		