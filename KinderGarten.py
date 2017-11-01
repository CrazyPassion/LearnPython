# KinderGarten
# -*- coding: utf-8 -*-
import re

def CalcTeamNum(teamGroup, range, candyNumInCan):
    teamNum = 0
    if (range == 0):
        teamNum = cc1(teamGroup, candyNumInCan)
    elif (range == 1):
        teamNum = cc2(teamGroup, candyNumInCan)
    elif(range == 2):
        teamNum = cc3(teamGroup, candyNumInCan)
    elif(range == 3):
        teamNum = cc4(teamGroup, candyNumInCan)
    # print teamNum,range
    return teamNum


def CalcSatisfiedTeamNum(teamGroup, teamMember, candyNumInCan):
    # print len(teamGroup), teamMember, candyNumInCan
    if (len(teamGroup)>teamMember) or (candyNumInCan < 1):
        print "invalid data"
        return 0

    satisfiedTeamNumber = 0
    for x in xrange(0,candyNumInCan):
        # print "hhh"
        # print teamGroup
        satisfiedTeamNumber = satisfiedTeamNumber + CalcTeamNum(teamGroup, x, candyNumInCan)
        if(len(teamGroup) < candyNumInCan):
            break
        # print "hhh"+str(satisfiedTeamNumber)
    # if teamGroup:
        # print "ttt"+str(satisfiedTeamNumber)
        # print teamGroup
        # print satisfiedTeamNumber
    # else:
    #     print "null"+str(satisfiedTeamNumber)
    return satisfiedTeamNumber



def GetAllSatisfiedTeamNumber(file_path):
    print "GetAllSatisfiedTeamNumber"
    fp = open(file_path, 'r')
    linenum = 0
    caseNum = 0
    satisfiedTeamNumber = 0
    candyNumInCan = 0
    for line in fp:
        digi_str = re.findall(r'([0-9]+)',line)
        digi = [int(i) for i in digi_str]
        # print digi
        if (linenum == 0):
            totalCaseNum = digi[0]
            print totalCaseNum

        elif (linenum % 2 == 1):
            caseNum = caseNum + 1
            teamNum = digi[0]
            candyNumInCan = digi[1]
        else:
            if (candyNumInCan != 2) and (candyNumInCan != 3):
                print candyNumInCan
            satisfiedTeamNumber = CalcSatisfiedTeamNum(digi, teamNum, candyNumInCan)
            print "Case #" + str(caseNum) +": "+str(satisfiedTeamNumber)
            pass

        linenum = linenum + 1

        # print "line" +str(linenum)
        # if linenum == 3:
        #     break
    fp.close()


def cc1(l,candy):
    num = 0
    needPop = []
    for idx in xrange(0,len(l)):
        if l[idx] % candy == 0:
            num = num + 1
            needPop.append(idx)
    # print needPop
    offset = 0
    for i in needPop:
        # print i
        l.pop(i - offset)
        offset = offset + 1
    if len(l) == 1:
        num = num + 1
    return num


def cc2(l, candy):
    num = 0
    found = False
    idx = 0
    while len(l):
        if len(l) <= candy and len(l) <= 2:
            num = num + 1
            l[:] = []
            break
        allSearch = False
        for secIdx in xrange(idx + 1, len(l)):
            # print len(l)
            if secIdx == len(l) - 1:
                allSearch = True
            # print idx,secIdx,l[idx],l[secIdx]
            if (l[idx]+l[secIdx]) % candy == 0:
                # print idx,secIdx,l[idx],l[secIdx]
                l.pop(idx)
                l.pop(secIdx - 1)
                num = num + 1
                # print "tmpl", l
                found = True
                break
        if allSearch:
            break
        else:
            idx = 0
    # print "c2",l
    return num


def cc3(l, candy):
    num = 0
    found = False
    while len(l):
        idx = 0
        if len(l) <= candy:
            num = num + 1
            l[:] = []
            break
        allSearch = False
        for secIdx in xrange(idx + 1, len(l)):
            found = False
            if secIdx == len(l) - 1:
                allSearch = True
            # allSearchThird = False
            for thirdIdx in xrange(secIdx + 1, len(l)):
                # if thirdIdx == len(l) - 1:
                #     allSearchThird = True
                # print "ss",idx,secIdx,thirdIdx,l[idx],l[secIdx],l[thirdIdx]
                if (l[idx]+l[secIdx] + l[thirdIdx]) % candy == 0:
                    # print "ss",idx,secIdx,thirdIdx,l[idx],l[secIdx],l[thirdIdx]
                    l.pop(idx)
                    l.pop(secIdx - 1)
                    l.pop(thirdIdx - 2)
                    num = num + 1
                    found = True
                    # print "tmpl3", l
                    break
            if found:
                break
            else:
                idx = 0
        if allSearch:
            break
    # print "c3",l
    return num



def cc4(l, candy):
    num = 0
    found = False
    while len(l):
        idx = 0
        if len(l) <= candy:
            num = num + 1
            l[:] = []
            break
        allSearch = False
        for secIdx in xrange(idx + 1, len(l)):
            if secIdx == len(l) - 1:
                allSearch = True
            for thirdIdx in xrange(secIdx + 1, len(l)):
                for forthIdx in xrange(thirdIdx + 1, len(l)):
                    # print "ss",idx,secIdx,thirdIdx,l[idx],l[secIdx],l[thirdIdx],l[forthIdx]
                    if (l[idx]+l[secIdx] + l[thirdIdx]+l[forthIdx]) % candy == 0:
                        l.pop(idx)
                        l.pop(secIdx - 1)
                        l.pop(thirdIdx - 2)
                        l.pop(forthIdx - 3)
                        num = num + 1
                        found = True
                        # print "tmpl4", l
                        break
                if found:
                    break
            if found:
                break
        if found or allSearch:
            break
    return num



