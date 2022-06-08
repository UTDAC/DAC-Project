#  File: Boxes.py

#  Description:

#  Student Name: Sebastian Davoli

#  Student UT EID: sd695

#  Partner Name: Elaine Williams

#  Partner UT EID: 

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created:

#  Date Last Modified:

import sys

nesting_cache = {}

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes



def nesting_boxes (i,j,skip,box_list):
    global nesting_cache
    length = len(box_list)
    print('box_list =',(box_list))
    print('skip =',skip)
    print('i =',str(i))
    print('current box:',box_list[length-i])
    print('j =',str(j))
    print('tested box:',box_list[length-j])


    
    if i == length: #if the end has been reached
        i = i - skip
        j = i + 1
        print('i == length')
        print('\n \n \n \n ')        
        return nesting_boxes(i,j,skip,box_list)

    elif j > length:
        print('j > length')
        print('\n \n \n \n ')
        j = i + 1 #setting tested box to one after the current box (skipping over current box)
        i = length-skip+1 #setting current box to the previous 
        skip = 0 #resetting skip
        return nesting_boxes(i,j,skip,box_list) #moving i back to previous position and j skips the box with no inner fits

    elif j <= length and does_fit((box_list[length-j]),(box_list[length-i])): #if box 1 fits in box 2
        print('tested box fits!')
        print('\n \n \n \n ')
        skip = j - i + 1
        i = j #box2 is now box1
        j += 1 #box1 shifts down 1


        #how tf we doing this?
        
        nesting_cache[length-i] += nesting_cache[length-j] + 1#max boxes for i = max boxes for j + 1
        print(nesting_cache[length-i])


        return nesting_boxes(i,j,skip,box_list) #repeat with new i and j values

    else:
        print('moving j and skip')
        print('\n \n \n \n ')
        j += 1
        skip += 1
        return nesting_boxes(i,j,skip,box_list) #repeat with a new j only
    
    return 0, 0







# returns True if box1 fits inside box2
def does_fit (box1, box2):
    return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
    global nesting_cache
    # read the number of boxes 
    line = sys.stdin.readline()
    line = line.strip()
    num_boxes = int (line)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range (num_boxes):
        line = sys.stdin.readline()
        line = line.strip()
        box = line.split()
        for j in range (len(box)):
            box[j] = int(box[j])
        box.sort()
        box_list.append (box)

    #print to make sure that the input was read in correctly
    #print('original list')
    #print(box_list)
    #print()
    

    # sort the box list
    box_list.sort()

    # print the box_list to see if it has been sorted.
    print('sorted box list')
    print(box_list)
    print()

    #creating dictionary of index value and the max # of boxes which fit in it
    for i in range(len(box_list)):
        nesting_cache[i] = 0 #nesting_cache[index of box] = max # boxes which fit inside it
    
    i = 1
    j = 2
    skip = 1

    # get the maximum number of nesting boxes and the
    # number of sets that have that maximum number of boxes
    max_boxes, num_sets = nesting_boxes(i,j,skip,box_list)

    # print the largest number of boxes that fit
    print (max_boxes)

    # print the number of sets of such boxes
    print (num_sets)


if __name__ == "__main__":
  main()


