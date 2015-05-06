import itertools

def crossing(left,right,raft,direction):
    if (direction==-1): #happens in the base case
        #load up raft for the first time with all combinations and call crossing
        combinations=list(itertools.combinations(left,1))+list(itertools.combinations(left,2))
        #combinations is a list of all possible combinations of 1 and 2 party
        for combo in combinations:
            crossing(list(set(left)-set(combo)),right,combo,0)

    else: #now we should check the raft and left and right conditions for rule violations
        if ("F" not in raft) or ("M" not in raft) or ("G" not in raft):
            return; #invalid move if father mother or guard not in the raft
        elif ( ("F" and ("D1" or "D2"))and "M" not in left) or ("F" and ("D1" or "D2"))and "M" not in right:
            return;#invalid move father cannot be left alone with daughters without mother present
        elif ( ("M" and ("S1" or "S2"))and "F" not in left) or ("M" and ("S1" or "S2"))and "F" not in right:
            return; #invalid move mother cannot be left alone with sons without the father present
        elif ("P" in left and "G" not in left) or ("P" in right and "G" not in right):
            return; #invalid move because the prisoner cannot be left without the guard
        if (direction==0):
            right=right+raft #dump the raft onto the right side
            raft=[] #empties the raft
            if (len(right)==8): #check to see if all people are on the right side
                return "Problem Solved";
            combinations=list(itertools.combinations(right,1))+list(itertools.combinations(right,2))
            #combinations is a list of all possible combinations of 1 and 2 party
            for combo in combinations:
                crossing(left,list(set(right)-set(combo)),combo,1)
        else:
            left=left+raft #dump the raft onto the left side
            raft=[]
            combinations=itertools.combinations(left,1)+itertools.combinations(left,2)
            #combinations is a list of all possible combinations of 1 and 2 party
            for combo in combinations:
                crossing(list(set(left)-set(combo)),right,combo,0)
    


def main():
    left=["F","M","S1","S2","D1","D2","G","P"]
    right=[]
    raft=[]
    movelist=[]
    direction= -1#direction 0 represents going towards the right and direction 1 represents going towards the left
    print(crossing(left,right,raft,direction))


if __name__=="__main__":
    main();
