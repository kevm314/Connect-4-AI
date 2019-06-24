#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:47:07 2019

@author: kevorkmouradian
"""
import time
import sys
import ConnectFour_bench
import state_maker
import util_eval


#starting board
board = ".......,.......,.......,.......,.......,......."
battle_front = [0, 0, 0, 0, 0, 0, 0]

turn_counter = 0


while(1):
    #prompt for user input    
    print("Do you wish to play first?")
    print("'y' for yes and 'n' for no")
    
    human_colour = input()
    
    if human_colour == 'y':
        #check for yes and set 0 as yes
        human_colour = 1
        break
    elif human_colour == 'n':
        #check for no and set 1 as no
        human_colour = 0
        break
    else:
        #invalid input 
        print("Invalid input!\n")

while(1):
    


    if(turn_counter%2 == human_colour):
        player = "red"
        token = "r"
        
        inp = ["ConnectFour.py", board, player, "A", "4"]
        
        bench_column = ConnectFour_bench.play_bench(inp)
        
        ply = "AI"
        
    else:
        player = "yellow"
        token = "y"
        
        
        
       
        
        while(1):
            print("Enter a column to play in [0-6]:\n")
            
            bench_column_raw = input()
            
        
            #check for valid input
            if bench_column_raw.isdigit() == True:
                bench_column = int(bench_column_raw)
                if bench_column >= 0 and bench_column <= 6:
                    break
            
            #invalid input
            print("Invalid input!")
        
        
        ply = "Human"
    
    
    #######RECONSTRUCT THE GAME BOARD########
    #CHECK FOR A WINNER#
    
    layers_str = board.split(',')
    
    layers = []
    test_layers = []
    
    counter = 0
    while counter < 6:
        s = list(layers_str[counter])
        
        if (counter == battle_front[bench_column]):
            s[bench_column] = token
        
        layers.append(''.join(s))
        test_layers.append(s)
    
        counter += 1
    
    
    board = layers[0] + ',' + layers[1] + ',' + layers[2] + ',' + layers[3] + ',' + layers[4] + ',' + layers[5] 
    battle_front[bench_column] += 1
    
    
    game_state = state_maker.state(test_layers)
    
    print(ply + " plays...\n")

    rows = board.split(',')
    for r in reversed(rows):
        print(r)
    
    print('\n')
    print('\n')
    print('\n')
    
    
    if ((util_eval.evaluation(game_state)) == 10000):
        print(ply + " WON")
        break
    elif ((util_eval.evaluation(game_state)) == -10000):
        print(ply + " WON")
        break
    

    turn_counter += 1
    










