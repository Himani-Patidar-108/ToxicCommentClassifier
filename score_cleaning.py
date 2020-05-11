#for regurlar expressions
import re

#for configuration
import config

def toxicity_score(comment):
	'''
	check comment for toxicity
	input: string
	output: value between 0 - 1 indicating toxicity
	'''
	num_toxic_words = 0

	words = comment.split(' ')
	print("Words:", words)

	for word in words:

		# keep only alphabet characters!
		word = re.sub('[^a-zA-Z]+', '', word)
		# convert to lowercase
		word = word.lower()
		if word in config.toxic_words:
			num_toxic_words += 1

	print(f"Toxic Words found:{num_toxic_words}")
	print(f"Comment Length:{len(words)}")
	score = num_toxic_words / len(words)
	return score
