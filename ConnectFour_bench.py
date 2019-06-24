#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:47:07 2019

@author: kevorkmouradian
"""
import time
import sys
import state_maker
import game_maker
import minimax
import alpha_beta
import util_eval

def find_battle_front(game_board):
    
    #set the respective counters
    row_counter = 0
    
    #battle front has the first unmarked position
    #ready to play in any column
    battle_front = [10 for x in range(7)]
    
    #for efficiency, when battlefront entires are filled, terminate search
    #do this using a counter of entries
    num_entries = 7
    
    for r in game_board:
        
        #reset after iterating through a 'row' of columns
        column_counter = 0
        
        for c in r:
            #check empty position and if 
            #this position is truly in the battlefront
            if c == '.' and battle_front[column_counter] == 10:
                #set the current empty position as the current row index
                battle_front[column_counter] = row_counter
                num_entries -= 1
                
            column_counter += 1
            
            
            
        row_counter += 1
        
        #check if battle front is filled after every row iterations
        if num_entries == 0:
            break
        
    return battle_front




def play_bench(inp):
    
    #colour to play
    player = inp[2]
    
    #algorithm type
    algorithm = 'A'
    
    #maximum depth to search state space
    max_depth = int(inp[4])
    
    
    #parse rows of the game board
    rows = inp[1].split(',')
    
    #game board variable
    game_board = []
    
    #parse the game state into a 2D matrix of characters
    for r in rows:
        game_board.append(list(r))
        
    
    #find the battle front
    battle_front = find_battle_front(game_board)
    
    start = time.time()  
    #convert the original game board into a state   
    root_state = state_maker.state(game_board, battle_front)
    end = time.time()
  
    
    
    start = time.time() 
    #create the game tree down to some maximum depth
    game_tree = game_maker.generate_states(root_state, max_depth, player)
    end = time.time()

    
    column_to_play_in = 0
    
    #perform the appropriate algorithm
    if algorithm == 'M':
        #perform minimax
        number_expanded = minimax.m_dfs(game_tree, max_depth, player)
    
        #check where the minimax parameter game from
        
        
        #count column to play in and child's minimax value
        final_parameter = game_tree.nodes[0].parameter
        
        
        column_to_play_in = 0
        
        #check which column to play in
        #reverse to check children in reverse
        for k in reversed(game_tree.children[0]):
            
            if game_tree.nodes[k].parameter == final_parameter:
                
                counter = 0
                
                while counter < 7:
                    if game_tree.nodes[k].battle_front[counter] != game_tree.nodes[0].battle_front[counter]:
                        column_to_play_in = counter
                        break
                    counter += 1
                    
        return column_to_play_in
        
        
    else:
        #perform alpha beta pruning
        final_parameter, count, index = alpha_beta.ab_dfs(game_tree, max_depth, player)
        
        counter = 0
                
        while counter < 7:
            if game_tree.nodes[index].battle_front[counter] != game_tree.nodes[0].battle_front[counter]:
                column_to_play_in = counter
                break
            counter += 1
        
        return column_to_play_in
        
        
    
    





