# Advent of code Year 2020 Day 7 solution
# Author = David Myers
# Date = December 2020

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
'''
initial thoughts: taking a peek at the input tells shows that there's a lot more than just the 9 example rules they provided.
i'm thinking I need to:
 - split the input on newline '\n'
  - define a 'rule' class
    attributes:
        self_description (color_mod, color)
        content_description (quantity, color_mod, color)
 - create objects for each rule in input (list comp)

'''
    input=input.split('\n')



print("Part One : "+ str(None))



print("Part Two : "+ str(None))
