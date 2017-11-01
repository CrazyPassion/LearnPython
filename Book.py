# Book.py

def findMinCost(Y1, Y2, Y3, Y4, Y5):
    arr =[Y1, Y2, Y3, Y4, Y5]
    # print arr
    arr.sort()
    # print arr
    if arr[0]<0:
        print "the book number shoulb bigger than 0"
        return 0
    #Y1>=Y2>=Y3>=Y4>=Y5
    Y5=arr[0]
    Y4=arr[1]
    Y3=arr[2]
    Y2=arr[3]
    Y1=arr[4]
    cost = 0.0
    if (Y5>=1):
        cost=min(
                8*5*(1-0.25)+findMinCost(Y1-1,Y2-1,Y3-1,Y4-1,Y5-1),
                8*4*(1-0.20)+findMinCost(Y1-1,Y2-1,Y3-1,Y4-1,Y5),
                8*3*(1-0.10)+findMinCost(Y1-1,Y2-1,Y3-1,Y4,Y5),
                8*2*(1-0.05)+findMinCost(Y1-1,Y2-1,Y3,Y4,Y5)
            )
    elif (Y4>=1):
        cost=min(
                8*4*(1-0.20)+findMinCost(Y1-1,Y2-1,Y3-1,Y4-1,Y5),
                8*3*(1-0.10)+findMinCost(Y1-1,Y2-1,Y3-1,Y4,Y5),
                8*2*(1-0.05)+findMinCost(Y1-1,Y2-1,Y3,Y4,Y5)
            )
    elif(Y3>=1):
        cost=min(
                8*3*(1-0.10)+findMinCost(Y1-1,Y2-1,Y3-1,Y4,Y5),
                8*2*(1-0.05)+findMinCost(Y1-1,Y2-1,Y3,Y4,Y5)
            )
    elif(Y2>=1):
        cost=8*2*(1-0.05)+findMinCost(Y1-1,Y2-1,Y3,Y4,Y5)
    elif(Y1>=1):#{Y1,0,0,0,0} #same book
        cost=8*Y1
    else:#0,0,0,0,0
        cost=0
    return cost


if __name__ == '__main__':
    print "start"
    print findMinCost(3,2,1,4,5)
    print findMinCost(2,2,2,1,1) #51.2
    print findMinCost(1,2,3,3,0) #29.6

