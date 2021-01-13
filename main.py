# https://rosettacode.org/wiki/Bulls_and_cows

# Create a four digit random number from the digits   1   to   9,   without duplication.
# The program should:
  # ask for guesses to this number
  # reject guesses that are malformed
  # print the score for the guess
# The score is computed as:
  # The player wins if the guess is the same as the randomly chosen number, and the program ends.
  # A score of one bull is accumulated for each digit in the guess that equals the corresponding digit in the randomly chosen initial number.
  # A score of one cow is accumulated for each digit in the guess that also appears in the randomly chosen number, but in the wrong position.
  
import random
import re

# global variables
# valid_symbols is assumed to contain only unique symbols
valid_symbols = '123456789'

def main():
	print('***Bulls and cows program***')
	print('(aka Mastermind)')
	print('In this program, you will be attempting to find the correct sequence given the "bulls" and "cows" for each guess you make.')
	print('For each symbol in your guess that is in the correct place, you get one bull.')
	print('For each symbol in your guess that exists in the answer but is in the wrong place, you get one cow.')
	print('No symbol will be repeated.')	
	print('The valid symbols are:', valid_symbols)
	print()
	
	gameloop = True
	while gameloop:
		# create an answer in the format '#####'
		sequence_length = input_sequence_length(len(valid_symbols))
		answer = ''.join(random.sample(valid_symbols, sequence_length))
		
		guess_count = 0
		guessloop = True
		while guessloop:
			guess_count += 1
			
			# get a valid guess
			guess = validate_guess(sequence_length)
			
			if guess == answer:
				print(f'Correct! You found the answer in {guess_count} guesses.')
				guessloop = False
				continue
			else:
				# process the guess
				result = process_guess(guess, answer)
				print(f'{result[0]} bulls, {result[1]} cows')
		
		gameloop = play_again_prompt()

# processes the guess against the answer by determining the number of bulls and cows
# returns a tuple with the number of bulls and cows, respectively
def process_guess(guess, answer):
	bulls = 0
	cows = 0
	for i, v in enumerate(guess):
		# symbol in correct place
		if v == answer[i]:
			bulls += 1
		# symbol is in answer but is in incorrect place
		elif v in answer:
			cows += 1
	return (bulls,cows)
	
# asks user for a guess and makes sure it is valid for the given sequence
# returns the user's guess
def validate_guess(sequence_length):
	while True:
		try:
			print()
			guess = input('Make a guess: ')
			if len(guess) != sequence_length:
				raise ValueError('LengthError')
			for i, v in enumerate(guess):
				if v not in valid_symbols:
					raise ValueError('UnknownSymbolError')
				if v in guess[i+1:]:
					raise ValueError('DuplicateError')
			return guess
			
		except ValueError as err:
			err = str(err)
			if err == 'LengthError':
				print(f'The guess must be exactly {sequence_length} symbols long.')
			elif err == 'UnknownSymbolError':
				print(f'The guess must contain only these symbols: {valid_symbols}')
			elif err == 'DuplicateError':
				print(f'The guess must not contain more than one of the same symbol.')
			else:
				print('I just don\'t know what went wrong!')

# asks user for sequence length and returns it
def input_sequence_length(max_len):
	while True:
		try:
			n = int(input('How long should the sequence be this round: '))
			if n <= 1 or n > max_len:
				raise ValueError
			return n
			
		except ValueError:
			print(f'Please enter a number greater than 1 and less than {max_len + 1}.')

# asks user if they want to play again
# returns their answer
def play_again_prompt():
	while True:
		keep_playing_input = input('Keep playing? (y/n) ');
		if re.search('^y(es)?$', keep_playing_input, re.IGNORECASE):
			print('Starting new game...')
			print()
			return True
		elif re.search('n(o)?$', keep_playing_input, re.IGNORECASE):
			print('Thanks for playing!')
			print()
			return False
		else:
			print('Invalid input.')
			continue

main()