# Advent of code Year 2020 Day 2 solution
# Author = David Myers
# Date = December 2020

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()



input = input.split('\n') #split the input (type = list) by the newline char "/

for i in range(len(input)):
    input[i] = input[i].split(' ') #split the input (type = list) by the newline char "/n"

"""establish if a password is valid for PART 1"""
    
valid_pass = 0 #keep a count of valid passwords
for i in range(len(input)):
    ltr = input[i][1] #has the letter plus a colon "g:" 
    count_of_membership = input[i][2].count(ltr[0]) #times ltr is in pass
    mem_range = input[i][0].split('-') #get min and max requirements
    if int(mem_range[0])<=count_of_membership <= int(mem_range[1]): #main test
        valid_pass+=1 # keep count
        
print("Part One : "+ str(valid_pass))


"""part2"""

# in part two, the min/max are actually positions, where the letter most occur in one OR the other; not both.

for i  in range(len(input)):
    if len(input[i][0].split('-'))>2:
        print(position)

valid_pass2 = 0 #keep a count of valid passwords
for i in range(len(input)):
    ltr = input[i][1] #has the letter plus a colon "g:" 
    position = input[i][0].split('-') #get POSITIONS to check
    password = input[i][2]
    if int(max(position))-1 <= len(password):
        if ltr[0]==password[int(position[0])-1] and ltr[0]!=password[int(position[1])-1]:#in first position but not second
            valid_pass2+=1 # keep count
        elif ltr[0]==password[int(position[1])-1] and ltr[0]!=password[int(position[0])-1]: #in second position not first
            valid_pass2+=1
print("Part Two : "+ str(valid_pass2))
