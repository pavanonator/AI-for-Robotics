# The function localize takes the following arguments:
#
# colors:
#        2D list, each entry either 'R' (for red cell) or 'G' (for green cell)
#
# measurements:
#        list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:
#        list of actions taken by the robot, each entry of the form [dy,dx],
#        where dx refers to the change in the x-direction (positive meaning
#        movement to the right) and dy refers to the change in the y-direction
#        (positive meaning movement downward)
#        NOTE: the *first* coordinate is change in y; the *second* coordinate is
#              change in x
#
# sensor_right:
#        float between 0 and 1, giving the probability that any given
#        measurement is correct; the probability that the measurement is
#        incorrect is 1-sensor_right
#
# p_move:
#        float between 0 and 1, giving the probability that any given movement
#        command takes place; the probability that the movement command fails
#        (and the robot remains still) is 1-p_move; the robot will NOT overshoot
#        its destination in this exercise
#
# The function should RETURN (not just show or print) a 2D list (of the same
# dimensions as colors) that gives the probabilities that the robot occupies
# each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform
# probability of being in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.
#
# Motion:
#  [0,0] - stay
#  [0,1] - right
#  [0,-1] - left
#  [1,0] - down
#  [-1,0] - up

def localize(colors,measurements,motions,sensor_right,p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    
    # >>> Insert your code here <<<
    for k in range(len(measurements)):
        p = move(p, motions[k], p_move)
        p = sense(p, measurements[k], sensor_right)
    return p

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print '[' + ',\n '.join(rows) + ']'
    
def sense(p, Z, sensor_right):
    q=[]
    s=0
    for i in range(len(p)):
        q.append([])
        for j in range(len(p[0])):
            hit = (Z == colors[i][j])
            q[i].append(p[i][j] * (hit * sensor_right + (1-hit) * (1-sensor_right)))
            s+=q[i][j]
    
    for i in range(len(q)):
        for j in range(len(q[0])):
            q[i][j] = q[i][j] / s
    #show(q)
    return q

def move(p, U, p_move):
    q = []
    #remember that U will be an array of arrays: [[0,1][1,0]]
    #acct for pMove - prblity that it successfully moves instead of staying in place
    
    for i in range(len(p)):
        q.append([])
        for j in range (len(p[0])):
            if (U[0]>0 & U[1]==0): #moves down
                s = p_move*p[(i-U[0])%len(p)][j] + (1-p_move)*p[i][j]
            if (U[0]<0 & U[1]==0): #moves up
                s = p_move*p[(i-U[0])%len(p)][j] + (1-p_move)*p[i][j]
            if (U[0]==0 & U[1]==0): #no move
                s=p[i][j]
            if (U[1]>0 & U[0]==0): #right
                s = p_move*p[i][(j-U[1])%len(p[0])] + (1-p_move)*p[i][j]
            if (U[1]<0 & U[0]==0): #left
                s = p_move*p[i][(j-U[1])%len(p[0])] + (1-p_move)*p[i][j]
            #s = pExact * p[(i-U) % len(p)]
            #s = s + pOvershoot * p[(i-U-1) % len(p)]
            #s = s + pUndershoot * p[(i-U+1) % len(p)]
            q[i].append(s) 
    #show(q)
    return q
    

#############################################################


colors = [['R','G'],
          ['R','R'],
          ['G','R'],
          ['R','G'],
          ['G','G']]

measurements = ['R','R','G','G','G','R']
motions = [[0,0],[-1,0],[0,1],[0,-1],[0,1],[1,0]]
p = localize(colors,measurements,motions,sensor_right = 0.99, p_move = 0.97)
show(p) # displays your answer
