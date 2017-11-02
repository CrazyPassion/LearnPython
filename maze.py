import re

def GetZPos(maze):
    # print maze[0]
    for x in xrange(0,len(maze)):
        for y in xrange(0,len(maze[0])):
            if maze[x][y] == 'Z':
                return x,y


def GetAllPath(file_path):
    with open(file_path, 'r') as fp:
        linenum = 0
        infoline = 1
        maze=[]
        N=0
        M=0
        T=0
        for line in fp:
            # print "line",line,linenum,infoline
            line = line.strip('\r\n')
            if (linenum == 0):
                linenum = linenum + 1
                continue
            if infoline == linenum:
                digi_str = re.findall(r'([0-9]+)',line)
                digi = [int(i) for i in digi_str]
                N = digi[0]
                M = digi[1]
                T = digi[2]
                infoline = infoline + M
                # print 'digi',digi,linenum
                continue
            if M>0:
                line = line.replace(' ','')
                maze.append(list(line))
                M = M - 1
                # print 'maze',maze,'M',M
                if M==0:
                    x,y = GetZPos(maze)
                    # print x, y
                    # print "type",type(maze[0]),"len",len(maze[0])
                    if search(maze,x,y,T+1):
                        print "YES"
                    else:
                        print "NO"
                    maze[:] = []

            linenum = linenum + 1


            # print "line" +str(linenum)
            # if linenum == 80:
            #     break

def search(maze, x, y, step):
    step = step - 1
    # print 'step',step
    if step >= 0 :
        if maze[x][y] == 'L':
            # print 'found at %d,%d' % (x, y)
            return True
        elif maze[x][y] == '*':
            # print 'wall at %d,%d' % (x, y)
            return False
        elif maze[x][y] == 'p':
            # print 'visited at %d,%d' % (x, y)
            return False
    else:
        return False

    # print 'visiting %d,%d' % (x, y)
    # mark as visited
    maze[x][y] = 'p'

    #  explore neighbors clockwise starting by the one on the right
    if ((x < len(maze)-1 and search(maze, x+1, y, step))
        or (y > 0 and search(maze, x, y-1, step))
        or (x > 0 and search(maze, x-1, y, step))
        or (y < len(maze[0])-1 and search(maze, x, y+1, step))):
        return True

    return False

# search(0, 0)


def WillGet(maze, step):
    # print maze[0][3]
    print search(maze,3,0,step+1)



def testcode():
    l1=['.', '.', '.', 'L']
    l2=['.', '*', '.', '.']
    l3=['.', '*', '.', '.']
    l4=['Z', '.', '.', '*']
    maze1=[l1,l2,l3,l4]
    # print maze1
    WillGet(maze1,5) #NO(4,4,5)

    ll1=['.', '.', 'L']
    ll2=['*', '.', '.']
    ll3=['*', '.', '.']
    ll4=['Z', '.', '*']
    maze2=[ll1,ll2,ll3,ll4]
    # print len(maze2[0])
    # print maze2
    WillGet(maze2,5) #YES(3,4,5)


if __name__ == '__main__':
    testcode()
    # GetAllPath('LongMenHotel_small_1509165675196')
