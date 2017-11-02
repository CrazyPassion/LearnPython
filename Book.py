def findMinCost(bookNum):
    bookNum.sort()
    # print arr
    if bookNum[0] < 0:
        print "the book number shoulb bigger than 0"
        return 0.0

    #Y1>=Y2>=Y3>=Y4>=Y5
    Y5=bookNum[0]
    Y4=bookNum[1]
    Y3=bookNum[2]
    Y2=bookNum[3]
    Y1=bookNum[4]
    cost = 0.0
    if Y5>=1:
        # print 'y5'
        cost=min(
                8*5*(1-0.25)+findMinCost([Y1-1,Y2-1,Y3-1,Y4-1,Y5-1]),
                8*4*(1-0.20)+findMinCost([Y1-1,Y2-1,Y3-1,Y4-1,Y5]),
                8*3*(1-0.10)+findMinCost([Y1-1,Y2-1,Y3-1,Y4,Y5]),
                8*2*(1-0.05)+findMinCost([Y1-1,Y2-1,Y3,Y4,Y5]),
                8.0+findMinCost([Y1-1,Y2,Y3,Y4,Y5])
                )
    elif Y4>=1:
        # print 'y4'
        cost=min(
                8*4*(1-0.20)+findMinCost([Y1-1,Y2-1,Y3-1,Y4-1,0]),
                8*3*(1-0.10)+findMinCost([Y1-1,Y2-1,Y3-1,Y4,0]),
                8*2*(1-0.05)+findMinCost([Y1-1,Y2-1,Y3,Y4,0]),
                8.0+findMinCost([Y1-1,Y2,Y3,Y4,Y5])
                )
    elif Y3>=1:
        # print 'y3'
        cost=min(
                8*3*(1-0.10)+findMinCost([Y1-1,Y2-1,Y3-1,0,0]),
                8*2*(1-0.05)+findMinCost([Y1-1,Y2-1,Y3,0,0]),
                8.0+findMinCost([Y1-1,Y2,Y3,0,0])
                )
    elif Y2>=1:
        # print 'y2'
        cost=min(8*2*(1-0.05)+findMinCost([Y1-1,Y2-1,0,0,0]),
                 8.0+findMinCost([Y1-1,Y2,0,0,0]))
    elif Y1>=1:
        cost=8*Y1
    else:#0,0,0,0,0
        cost = 0
    return cost


def getBookNum(line):
    bookNum = [0,0,0,0,0]
    for x in xrange(1,len(line)):
        if line[x] == '1':
            bookNum[0] = bookNum[0] + 1
        elif line[x] == '2':
            bookNum[1] = bookNum[1] + 1
        elif line[x] == '3':
            bookNum[2] = bookNum[2] + 1
        elif line[x] == '4':
            bookNum[3] = bookNum[3] + 1
        elif line[x] == '5':
            bookNum[4] = bookNum[4] + 1

    # print bookNum
    return bookNum

def GetAllMinCost(file_path):
    with open(file_path, 'r') as fp:
        linenum = 0
        for line in fp:
            # print line
            if (linenum == 0):
                linenum = linenum + 1
                continue
            bookNum = getBookNum(line)
            print findMinCost(bookNum)
            # print "s"
            # print line

            linenum = linenum + 1

            # print "line" +str(linenum)
            # if linenum == 2:
            #     break


if __name__ == '__main__':
    # print findMinCost([3,2,1,4,5])
    # print findMinCost([2,2,2,1,1]) #51.2
    # print findMinCost([1,1,2,0,0]) #29.6//1233
    GetAllMinCost('DaoMuBook_small_1509165671830')