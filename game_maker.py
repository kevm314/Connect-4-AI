#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 21:59:52 2019

@author: kevorkmouradian
"""

import math
import time
import copy
import tree
import state_maker
from collections import deque
import util_eval

#generate states builds the game tree from the root state
def generate_states(root_state, max_depth, max_player):
    
    #create the game_tree rooted at the root_state
    game_tree = tree.tree(root_state)
    
    #craete the fringe and expanded lists based on index
    fringe = deque([0])
    expanded = deque([])
    
    #the root_player is MAX, the enemy_player is MIN
    #MAX corresponds to even layers, MIN corresponds to odd layers
    if max_player == 'red':
        min_player = 'yellow'
        max_token = 'r'
        min_token = 'y'
    else:
        min_player = 'red'
        max_token = 'y'
        min_token = 'r'
    
    fringe_length = 1
    
    total_time = 0
    
    
    
    #check state node depth
    while fringe_length > 0:
        
        
        
        
        #set current node to explore
        current_node = fringe.popleft()
        fringe_length -= 1
        
        #extract nodes level
        node_level = game_tree.attributes[current_node][4]
        
        
        if node_level == max_depth:
            return game_tree
        
        #extract current node's battlefront
        current_battle_front = game_tree.nodes[current_node].battle_front
        
        #set the token of play
        if node_level % 2 == 0:
            token = max_token
        else:
            token = min_token
        
        #counter for the columns
        column_counter = 0
        
        
        
        
        
        
        
        
        #################################
        #TEST
         #################################
        #TESTING
        #testing(game_tree.nodes[current_node], node_level)
        
        
        #check for an end of game state
        if (abs(util_eval.evaluation(game_tree.nodes[current_node])) == 10000):
            continue
        
        
        
        
        
        #iterate through the columns of the battlefront
        for c in current_battle_front:
            
            #check whether the column is saturated up to the top
            if c > 5:
                #move to the next olumn
                column_counter += 1
                
                
                
                #continue iteration through the columns
                continue
            
            
            #set it equal to the current battle front
            child_battle_front = copy.deepcopy(current_battle_front)
            
            
            #increment the slot position where a token is added
            child_battle_front[column_counter] += 1
            
            
            #create the child game board
            child_game_board = copy.deepcopy(game_tree.nodes[current_node].game_board)
            
            
            #add the token as a character
            child_game_board[c][column_counter] = token
            
            #create the state object
            child_state = state_maker.state(child_game_board, child_battle_front)
            
            #extract parent state
            parent_state = game_tree.nodes[current_node]
            
            
            #connect the states
            game_tree.connect(parent_state, child_state)
            
            
            
            #increment the column counter
            column_counter += 1
            
            
            
            
            
            
            
            
            #################################
            #TEST
            #################################
            #testing(child_state, node_level+1)
            
            
        #once done with current node add its children to the fringe
        fringe += game_tree.children[current_node] 
        fringe_length += len(game_tree.children[current_node])         
            
            
            
            
        
        
        
    #CLEAN UP COMMENTING
    #print("clean up test comments here and need to implement EVAL FUNCTION and MINIMAX CHECK FULL TEST CASE WRONG")
    

    
    


    
    return game_tree



"""
def testing(state, node_level):
    print("UPSIDE DOWN ^")
    print('\n' + str(node_level) + '\n')
    for l in reversed(state.game_board):
        print(str(l))

    print(state.battle_front)
    print('\n\n\n')
"""