# Advent of code Year 2020 Day 6 solution
# Author = David Myers
# Date = February 2021
import math
import os
import string
##require collections
from collections import Counter

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

##split list into groups
    input=input.split('\n\n')

##indidviduals by group
    ibg = []
    for i in range(len(input)):
        ibg.append(input[i].split('\n'))

##all the answers from the group
'''
I should have done this as a function, and put the 'for each letter' as the function caller... but lazy
'''
    yes_by_all = []
    all_yes = 0
    for group in ibg:
        group_answers = []
        for person in group:
            for answer in person:
                group_answers.append(answer)
            count = Counter(group_answers) #takes the form: Counter({'a':4}), so count is subscriptable by letter
            for letter in string.ascii_lowercase: #the lowercase alphabet as a string
                if count[letter] == len(group): #len of group = # of people who should have the same answer
                    yes_by_all.append([1,letter])
                    all_yes+=1
        
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
            questions_answered_yes.append(each)
    return(len(questions_answered_yes))

group_sum = 0
for group_num in group:
    group_sum += yesbygroup(group_num)

print("Part One : "+ str(group_sum))


print("Part Two : "+ str(all_yes))
