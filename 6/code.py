# Advent of code Year 2020 Day 6 solution
# Author = David Myers
# Date = December 2020
import math
import os
import string
##require collections
from collections import Counter

with open((__file__.rstrip("code.py")+"test_input.txt"), 'r') as input_file:
    input = input_file.read()

##split list into groups
    input=input.split('\n\n')

##indidviduals by group
    ibg = []
    for i in range(len(input)-1):
        ibg.append(input[i].split('\n'))

##all the answers from the group
    yes_by_all = 0
    for group in ibg:
        group_answers = []
        for person in group:
            for answer in person:
                group_answers.append(answer)
        count = Counter(group_answers)
        for letter in string.ascii_lowercase:
            if count[letter] == len(group):
                print('all yes' +'\n'+ str(count[letter]) +'\n'+ str(len(group)) +'\n'+ str(group))
                yes_by_all += 1                        
            
        
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
            print(each)
            questions_answered_yes.append(each)
            print(questions_answered_yes)
    return(len(questions_answered_yes))

'''
for part two I need to know the answers by individual, AND group
from part 1 I already have the set of unique answers by group.
So next I need to check to see if each individual in that group had that set.
If not, I can trim the group set.
'''

'''
this is where i should use branching because I have a new approach
list all the groups answers.
If the count(answers ='a') == len(group):
    then everyone in the group had that answer, so count it. 
'''


group_sum = 0
for group_num in group:
    print(group_num)
    group_sum += yesbygroup(group_num)
##    print(group_sum)

print("Part One : "+ str(group_sum))


print("Part Two : "+ str(None))
