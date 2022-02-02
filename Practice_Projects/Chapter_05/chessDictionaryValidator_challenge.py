#In this chapter, we used the dictionary value 
# {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', 
# '5h': 'bqueen', '3e': 'wking'}
# to represent a chess board. Write a function named 
# isValidChessBoard() that takes a dictionary argument
# and returns True or False depending on if the board 
# is valid.
#A valid board will have exactly one black king and 
# exactly one white king. Each player can only have at 
# most 16 pieces, at most 8 pawns, and
#all pieces must be on a valid space from '1a' to '8h'; 
# that is, a piece can’t be on space '9z'. The piece 
# names begin with either a 'w' or 'b' to represent 
# white or black, followed by 'pawn', 'knight', 
# 'bishop', 'rook', 'queen', or 'king'. This function
# should detect when a bug has resulted in an improper
# chess board.

current_board = {'1a': 'bking', '2a': 'bqueen', '3a': 'bknight',
                 '4a': 'bbishop', '5a': 'brook', '6a': 'bpawn',  
                 '1b': 'wking', '2b': 'wqueen', '3b': 'wknight',
                 '4b': 'wbishop', '5b': 'wrook', '6b': 'wpawn'}


def isValidChessBoard(board):
    coordinate_x = [1, 2, 3, 4, 5, 6, 7, 8]
    coordinate_y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    position = []

    #Create all possible positions on board (1a - 8h)
    for x in coordinate_x:
        for y in coordinate_y:
            position.append(f'{x}{y}')
    
    correct_number = True
    correct_pieces = True
    correct_positions = True

    king_w = 0
    king_b = 0
    queen_w = 0
    queen_b = 0
    bishop_w = 0
    bishop_b = 0
    rook_w = 0
    rook_b = 0
    knight_w = 0
    knight_b = 0
    pawn_w = 0
    pawn_b = 0

    total_w = 0
    total_b = 0

    #Check if position is a valid position
    for pos in board.keys():
        if pos not in position:
            correct_positions = False
            print(f'{pos} is not a valid position')
            break
        else:
            #Check if piece is a valid piece and count
            piece = board[pos]

            if piece == 'wking':
                king_w += 1
            elif piece == 'wqueen':
                queen_w += 1
            elif piece == 'wbishop':
                bishop_w += 1
            elif piece == 'wrook':
                rook_w += 1
            elif piece == 'wknight':
                knight_w += 1
            elif piece == 'wpawn':
                pawn_w += 1
            elif piece == 'bking':
                king_b += 1
            elif piece == 'bqueen':
                queen_b += 1
            elif piece == 'bbishop':
                bishop_b += 1
            elif piece == 'brook':
                rook_b += 1
            elif piece == 'bknight':
                knight_b += 1
            elif piece == 'bpawn':
                pawn_b += 1
            else:
                correct_pieces = False
                print(f'{board[pos]} is not a valid piece')
                break
    
    total_w = king_w + queen_w + rook_w + bishop_w + knight_w + pawn_w
    total_b = king_b + queen_b + rook_b + bishop_b + knight_b + pawn_b

    #Right amount of pieces?
    if (king_w > 1) or (king_b > 1):
        print('Too many Kings!')
        correct_number = False
    elif (king_w == 0) or (king_b == 0):
        print('Not enough Kings!')
        correct_number = False
    elif (queen_w > 1) or (queen_b > 1):
        print('Too many Queens!')
        correct_number = False
    elif (rook_w > 2) or (rook_b > 2):
        print('Too many Rooks will spoil your wrath!')
        correct_number = False
    elif (bishop_w > 2) or (bishop_b > 2):
        print('Too many Bishops!')
        correct_number = False
    elif (knight_w > 2) or (knight_b > 2):
        print('Too many Knight!')
        correct_number = False
    elif (pawn_w > 8) or (pawn_b > 8):
        print('Too many Pawns!')
        correct_number = False
    elif (total_w > 16) or (total_b > 16):
        print('Too many pieces!')
        correct_number = False
    else:
        correct_number = True

    if correct_pieces and correct_number and correct_positions == True:
        return True
    else:
        return False

print(isValidChessBoard(current_board))
