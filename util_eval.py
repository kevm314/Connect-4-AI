#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:51:21 2019

@author: kevorkmouradian
"""


import copy



def UTILITY(state):
    if red is winner:
        return 10000
    elif yellow is winner:
        return -10000
    
    
def EVALUATION(state):
    

    
    return 2
    
    #return SCORE(state, red_player) - SCORE(state, yellow_player)
    
def SCORE(state, player):
    """
    return num_colour_tokens +
            10*NUM_IN_A_ROW(2, state, player) +
            100*NUM_IN_A_ROW(3, state,player) +
            1000*NUM_IN_A_ROW(4 or more, state, player)
    """
    
    
def NUM_IN_A_ROW(count, state, player):
    return """count in a row, column or diagonal"""

def evaluation(state):
    
    #total tokens on the board
    total_tokens = 0
    
    #yellow token counts [double, triple, quadruple or more]
    yellow_counts = [0, 0, 0]
    
    #red token counts [double, triple, quadruple or more]
    red_counts = [0, 0, 0]
    
    #list of coordinates to sweep diagonally from bottom-left to top-right
    l_sweep = [
            (5, 0, 1),
            (4, 0, 2),
            (3, 0, 3),
            (2, 0, 4),
            (1, 0, 5),
            (0, 0, 6),
            (0, 1, 6),
            (0, 2, 5),
            (0, 3, 4),
            (0, 4, 3),
            (0, 5, 2),
            (0, 6, 1)
            ]
    
    #list of coordinates to sweep diagonally from top-left to bottom-right
    r_sweep = [
            (5, 6, 1),
            (5, 5, 2),
            (5, 4, 3),
            (5, 3, 4),
            (5, 2, 5),
            (5, 1, 6),
            (5, 0, 6),
            (4, 0, 5),
            (3, 0, 4),
            (2, 0, 3),
            (1, 0, 2),
            (0, 0, 1)
            ]
    
    #list of coordinates to sweep diagonally from top-left to bottom-right
    up_sweep = [
            (0, 0, 6),
            (0, 1, 6),
            (0, 2, 6),
            (0, 3, 6),
            (0, 4, 6),
            (0, 5, 6),
            (0, 6, 6)
            ]

    #list of coordinates to sweep diagonally from top-left to bottom-right
    side_sweep = [
            (0, 0, 7),
            (1, 0, 7),
            (2, 0, 7),
            (3, 0, 7),
            (4, 0, 7),
            (5, 0, 7)
            ]
    
    #call the sweep method
    [red_counts, yellow_counts, red_tokens_board, yellow_tokens_board] = sweep(state, l_sweep, 'l_sweep', red_counts, yellow_counts, 1)
    [red_counts, yellow_counts] = sweep(state, r_sweep, 'r_sweep', red_counts, yellow_counts)
    [red_counts, yellow_counts] = sweep(state, up_sweep, 'up_sweep', red_counts, yellow_counts)
    [red_counts, yellow_counts] = sweep(state, side_sweep, 'side_sweep', red_counts, yellow_counts)
    
    #check for a definite win
    if red_counts[2] != 0:
        return 10000
    elif yellow_counts[2] != 0:
        return -10000
     
    
    #calculate the respective player scores
    red_score = red_tokens_board + 10 * red_counts[0] + 100 * red_counts[1] +1000 * red_counts[2]
    yellow_score = yellow_tokens_board + 10 * yellow_counts[0] + 100 * yellow_counts[1] +1000 * yellow_counts[2]
    
    return red_score - yellow_score
    
def sweep(state, coordinates, sweep_type, red_counts, yellow_counts, count_the_tokens=0):
    
    
    #total oken counts for each player
    red_tokens_board = 0
    yellow_tokens_board = 0
    
    
    ##############################
    #TEST
    ##############################
    
    
    
    #total tokens on the board
    total_tokens = 0
    
    
    #perform sweep
    for t in coordinates:
                 
        #diagonal counter
        counter = 0
        
        #set the coordinates
        row = t[0]
        col = t[1]
        
        #current token count
        current_token_count = 1
        
        #set the current_token character
        current_token = state.game_board[row][col]
        
        #increment coordinate counter
        counter +=1
        
        
        
        
        if count_the_tokens == 1:
        #increment the token count for each player
            if current_token == 'y':
                yellow_tokens_board += 1
            elif current_token == 'r':
                red_tokens_board += 1
        
        
        
        
        """
        #TEST SWEEP TRAVERSAL
        #################################
        
        state_copy.game_board[row][col] = 'O'
            
        for l in reversed(state_copy.game_board):
            print(str(l))
            
        #################################
        
        a = 1
        """
        
        
        
        
        #iterate until sweep limit has been reached
        while counter < t[2]:
            
            #update coordinates depending on type
            if sweep_type == "l_sweep":
                row += 1
                col += 1
            elif sweep_type == "r_sweep":
                row -= 1
                col += 1
            elif sweep_type == "up_sweep":
                row += 1
            elif sweep_type == "side_sweep":
                col += 1
            
            #extract the test token
            test_token = state.game_board[row][col]
            
            
            
            if count_the_tokens == 1:
            #increment the token count for each player
                if test_token == 'y':
                    yellow_tokens_board += 1
                elif test_token == 'r':
                    red_tokens_board += 1
            
            
            
            
            """
            #TEST SWEEP TRAVERSAL
            #################################
            
            state_copy.game_board[row][col] = 'O'
            
            for l in reversed(state_copy.game_board):
                print(str(l))
            
            #################################
            """
            
            
            
            
            
            #test whether equal type of coloured token
            if current_token == test_token and current_token != '.':
                current_token_count += 1
            #check whether different type of coloured token
            elif current_token != test_token and current_token != '.' and current_token_count > 1:
                
                index = 0
                
                #check class of in-a-row
                if current_token_count == 2:
                    index = 0
                elif current_token_count == 3:
                    index = 1
                elif current_token_count >= 4:
                    index = 2
                
                #update the total count type
                if current_token == 'y':
                    yellow_counts[index] += 1
                elif current_token == 'r':
                    red_counts[index] += 1
                
                
                current_token = test_token
                current_token_count = 1
                
            #otherwise reset token count type
            else:
                current_token = test_token
                current_token_count = 1
           
            
            #increment coordinate count
            counter += 1
        
        #check for board edge in-a-row
        if current_token != '.' and current_token_count > 1:
            
            index = 0
                
            #check class of in-a-row
            if current_token_count == 2:
                index = 0
            elif current_token_count == 3:
                index = 1
            elif current_token_count >= 4:
                index = 2
                    
            #update the total count type
            if current_token == 'y':
                yellow_counts[index] += 1
            elif current_token == 'r':
                red_counts[index] += 1
                
                current_token = test_token
                current_token_count = 1    
        
    #potentially return the token count of individual players as well
    if count_the_tokens == 1:
        return [red_counts, yellow_counts, red_tokens_board, yellow_tokens_board]
    else:
        return [red_counts, yellow_counts]
    
    
    
    
    
    
    
    
    
    