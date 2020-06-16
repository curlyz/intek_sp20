from cardinal_numeral import integer_to_english_numeral, integer_to_vietnamese_numeral
import random

useCloud = False

for i in range(10000):
	randomNumber = random.randrange(0, 999999999999)
	# print('Test South')
	# integer_to_vietnamese_numeral(randomNumber, region='south', activate_tts=True, usingCloud = useCloud)
	# print('Test North')

	# integer_to_vietnamese_numeral(randomNumber, region='north', activate_tts=True, usingCloud = useCloud)
	
	print('Test English')

	integer_to_english_numeral(randomNumber, activate_tts=True, usingCloud = useCloud)