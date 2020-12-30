from random import randint
def Algo (PC,PLR):
    wins=[[11,12,13],[21,22,23],[31,32,33],[11,21,31],[12,22,32],[13,23,33],[11,22,33],[31,22,13]]
    All=[11,12,13,21,22,23,31,32,33]
    opportunity=list()
    
    for win in wins:
        if len(set(win).intersection(set(PC))) == 2:  # Play in Winning Block
            move = list(set(win)-set(PC))[0]
            if not((move in PLR) or (move in PC)) is True:
                return move
    
    for win in wins:
        if len(set(win).intersection(set(PLR))) == 2  :# Block opponent win
            move = list(set(win)-set(PLR))[0]
            if not((move in PLR) or (move in PC)) is True:
                return move
    
    if randint(0,9)>7:
        move = 11
        while (move in PLR) or (move in PC) is True:# 20% chance of making a random move
            move= 10*randint(1,3)+randint(1,3)
        print("RANDOM")
        return move    
    
    
    if any(comb in PLR for comb in [11,31,33,13]) is True and len(PC) == 0:# To counter the corner move trick
        if randint(0,9)>4:
            return 22

    for move in Diff(All,PC,PLR):
        opportunity.append((Minimax(move,0.0,PC,PLR,2.0),move))# Minimax Concept applied poorly
    opportunity.sort(reverse=True)
    print(opportunity)
    for move in opportunity:
        return move[1]



def wincheck(check):
        wins=[[11,12,13],[21,22,23],[31,32,33],[11,21,31],[12,22,32],[13,23,33],[11,22,33],[31,22,13]]
        for win in wins:
            if all(play in check for play in win) is True:
                return True
        return False

def Diff(a,b,c):
    return list(set(a)-set(b)-set(c))

def Minimax(move,minimax,PC,PLR,c):
            All=[11,12,13,21,22,23,31,32,33]
            PCTest=PC.copy()
            PCTest.append(move)
            for first in Diff(All,PCTest,PLR):
                PLRTest=PLR.copy()
                PLRTest.append(first)
                if wincheck(PLRTest) is True:
                    minimax=minimax-c

                else:
                    for second in Diff(All,PCTest,PLRTest):
                        PCTest.append(second)
                        if wincheck(PCTest) is True:
                            minimax=minimax+c
                        else:
                            minimax = Minimax(second,minimax,PCTest,PLRTest,c/2)
            return minimax
