# Advent of code Year 2020 Day 4 solution
# Author = David Myers
# Date = December 2020

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
import regex as re
import numpy as np

'''sample_input.txt is available for testing'''

##print(input[0])
## split into separate passports
input = re.split('\n\n',input) #note that the slash direction matters for newline
##split into 'field:value'
for i in range(len(input)):
    input[i] = re.split(' |\n',input[i]) #break each passport into separate components


valid_passport = len(input)
print("passports to review: " +str(valid_passport))
invalid_cond_1,invalid_cond_2 = 0,0
for i in range(len(input)):
    if len(input[i])<7: #cannot be missing more than 1 field
        #diagnostics
        print("passport #"+str(i) +" condition 1 violated. # of fields: " + str(len(input[i])))
        valid_passport-=1
        invalid_cond_1+=1

    elif len(input[i])<8: #missing a field: CID shouldn't be present
        for j in input[i]:
            if j.find('cid') == 0:
                valid_passport -=1
                invalid_cond_2+=1
                #diagnostics
                print("passport #"+str(i) +" condition 2 violated. # of fields: "+ str(len(input[i]))+" " +str(j))

    elif 1==1: #all necessary fields present; make sure they're valid
        for j in input[i]:
            key_val = re.split(":",j)
            key = key_val[0]
            val = key_val[1]
            if key == "byr":
                if not (len(val)==4 and 1919<int(val)<2003):
                    print(str(key)+" violated: " + str(val) + "  passport: " +str(i))
                    valid_passport -=1
            elif key == "iyr":
                if not (len(val)==4 and 2009<int(val)<2021):
                    valid_passport -=1
                    print(str(key)+" violated: " + str(val) + "  passport: " +str(i))
            elif key == "eyr":
##                print("checked expiration year "+str(i))
                if not (len(val)==4 and 2019<int(val)<2031):
                    valid_passport -=1
                    print(str(key)+" violated: " + str(val) + "  passport: " +str(i))
            elif key == "hgt":
                if val.find('cm')==0:
                    cm = re.split('cm',val)
                    if not (150<int(cm[0])<193):
                        valid_passport -=1
                        print(str(key)+" violated: " + str(val) + "  passport: " +str(i))
                elif val.find('in')==0:
                    inch = re.split('in',val)
                    if not (59<int(inch[0])<76):
                        valid_passport -=1
                        print(str(key)+" violated: " + str(val) + "  passport: " +str(i))
            elif key == "hcl":
                if not (val.find('#')==0 and len(val)==7): #does not account for non alphanumeric characters in hcl
                    valid_passport -=1
                    print(str(key)+" violated: " + str(val) + "  passport: " +str(i))
            elif key == "ecl":
                if val not in ['amb','blu','brn','gry','hzl','oth']:
                    valid_passport -=1
                    print(str(key)+" violated: " + str(val) + "  passport: " +str(i))
            elif key == "pid":
                if not len(val)==9: #does not account for non numeric inputs
                    valid_passport -=1
                    print(str(key)+" violated: " + str(val) + "  passport: " +str(i))

print("Part One : "+ "205") #str(valid_passport)) #(205 was correct for part 1)

print("condition 1 violations: "+ str(invalid_cond_1) + " condition 2 violations: " + str(invalid_cond_2))


print("Part Two : "+ str(valid_passport)) #179 was correct on the first attempt;
# caught multiple errors using sample inputs and had to do a lot of printing to help troubleshoot.
