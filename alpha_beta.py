#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 20:22:48 2019

@author: kevorkmouradian
"""

import math
import util_eval
from collections import deque


def minimum(game_tree, state_node, alpha, beta, max_depth):
    
    total_count = 1
    
    #solution index
    sol_index = 0
    
    #total count of expanded nodes
    total_count = 1
    
    #check for a terminal node
    if len(game_tree.children[state_node]) == 0:
        
        
        #return the utility value of this node
        return util_eval.evaluation(game_tree.nodes[state_node]), total_count, state_node
    
    #check if max depth reached
    if game_tree.attributes[state_node][4] == max_depth:
        #evaluate the evaluation or utility function at this node
        return util_eval.evaluation(game_tree.nodes[state_node]), total_count, state_node
    
    
    #go through children, and find min values
    for child in game_tree.children[state_node]:
        [returned_value, count, index] = maximum(game_tree, child, alpha, beta, max_depth)
        
        #increment the total count
        total_count += count
        
        #if the child returns a beta value greater than or equal to the current value
        #then terminate the search
        if returned_value <= alpha:

            return [returned_value, total_count, sol_index]
        #check if a greater value found
        elif returned_value < beta:
            beta = returned_value
            #update the solution index
            sol_index = child

            

    return [beta, total_count, sol_index]



def maximum(game_tree, state_node, alpha, beta, max_depth):
    
    total_count = 1
    
    #solution index
    sol_index = 0

    #total count of expanded nodes
    total_count = 1
    
    #check for a terminal node
    if len(game_tree.children[state_node]) == 0:
        #return the utility value of this node
        return util_eval.evaluation(game_tree.nodes[state_node]), total_count, state_node
    
    #check if max depth reached
    if game_tree.attributes[state_node][4] == max_depth:
        #evaluate the evaluation or utility function at this node
        return util_eval.evaluation(game_tree.nodes[state_node]), total_count, state_node
    
    
    #go through children, and find min values
    for child in game_tree.children[state_node]:
        [returned_value, count, index] = minimum(game_tree, child, alpha, beta, max_depth)
        
        #increment the total count
        total_count += count
        
        #if the child returns a beta value greater than or equal to the current value
        #then terminate the search
        if returned_value >= beta:
            
            return [returned_value, total_count, sol_index]
        
        #check if a greater value found
        elif returned_value > alpha:
            alpha = returned_value
            #update the solution index
            sol_index = child
    
        
    
    
    return [alpha, total_count, sol_index]

def ab_dfs(game_tree, max_depth, player):
    
    #instantiate the count of expanded nodes
    count = 0
    
    
    #initialise alpha and beta
    alpha = float("-inf")
    beta = float("inf")    
    
    #check for max
    if player == 'red':
        #start off with max
        [final_parameter, count, index] = maximum(game_tree, 0, alpha, beta, max_depth)
    else:
        #start off with min
        [final_parameter, count, index] = minimum(game_tree, 0, alpha, beta, max_depth)
        
    return [final_parameter, count, index]