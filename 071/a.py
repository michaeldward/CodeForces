i = int(raw_input())

words = []

for x in range(0, i):
	word = raw_input()
	if (len(word)>10):
		newWord = word[0] + str(len(word) - 2) + word[len(word) - 1]
		words.append(newWord)
	else:
		words.append(word)

for x in words:
	print x