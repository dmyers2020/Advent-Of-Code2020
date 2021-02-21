# Advent of code Year 2020 Day 7 solution
# Author = David Myers
# Date = December 2020

with open((__file__.rstrip("code.py")+"sample_input.txt"), 'r') as input_file:
    input = input_file.read()
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
input =input.split('\n')

print(input)

print("Part One : "+ str(None))



print("Part Two : "+ str(None))
