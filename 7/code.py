# Advent of code Year 2020 Day 7 solution
# Author = David Myers
# Date = December 2020

with open((__file__.rstrip("code.py")+"sample_input.txt"), 'r') as input_file:
    data = input_file.read().split(".\n")
'''
initial thoughts: taking a peek at the input tells shows that there's a lot more than just the 9 example rules they provided.
i'm thinking I need to:
 - split the input on newline '\n' to separate rules
 - split each rule on ',' to get list of contents
 - keyword 'contain' preceeds allowed quantity of each kind of contents
    - quantity special case: 'no other'
    - quantity otherwise: regex number in  each content
  - define a 'bag' class?
    attributes:
        self_description (color_mod, color)
        content_description (quantity, color_mod, color)
 - create objects for each bag in input (list comp?)

 how many colors can, eventually, contain at least one shiny gold bag?
    - we only count the OUTTERMOST BAG, using sample_input, the answer should be 4

 - a directed graph using tuples?

 - note that in part 1, it doesn't seem that the quantities given in the rules,
  have any relevance; so they probably DO in part 2, as costs for each arc

  - rule pattern: 'color_mod color useless [qty, no] color_mod color, [[qty, no] color_mod color]

'''

import collections
'''
initialize a class to explore DFS
'''
class Tree_Node:
    def __init__(self,root_value,children_nodes):
        self.value = root_value
        self.children = children_nodes
'''
Breadth First Search function
takes in a Root_Node
traverses the children of that root according to 
the BFS algo
'''
def bfs(Root_Node):
    '''
dequeue() [DOUBLY ENDED QUEUE] is like a list indexed in both directions; which
makes it easier to add/delete values because you can traverse the list from either direction
append() appendleft() pop() popleft()
***note***  pop - does what it says; it pops the value out, so you can USE it (assign to a var
'''    
    queue = collections.deque() #create an empty doubly ended queue
    queue.append(Root_Node.value) # add the input to the function to the queue
    
    while queue: #while the list is not empty (we're gonna be popping)
        node_value = queue.popleft() #set the node_value as the first entry in the queue
        print(node_value)
        children_nodes = bags_dic[node_value]
        
        for i in children_nodes:
            if i == None or 'no other': #if your at a leaf (a node that has no children)
##                print(i + ' no other?')
                continue #don't throw an error - instead; just run again
            queue.append(i)
        

'''
create the tree as a dictionary for our algo to traverse
'''
import re

## create a dictionary
bags_dic = {} #initialize the dictionary
for bag in data: #populate the dcitionary
    bag = bag.replace(" bags", "").replace(" bag", "").replace(".", "") #remove irrelevant text
    bag = bag.split(" contain ") #split each entry into parent and child
    bags_dic[bag[0]] = [bag[1]] #populate the dictionary Key: parent, value: child

for key, value in bags_dic.items():
    bags_dic[key] = value[0].split(', ')  #split the values into a list by comma
    for i in range(len(bags_dic.get(key))): #for all the values of this key
        bags_dic.get(key)[i] = re.sub("\d+ ", "", bags_dic.get(key)[i]) #drop the quantities
##        print(bags_dic.get(key)[i])
'''
create an object of the root node class 
initialize it with the first item in the dictionary
'''
root_node_value = next(iter(bags_dic.keys())) #iterate thru the dictionary keys
root_node_children = next(iter(bags_dic.values())) #iterate through the values
root_node = Tree_Node(root_node_value,root_node_children) #create a roote node object using the key:value pair

bfs(root_node)

"""
def bag_check(bags_dict, bag, bags_holding_gold, iterations):
    '''
    takes in a dict and a bag (key)
    checks the items associated with that key.
    recurses until the key has no items; or contains a 'shiny gold'
    returns the list of bags which can eventually contain a 'shiny gold'
    '''
    for bag in bags_dict.keys():
    ##    print(bag)
        none_check = bags_dict.get(bag)
        if none_check is not None and iterations<1000 : #catch none types and inf loops
            for item in bags_dict.get(bag): #check each item in that bag
                item = re.sub("\d+ ", "", item) #drop the number and the space

                if item in bags_holding_gold:
                    bags_holding_gold.append(key) #this bag holds a bag which can hold shiny gold
                if 'shiny gold' in item:  #if any of the items are a shiny gold bag note the bag its held by
    ##                print(key, bag, item, bags_holding_gold)
                    bags_holding_gold.append(bag)
                bag_check(bags_dict, item, bags_holding_gold, iterations) #recursively check to see if an item in the bag could hold a shiny gold
            iterations +=1
    return(bags_holding_gold)


bags_holding_gold =[]
##for key in bags_dict.keys(): #check each bag in the in the dictionary
   ##    print(key)
bag_check(bags_dict, 1, bags_holding_gold,0) #i'm not sure what this will do

##bags_holding_gold= set(bags_holding_gold)

print(len(bags_holding_gold))
print(bags_holding_gold)

 print("Part One : "+ str(None))



 print("Part Two : "+ str(None))
"""
