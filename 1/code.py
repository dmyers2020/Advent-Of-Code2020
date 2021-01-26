# Advent of code Year 2020 Day 1 solution
# Author = David Myers
# Date = December 2020

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()



print("Part One : "+ str(None))

#sinput = [l.split('%')for l in ','.join(input).split(',')]
#input = [input.replace("\n",",")]
#input = input[1:len(input)]

input = input.split('\n') #split the input (type = list) by the newline char "/n"

input = [int(i) for i in input] # use list comprehension to convert str members to ints

for i in input:
    for j in input:
            for k in input:
                if i+j+k==2020:
                    ans = i*j*k
                    print(i,j,k,ans)
                    break
#printing all permutations of answer - need a more clean approach: could I use yield? how to break out of nested loops)
    
            

print("Part Two : "+ str(None))
