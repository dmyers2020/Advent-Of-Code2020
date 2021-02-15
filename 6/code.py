# Advent of code Year 2020 Day 6 solution
# Author = David Myers
# Date = December 2020
import math
import os
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

##split list into groups
    input=input.split('\n\n')

##combine group inputs 
    group =[]
    for i in input:
        group.append(i.replace("\n",""))

##search group for unique inputs        
def yesbygroup (group_num):
    '''
    takes list of questions each passeneger said yes to as separate rows within the group
    returns the count of the unique questions from that group
    '''
    questions_answered_yes = []
    for each in group_num:
        if each not in(questions_answered_yes):
##            print(each)
            questions_answered_yes.append(each)
    return(len(questions_answered_yes))

group_sum = 0
for group_num in group:
##    print(group_num)
    group_sum += yesbygroup(group_num)
##    print(group_sum)

print("Part One : "+ str(group_sum))



print("Part Two : "+ str(None))
