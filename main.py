import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

listOfCells = []

def calcPointGrow(size,trees):
    base = 1
    if size == 1:
        base = 3
    if size == 2 : 
        base = 7
    elif size == 3:
        base = 7

    for arbre in trees:
        if arbre.size == (size+1) and arbre.mine:
            base += 1
    return base

def nbDarbreMine(trees):
    nb = 0
    for t in trees:
        if t.mine:
            nb += 1

    return nb

def calcPointToSeed(trees):
    pt = 0
    for arbre in trees:
        if arbre.size == 0 and arbre.mine:
            pt += 1

    return pt

def isCellAvailable(index, trees):
    available = True
    for arbre in trees:
        if arbre.location == index:
            available = False
    
    return available

def nbTreeForLevel(trees,level):
    nb = 0
    for t in trees:
        if t.mine and t.size == level:
            nb += 1
    return nb

def chooseCellToSeed(arbre,trees,listOfCells):
    index = -1
    actualCell = None
    arbreCell = None
    for c in listOfCells:
        if c.index == arbre.location:
            arbreCell = c
            break
    for actionSeed in arbre.actionSeed:
        param = actionSeed.split(" ")
        index = int(param[2])
        newCell = None
        for cell in listOfCells:
            if cell.index == index:
                newCell = cell
                break
        if isCellAvailable(index,trees):
            if actualCell is None:
                actualCell = newCell
            else:
                #if newCell.richness > actualCell.richness:
                if arbre.size == 2 :
                    if arbreCell.richness <3 and newCell.richness == 3:
                        actualCell = newCell
                        break
                    elif arbreCell.richness == 3 and newCell.richness == 1:
                        actualCell = newCell
                        break
                            
                    else:
                        if newCell.richness == 1:
                            actualCell = newCell
                            break
                elif newCell.richness == 2:
                    actualCell = newCell

    if actualCell is not None:
        return actualCell.index
    return -1
    


class Cell:
    def __init__(self):
        self.index = 0
        self.richness = 0
        self.neigh=[]

class Tree:
    def __init__(self):
        self.size = 0
        self.location = 0
        self.isDormant = False
        self.actionSeed = []
        self.mine = False
        self.lastTick_Seeded = 0


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
    listOfCells.append(cell)

# game loop
hasSeeded = False
waitForGrow = False
tour = 0
while True:
    tour += 1
    hasSeeded = not hasSeeded
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
    listOfTrees = []
    for i in range(number_of_trees):
        inputs = input().split()
        cell_index = int(inputs[0])  # location of this tree
        size = int(inputs[1])  # size of this tree: 0-3
        is_mine = inputs[2] != "0"  # 1 if this is your tree
        is_dormant = inputs[3] != "0"  # 1 if this tree is dormant
        if is_mine:
            arbre = Tree()
            arbre.size = size
            arbre.mine = is_mine
            arbre.isDormant = is_dormant
            arbre.location = cell_index
            listOfTrees.append(arbre)

    #listOfActions=[]
    number_of_possible_actions = int(input())  # all legal actions
    hasPrinted = False
    for i in range(number_of_possible_actions):
        possible_action = input()  # try printing something from here to start with
        print("Debug messages..." + possible_action, file=sys.stderr, flush=True)
        #listOfActions.append(possible_action)
        if "SEED" in possible_action:
            param=possible_action.split(" ")
            for t in listOfTrees:
                if t.location == int(param[1]):
                    #print("DPWET..." + str(t.location) + "§§" + str(int(param[1])), file=sys.stderr, flush=True)
                    t.actionSeed.append(possible_action)
                   # print("Debug SEEDD..." + str(len(t.actionSeed)), file=sys.stderr, flush=True)


    #if not hasPrinted:
    #    print("WAIT")         
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    for arbre in listOfTrees:
        #hasPrinted = False
        if not hasPrinted and arbre.mine:
            print("PPPPPP" + str(tour), file=sys.stderr, flush=True)
            nbBigTree = nbTreeForLevel(listOfTrees,3)
            if (arbre.size == 3) and(sun >= 4) and ((tour > 40) or nbBigTree>4):
                print("COMPLETE " + str(arbre.location))
                hasPrinted = True
                sun -= 4
            
            if not hasPrinted:
                nbArbre = nbDarbreMine(listOfTrees)
                nbSeed = nbTreeForLevel(listOfTrees,0)
                if (arbre.size >= 1) and (nbArbre<8) and (not arbre.isDormant) and (hasSeeded) and (nbSeed < 2):
                    nbPtNeeded = calcPointToSeed(listOfTrees)
                    #print("arbre seed " + str(arbre.location) + " action = " + arbre.actionSeed[0], file=sys.stderr, flush=True)
                    if (nbPtNeeded <= sun):
                        cellToSeed = chooseCellToSeed(arbre,listOfTrees,listOfCells)
                        if cellToSeed != -1:
                            print("SEED " + str(arbre.location) + " " + str(cellToSeed))
                            hasPrinted = True
                            sun -= nbPtNeeded
                            hasSeeded = True
                            break

                if not hasPrinted and arbre.mine:
                    if (arbre.size == 3) and(sun >= 4) and (tour > 40):
                        print("COMPLETE " + str(arbre.location))
                        hasPrinted = True
                        sun -= 4

                if not hasPrinted:
                    nbPtNeeded = calcPointGrow(arbre.size,listOfTrees)
                    print("abre size=" + str(arbre.size) + " location=" + str(arbre.location) + " ptneeded=" + str(nbPtNeeded) + " sun=" + str(sun), file=sys.stderr, flush=True)
                    if  (not arbre.isDormant) and (arbre.size < 3):
                        if (nbPtNeeded <= sun):
                            print("GROW " + str( arbre.location))
                            hasPrinted = True
                            sun -= nbPtNeeded
                            break
                        

   # if not hasPrinted :                
   #     for arbre in listOfTrees:
    ##        nbPtNeeded = calcPointGrow(arbre.size,listOfTrees)
    #        print("abre size=" + str(arbre.size) + " location=" + str(arbre.location) + " ptneeded=" + str(nbPtNeeded) + " sun=" + str(sun), file=sys.stderr, flush=True)
     #       if (nbPtNeeded <= sun) and (arbre.size < 3) and (not arbre.isDormant):
   #             print("GROW " + str( arbre.location))
     #           hasPrinted = True
     #           sun -= nbPtNeeded
     #           break
            
            
    if not hasPrinted:
        print ("WAIT")

    # GROW cellIdx | SEED sourceIdx targetIdx | COMPLETE cellIdx | WAIT <message>
    #print("WAIT")