def testcode():
    l1 = ['4', '5', '6','4']
    l11 = ['4', '5', '6','4']
    l2 = ['1','1','1']
    l1 = [int(i) for i in l1]
    l11 = [int(i) for i in l1]
    l2 = [int(i) for i in l2]
    l3 = [71,52,52,77,77,6,17,14,41,28,74,25,64,88,27,65,32,24,23,28,13,
          17,13,97,77,58,32,24,1,43,22,49,58,67,37,6,49,92,56,35,31,15,92,
          82,16,54,22,55,76,17,43,16,88,96,97,46,72,22,2,37,28,22,33,55,56,
          58,39,21,58,11,1,67,40,4,44,52,70,2,37,4,13,1,53,91,87,43,58,13,62,
          77,73,98,43,97,71,34,66,58,88,95]
    l4 =[31,85,87,85,69,23,81,81,67,21,41,45,91,9,93,85,87,81,23,65,61,45,93]
    l5 = [65,21,67,1,49,5,33,34,13,6,74,5,85,94,78,33,29,42,77,29,97,34,73,52,89,15,74,40,57,91,29,69,70,41,74,
           69,75,49,81,22,76,25,97,86,38,14,94,51,82,81,85,73,88,84,19,93,14,38,37,45,11,6,17,1,89,46,51,17,33,17,
           9,77,78,51,29,29,37,91,46,30,54,51,3,83,85,45,81,9,89,21,58,64,55,74,89,21,33,81,73,61]
    ll5 = [i for i in l5 if i%4 != 0]
    print ll5
    print len(l5) - len(ll5)
    # print len(l4)
    # l44 =[45,9,93,85,81,65,61,45,93] #7
    # print len(l44)
    # l45 = [93] #3
    # print l1[0:3],l1[1:2]
    # print  sum(l1[0]+i for i in l1[0:4])-len(l1[0:4])*l1[0]
    # Case #1: 3
    # Case #2: 4
    # Case #3: 1
    # Case #4: 53
    # Case #5: 10
    # Case #6:
    # res = CalcSatisfiedTeamNum(l1,4,3)#
    # print "res1:"+str(res)
    # print "res2:"+str(CalcSatisfiedTeamNum(l11,4,2))
    # print "res3:"+str(CalcSatisfiedTeamNum(l2,3,3))
    # print "res4:"+str(CalcSatisfiedTeamNum(l3,100,3))
    # print "res5:"+str(CalcSatisfiedTeamNum(l4,23,4))
    print "res6:"+str(CalcSatisfiedTeamNum(l5,100,4))


def test2():
    # l1 = [4, 5, 6, 9, 6,4]
    # cc1(l1,3)
    # print "l1", l1
    # l2 = [4, 5, 4 ,5 ,4]
    # cc2(l2,3)
    # print l2
    l3 = [71,52,52,77,77,6,17,14,41,28,74,25,64,88,27,65,32,24,23,28,13,
          17,13,97,77,58,32,24,1,43,22,49,58,67,37,6,49,92,56,35,31,15,92,
          82,16,54,22,55,76,17,43,16,88,96,97,46,72,22,2,37,28,22,33,55,56,
          58,39,21,58,11,1,67,40,4,44,52,70,2,37,4,13,1,53,91,87,43,58,13,62,
          77,73,98,43,97,71,34,66,58,88,95]

    # l31 = [71,52,52,77,77,17,14,41,28,74,25,64,88,65,32,23,28,13,
    #       17,13,97,77,58,32,1,43,22,49,58,67,37,49,92,56,35,31,92,
    #       82,16,22,55,76,17,43,16,88,97,46,22,2,37,28,22,55,56,
    #       58,58,11,1,67,40,4,44,52,70,2,37,4,13,1,53,91,43,58,13,62,
    #       77,73,98,43,97,71,34,58,88,95]

     # l3 = [43,16,88,97,46,22,37,28,22,55,
    #       58,58,1,67,40,4,52,70,37,4,13,1,53,91,43,58,13,62,
    #       77,73,43,97,34,58,88,95]

    l4 = [i for i in l3 if i% 3 == 0]
    print l4
    for i in l4:
        l3.remove(i)
    print l3
    ii = [46,22,37,28,22,55,
          58,58,1,67,40,4,52,70,37,4,13,1,91,43,58,13,
        73,43,97,34,58,88]
    print "ii",len(ii)
    l5 = [i%3 for i in ii]
    print l5
    #     [ 1, 1, 1,  1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1,  1,  1, 1, 1,  1, 1,
    #  1, 1, 1,  1, 1,   1, 1]
    l6 = [ 1, 1, 1,  1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1,  1,  1, 1, 1,  1, 1, 1, 1, 1,  1, 1,   1, 1]
    print len(l6)
    l7 = [55,76,43,16,88,97,46,22,37,28,22,55,
          58,58,1,67,40,4,52,70,37,4,13,1,53,91,43,58,13,62,
          77,73,98,43,97,71,34,58,88,95]
    print len(l7)

if __name__ == '__main__':
    # testcode()
    # test2()
    # print sum([ll[i,1],ll[0]])
    GetAllSatisfiedTeamNumber('Candy_small_1509165595493')
    GetAllSatisfiedTeamNumber('Candy_large_1509165618808')
    # getDigiStr('Candy_small_1509165595493')
