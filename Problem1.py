#Written by Dominick Modica
#Purpose: Information Builders Problem 1.

import random

def generate_matrix(N):
    random.seed()
    #generates an N by N matrix
    matrix=[[0 for row in range(N)]for col in range(N)]
    for i in range(N):
        for j in range(N):
            #generate a random number between 0,100 for each i,j
            x=random.randint(0,100)
            if (x<50):
                matrix[i][j]=0
            else:
                matrix[i][j]=1
    return matrix; #returns the created matrix

def solve_matrix(matrix):
    print("...Solving Matrix...")
    score=0
    valid_moves=[(1,0),(-1,0),(0,1),(0,-1)] #this serves as a bank of valid moves to try
    #these moves represent up, down,left, and right which are the only valid moves
    
    length=len(matrix);
    visited=[]

    for i in range(length):
        for j in range(length):
            if matrix[i][j]==1 and (i,j) not in visited: # we have now discovered a new island with a "1" 
                score+=1
                queue=[(i,j)]
                while(queue):
                    current=queue.pop(0)#pops from index 0 and returns it to current
                    visited.append(current)
                    for move in valid_moves:
                        try:
                            m,n=current[0]+move[0],current[1]+move[1] #the m and n coordinates represent a neighbor to the current coordinate
                            #being investigated
                            
                            if (matrix[m][n]==1 and (m,n) not in visited):
                                
                                queue.append((m,n))
                                #if you "find" a new coordinate
                                #that has not been visited and is a 1
                                #add it to the queue to be investigated later
                            else:
                                visited.append((m,n))
                                #otherwise just add it to the useless visited "pool"
                        except:
                            pass; #was an invalid move forget about it anyway, is an easy way to filter out illegal moves

                  
            else:
                visited.append((i,j))#adds the coordinate to visited
    
    return score;

def main():
    print("What size matrix would you like?");
    N=int(input());
    matrix =generate_matrix(N) # calls generate_matrix to create a matrix with random elements
    print("Here is your matrix \n")
    for line in matrix:
        print(line)
    answer=solve_matrix(matrix)#calls solve_matrix which will return # of "islands"
    print("There exist %d independent islands of the number 1 in your matrix." %answer)

if __name__=="__main__":
    main();
    print("\n")

