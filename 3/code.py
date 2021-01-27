# Advent of code Year 2020 Day 3 solution
# Author = David Myers
# Date = December 2020

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = input.split('\n')
tree_count = []
# print(str(input[0][2])=="#")
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]] #slopes to check

for j in range(len(slopes)):
    #initialize variables
    row, col, num_row, num_col = 0,0,len(input),len(input[0])
    #answer is the product of all members of tree_count (Part 1 is sloe[1])
    tree_count.append(0)

    #main
    for i in range(num_row):
        #tree in that position? use mod to "repeat" row pattern
        if str(input[row][col%num_col])=="#":
            tree_count[j]+=1

        #proceed down slope
        col += slopes[j][0] #right
        row += slopes[j][1] #down

        #handle slopes that jump down >1 row at a time breaking indexing
        if row >len(input): break


print("Part One : "+ str(tree_count)) #part 1 answer is 205 (tree_count[1])

result = 1
#get the product of all members of tree_count
for x in tree_count:
        result = result*x

print("Part Two : "+ str(result))
