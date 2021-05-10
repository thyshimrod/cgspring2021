import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Tree:
    size = 0
    location = 0
    isDormant = False
    def __init__(self):
        pass

number_of_cells = int(input())  # 37
for i in range(number_of_cells):
    # index: 0 is the center cell, the next cells spiral outwards
    # richness: 0 if the cell is unusable, 1-3 for usable cells
    # neigh_0: the index of the neighbouring cell for each direction
    index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]

# game loop
while True:
    day = int(input())  # the game lasts 24 days: 0-23
    nutrients = int(input())  # the base score you gain from the next COMPLETE action
    # sun: your sun points
    # score: your current score
    sun, score = [int(i) for i in input().split()]
    inputs = input().split()
    opp_sun = int(inputs[0])  # opponent's sun points
    opp_score = int(inputs[1])  # opponent's score
    opp_is_waiting = inputs[2] != "0"  # whether your opponent is asleep until the next day
    number_of_trees = int(input())  # the current amount of trees
    myTrees = []
    for i in range(number_of_trees):
        inputs = input().split()
        cell_index = int(inputs[0])  # location of this tree
        size = int(inputs[1])  # size of this tree: 0-3
        is_mine = inputs[2] != "0"  # 1 if this is your tree
        is_dormant = inputs[3] != "0"  # 1 if this tree is dormant
        if is_mine:
            arbre = Tree()
            arbre.size = size
            arbre.isDormant = is_dormant
            arbre.location = cell_index
            myTrees.append(arbre)

    listOfActions=[]
    number_of_possible_actions = int(input())  # all legal actions
    hasPrinted = False
    for i in range(number_of_possible_actions):
        possible_action = input()  # try printing something from here to start with
        print("Debug messages..." + possible_action, file=sys.stderr, flush=True)
        listOfActions.append(possible_action)
        #if possible_action != "WAIT" and not hasPrinted:
        #    print(str(possible_action))
        #    hasPrinted = True

    #if not hasPrinted:
    #    print("WAIT")         
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    for abre in myTrees:
        if arbre.size == 3 and not hasPrinted:
            print("COMPLETE " + arbre.location)
            hasPrinted = True
            break

    if not hasPrinted:
        for abre in myTrees:
            if arbre.size == 3 and not hasPrinted:
                print("GROW " + arbre.location)
                hasPrinted = True
                break
    
    if not hasPrinted:
        print ("WAIT")

    # GROW cellIdx | SEED sourceIdx targetIdx | COMPLETE cellIdx | WAIT <message>
    #print("WAIT")

