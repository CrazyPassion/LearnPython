def findMinCost(booklist):
    # print booklist
    booklist.sort(reverse=True)
    # print 'booklist', booklist

    Y1,Y2,Y3,Y4,Y5=booklist[0],booklist[1],booklist[2],booklist[3],booklist[4]
    cost = 0.0
    specialBook = min(Y3 - Y5,Y3 - Y4)
    if specialBook > 0 and Y5 >= 1 and (Y3 - specialBook*2)>0:
        #5+3
        # print 'tmp',Y1-specialBook*2,Y2-specialBook*2,Y3-specialBook*2,Y4-specialBook,Y5-specialBook
        cost=8*(1-0.20)*(specialBook*8)+findMinCost([Y1-specialBook*2,Y2-specialBook*2,Y3-specialBook*2,Y4-specialBook,Y5-specialBook])

    else:
        if Y5>=1:
            # print 'y5'
            cost=8*5*(1-0.25)*Y5+findMinCost([Y1-Y5,Y2-Y5,Y3-Y5,Y4-Y5,Y5-Y5])
        elif Y4>=1:
            # print 'y4'
            cost=8*4*(1-0.20)*Y4+findMinCost([Y1-Y4,Y2-Y4,Y3-Y4,Y4-Y4,0])
        elif Y3>=1:
            # print 'y3'
            cost=8*3*(1-0.10)*Y3+findMinCost([Y1-Y3,Y2-Y3,Y3-Y3,0,0])
        elif Y2>=1:
            # print 'y2'
            cost=8*2*(1-0.05)*Y2+findMinCost([Y1-Y2,Y2-Y2,0,0,0])
        elif Y1>=1:
            # print 'y1'
            cost=8*Y1
        else:#0,0,0,0,0
            # print 'all zero'
            cost = 0
    return cost


def getBookNum(line):
    bookNum = [0,0,0,0,0]
    for x in xrange(0,len(line)):
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
                print line.strip('\r\n')
                continue
            booklist = getBookNum(line)
            print '{0:g}'.format(float(findMinCost(booklist)))
            # print line

            linenum = linenum + 1

            # print "line" +str(linenum)
            # if linenum == 3:
            #     break


if __name__ == '__main__':
    # print findMinCost([3,2,1,4,5])
    # print findMinCost([2,2,2,1,1]) #51.2
    # print findMinCost([1,1,2,0,0]) #29.6//1233
    # GetAllMinCost('DaoMuBook_small_1509165671830')
    GetAllMinCost('DaoMuBook_large_1509165668412')