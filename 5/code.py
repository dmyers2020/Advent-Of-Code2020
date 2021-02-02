# Advent of code Year 2020 Day 5 solution
# Author = David Myers
# Date = December 2020
## things I learned:

'''
 indexing using from x to end -y like: [0:-3],
  or from the end -y to the end, like: [-4:]

 creating lists using a =list(range(4,10))

 creating list of lists using 'for x in input'
 with open('file_name.txt','r') as input:
    lines = [x.rstrip() for x in input]

 floor division using the operator: //

 that the behavior of extracting values from a list is important:
    inclusive of first element, not inclusive of last
    a = [0,1,2,3,4,5]
    a[0:3] --> [0,1,2] # not [0,1,2,3]
''' 

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    passlist = [x.rstrip() for x in input_file]

# the input is a list of character strings which are each 10 digits long
# the first 7 chars in each string will be 'F' or 'B' and indicate whether
# to limit the search space to either the front half (F) or back half (B)
# of a set of rows to find your seat
# the last 3 chars in each string tell you to similarly limit the search space
# to the left or right half of a set of 8 columns.


def lower(seats):
    """
    input: a list of sequential integers
    output: the lower half of that set
    """
    seats = seats[:len(seats)//2]
    return seats

def upper(seats):
    """
    input: a list of sequential integers
    output: the upper half of that set
    """
    seats = seats[len(seats)//2:]
    return(seats)

seat_id =[]
for x in passlist:
    rows = list(range(128))
    for rsearchdir in x[:-3]:
        if rsearchdir == 'F':
            rows = lower(rows)
        if rsearchdir == 'B':
            rows = upper(rows)
        row = rows[0]
    
    cols = list(range(8))
    for colsearchdir in x[-3:]:
        if colsearchdir == 'L':
            cols = lower(cols)
        if colsearchdir == 'R':
            cols = upper(cols)
        col = cols[0]
    
    seat_id.append(row*8+col)

part1_answer = max(seat_id)
print("the answer to part 1 is: " + str(part1_answer))

## PART TWO 

##find your seat it's the only one missing
##from the list which also has it's immediate neighbors
##they put a note in there to tell me that seats at the
##very front/back aren't my

seat_id.sort()
for n in range(1,len(seat_id)-2):
    if seat_id[n]-seat_id[n-1]!=seat_id[n+1]-seat_id[n]:
        print("the answer to part 2 is: " + str(seat_id[n]+1))
        break
        
    
