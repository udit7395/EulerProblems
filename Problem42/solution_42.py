import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def generate_triangle_sequence(limit):
	triangle_sequence = []
	for n in range(1, limit):
		triangle_sequence.append(0.5 * n * (n + 1))
	return triangle_sequence

def get_word_value(word):
	aggregate = 0
	for letter in word:
		aggregate += int(characeter_sequence.get(letter.lower()))
	return aggregate

def generate_character_sequence():
	characeter_sequence = {}
	index = 1
	for x in range(97, 123):
		characeter_sequence[chr(x)] = index
		index += 1
	return characeter_sequence

timer = timing()

limit = 1000
triangle_sequence = generate_triangle_sequence(limit)
characeter_sequence = generate_character_sequence()
triangle_word_count = 0

input_file = open('words.txt','r')

words = input_file.read()
words = words.replace("\"","")
words = words.split(",")

for word in words:
	if get_word_value(word) in triangle_sequence:
		triangle_word_count += 1

timer("Using words.txt, a 16K text file containing nearly two-thousand common English words, there are {} triangle words".format(triangle_word_count))

