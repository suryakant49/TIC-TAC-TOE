#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import clear output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('--------')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('--------')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('--------')


# In[ ]:


def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    marker = ''
    while not  (marker == 'X' or marker == 'O'):
        marker = input('Player1: Choose X or O: ').upper()
        
    if marker == 'X':
        
        return('X','O')
    else:
        return('O','X')


# In[ ]:


def place_marker(board, marker, position):
    
    board[position] = marker


# In[ ]:


def win_check(board, mark):
    
    # WIN TIC TAC TOE
    
    return((board[7] == mark and board[8] == mark and board[9] == mark) or
           (board[4] == mark and board[5] == mark and board[6] == mark) or
           (board[1] == mark and board[2] == mark and board[3] == mark) or
           (board[7] == mark and board[4] == mark and board[1] == mark) or
           (board[8] == mark and board[5] == mark and board[2] == mark) or
           (board[9] == mark and board[6] == mark and board[3] == mark) or
           (board[7] == mark and board[5] == mark and board[3] == mark) or
           (board[9] == mark and board[5] == mark and board[1] == mark))


# In[ ]:


import random

def choose_first():
    
    flip = random.randit(0,1)
    
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'


# In[ ]:


def space_check(board, position):
    
    return board[position] == ' '


# In[ ]:


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    # BOARD IS FULL IF WE RETURN TRUE
    return True


# In[ ]:


def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('choose a position: (1-9)'))
        
        return position


# In[ ]:


def replay():
    
    choice = input('Play Again? Enter Yes or No')
    
    return choice == 'yes'


# In[ ]:


# while loop to keep running the game
print('welcome to TIC TAC TOE ')

while True:
    #Play the game
    
    ##set everything up (Board, whos first, choose markers X,O )
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + 'will go first')
    
    play_game = input('ready to play? y or n?')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
        
    ## Game play
    
    while game_on:
        
        if turn == 'Player 1':
            #show the board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,player1_marker,position)
            
            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('player 1 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('tie again')
                    game_on = False
                else:
                    turn = 'player 2'
                    
                    
                    
    if not replay():
        break

