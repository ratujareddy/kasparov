# January 23
# I'm going to attempt to code up a chess board

# A chess board is an 8x8 array

ranks = ['1','2','3','4','5','6','7','8']
files = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
board = [(ranks[i], files[j]) for i in range(len(ranks)) for j in range(len(files))]

board_str = ["".join((x)) for x in board]

class Board:

	def __init__(self):
		self.pieces = 0


for i in range(56, -1, -8):
	print('\t'.join('{} {}'.format(*k) for k in enumerate(board_str[i:i+8])))

