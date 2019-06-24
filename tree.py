#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 15:20:55 2019

@author: kevorkmouradian
"""

from collections import deque

class tree():
    
    
    def __init__(self, root):
        
        #node objects in tree
        self.nodes = []
        
        #indexed list of children
        self.children = []
        
        self.num_nodes = 1
        
        #attributes for every node by index
        #order of attributes: parent index, edge value to parent, h-value, root-cost, level value
        self.attributes = []
        
        #add root to nodes of tree
        self.nodes.append(root)
        
        #add empty list for root
        self.children.append([])
        
        #set attributes for the root, by index
        self.attributes.append([0, 0, -1, 0, 0])
        
        
    def connect(self, parent, child, descriptor=1, h=1):
        
        #check whether state already exists
        #child_exists = 0
        
        #try and see if node contained else add it to list
        
        parent_index = self.nodes.index(parent)
        
        
        self.num_nodes += 1
            
            
        #try and see if node contained else add it to list
        
        
        self.nodes.append(child)
            
        #add empty list for child's own future children
        self.children.append([])
            
        #get child's cost to root
        child_root_cost = self.attributes[parent_index][3] + descriptor
            
        #get child's level value
        child_level = self.attributes[parent_index][4] + 1
            
        #set child attributes
        child_attributes = [parent_index, descriptor, h, child_root_cost, child_level]
            
        #append the attributes
        self.attributes.append(child_attributes)
            
        #get the child's index value
        child_index = self.num_nodes - 1#self.nodes.index(child)
            
        #set parent as having this child, specifty the child's index
        self.children[parent_index].append(child_index)
          
        
        
        
        
        
 
"""        
        
my_tree = tree('S')

#instantiate the tree
h_nodes = [      ['S', 'A' , 4, 2],
                 ['S', 'B' , 3, 1],
                 ['A', 'C' , 4, 0],
                 ['A', 'D' , 1, 1],
                 ['D', 'H' , 0, 15],
                 ['D', 'I' , 1, 0],
                 ['D', 'J' , 6, 3],
                 ['B', 'E' , 5, 0],
                 ['B', 'F' , 4, 2],
                 ['B', 'G' , 1, 1],
                 ['G', 'K' , 3, 0]
                ]
            
                

for edges in h_nodes:
    my_tree.connect(edges[0], edges[1], edges[2], edges[3])
    
    
#print(str(my_tree.attributes))
print(str(my_tree.nodes))
print(str(my_tree.children))

"""