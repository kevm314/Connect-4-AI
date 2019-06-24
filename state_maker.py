#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 21:38:51 2019

@author: kevorkmouradian
"""


class state():
    
    
    def __init__(self, game_board, battle_front=[]):
        
        #set the 2D game board
        self.game_board = game_board
        
        #set the battle front list
        self.battle_front = battle_front
        
        #set the prune/minimax values, initalised as NaN
        self.parameter = float('NaN')
        





