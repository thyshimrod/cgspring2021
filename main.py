import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def calcPointGrow(size,trees):
    base = 1
    if size == 1:
        base = 3
    if size == 2 : 
        base = 7
    elif size == 3:
        base = 7

    for arbre in trees:
        if arbre.size == size:
            base += 1
    base -= 1
    return base
    


class Cell:
    index = 0
    richness = 0
    neigh=[]
    lastTick_Seeded = 0
 
    def __init__(self):
        pass

class Tree:
    size = 0
    location = 0
    isDormant = False
    actionSeed = []
    def __init__(self):
        pass

listOfCells = []
number_of_cells = int(input())  # 37
for i in range(number_of_cells):
    # index: 0 is the center cell, the next cells spiral outwards
    # richness: 0 if the cell is unusable, 1-3 for usable cells
    # neigh_0: the index of the neighbouring cell for each direction
    index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
    cell = Cell()
    cell.index = index
    cell.richness = richness
    cell.neigh.append(neigh_0)
    cell.neigh.append(neigh_1)
    cell.neigh.append(neigh_2)
    cell.neigh.append(neigh_3)
    cell.neigh.append(neigh_4)
    cell.neigh.append(neigh_5)

# game loop
actualTick = 0
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
        if "SEED" in possible_action:
            param=possible_action.split(" ")
            for t in myTrees:
                if t.location == int(param[1]):
                    t.actionSeed.append(possible_action)


    #if not hasPrinted:
    #    print("WAIT")         
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    for abre in myTrees:
        if not hasPrinted:
            if arbre.size == 3 and sun >= 4:
                print("COMPLETE " + str(arbre.location))
                hasPrinted = True
                sun -= 4
            else:
                nbPtNeeded = calcPointGrow(arbre.size,myTrees)
                print("abre size=" + str(arbre.size) + " location=" + str(arbre.location) + " ptneeded=" + str(nbPtNeeded) + " sun=" + str(sun), file=sys.stderr, flush=True)
                if (nbPtNeeded <= sun) and (arbre.size < 3):
                    print("GROW " + str( arbre.location))
                    hasPrinted = True
                    sun -= nbPtNeeded
    
    if not hasPrinted:
        print ("WAIT")

    # GROW cellIdx | SEED sourceIdx targetIdx | COMPLETE cellIdx | WAIT <message>
    #print("WAIT")

    actualTick+=1