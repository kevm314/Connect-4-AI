#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:59:06 2019

@author: kevorkmouradian
"""


import math
import util_eval
from collections import deque



def m_dfs(game_tree, max_depth, player):
    
    rolling = 0
    
    expanded_set = 0
    
    fringe = deque([[0, 0]])
    expanded = []
    
    #calibrate the min, max level type for red and yellow players
    if player == 'red':
        #set the modulo operator result
        #to set even levels as max
        player_type = 0
    else:
        #set the modulo operator result
        #to set even levels as min
        player_type = 1
    
    fringe_length = 1
    
    #iterate while fringe is non-empty
    while fringe_length > 0:
        
        #extract a node to explore
        current_node_group = fringe.pop()
        fringe_length -= 1
        
        #extract index
        current_node = current_node_group[0]
        
        #extract whether expanded
        expanded = current_node_group[1]
        
        #check depth of the node
        depth = game_tree.attributes[current_node][4]
        
        #set player type for this level
        if depth % 2 == player_type:
            #MAX
            player = 'max'
        else:
            #MIN
            player = 'min'
        
        #get the parent's minimax value
        parent_node_index = game_tree.attributes[current_node][0]
        parent_node_minimax = game_tree.nodes[parent_node_index].parameter
        
        #check whether node explored
        if expanded == 0:
            
            #not expanded
            
            #increment expanded count
            expanded_set += 1
            
            #check whether max depth node or if leaf
            if depth == max_depth or len(game_tree.children[current_node]) == 0:
                
                
                #############################
                #call an evaluation function#
                #############################
                game_tree.nodes[current_node].parameter = util_eval.evaluation(game_tree.nodes[current_node])
                
                #set the leaf's minimax value
                current_node_minimax = game_tree.nodes[current_node].parameter

                
                #set parent's minimax value via comparison
                
                ############################
                #PERFORM MINIMAX COMPARISON#
                ############################
                
                #check whether parent has a minimax value set
                if math.isnan(parent_node_minimax):
                    #no minimax value set
                    game_tree.nodes[parent_node_index].parameter = current_node_minimax
                elif player == 'max':
                    #parent is min
                    if current_node_minimax < parent_node_minimax:
                        #child has smaller value
                        game_tree.nodes[parent_node_index].parameter = current_node_minimax
                else:
                    #parent is max
                    if current_node_minimax > parent_node_minimax:
                        #child has bigger value
                        game_tree.nodes[parent_node_index].parameter = current_node_minimax
                
                
                #set as expanded
                current_node_group[1] = 1
                 
                
                
                #continue to next node
                continue
              
            #node is unexpanded, but is not a leaf node    
            
            #now add the parent before the children so as to double check its own
            #minimax value with its parent's value
            fringe.append(current_node_group)
            fringe_length += 1
            
            #add children to the front of the fringe
            for c in reversed(game_tree.children[current_node]):
                child_group = [c,0]
                
                fringe.append(child_group)
                fringe_length += 1
            
            
            #set as expanded
            current_node_group[1] = 1
        
        
        else:
            #node already expanded
            #i.e. second visit of a parent
            
            #extract current node's minimax value
            current_node_minimax = game_tree.nodes[current_node].parameter
            
            
            ########################################
            #PERFORM MINIMAX COMPARISON WITH PARENT#
            ########################################
            
            #check whether parent has a minimax value set
            if math.isnan(parent_node_minimax):
                #no minimax value set
                game_tree.nodes[parent_node_index].parameter = current_node_minimax
            elif player == 'max':
                #parent is min
                if current_node_minimax < parent_node_minimax:
                    #child has smaller value
                    game_tree.nodes[parent_node_index].parameter = current_node_minimax
            else:
                #parent is max
                if current_node_minimax > parent_node_minimax:
                    #child has bigger value
                    game_tree.nodes[parent_node_index].parameter = current_node_minimax
                    
    
    return expanded_set