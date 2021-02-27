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
import re
## create a dictionary
bags_dict = {} #initialize the dictionary
for bag in data: #populate the dcitionary
    bag = bag.replace(" bags", "").replace(" bag", "").replace(".", "") #remove irrelevant text
    bag = bag.split(" contain ") #split each entry into parent and child
    bags_dict[bag[0]] = [bag[1]] #populate the dictionary Key: parent, value: child

for key, value in bags_dict.items():
	bags_dict[key] = value[0].split(', ')  #split the values into a list by comma

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

# print("Part One : "+ str(None))
#
#
#
# print("Part Two : "+ str(None))
