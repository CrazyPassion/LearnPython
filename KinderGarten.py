# KinderGarten
# -*- coding: utf-8 -*-
import re

def calcrange0(teamGroup, range, candyNumInCan):
    x = 0
    teamNum = 0
    while teamGroup:
        if(len(teamGroup) <= range + 1):
            teamNum = teamNum + 1
            # print "a0"
            break
        if (x >= len(teamGroup)):
            break
        if (teamGroup[x] % candyNumInCan == 0):
            # print "yes"
            teamNum = teamNum + 1
            teamGroup.pop(x)
            x = 0
        else:
            x = x + 1
    # print "end1"
    # print teamGroup
    # print "end11"
    return teamNum



def calcrange1(teamGroup, range, candyNumInCan):
    start = 0
    teamNum = 0
    while len(teamGroup):
        x = start
        # print teamGroup
        # print tmplist2
        # if(range == candyNumInCan - 1):
        #     teamNum = teamNum + 1
        #     break
        if(len(teamGroup) <= range + 1):
            teamNum = teamNum + 1
            # print "a1"
            break
        for y in xrange(x+1,len(teamGroup) - 1):
            # print "222"
            # print tmplist
            # print len(tmplist)
            # if(len(teamGroup) == 1):
            #     break;
            sum = teamGroup[x] + teamGroup[y]
            # print teamGroup[x], teamGroup[y]
            # print sum
            if(sum % candyNumInCan == 0):
                teamNum = teamNum + 1
                # print "a2"
                teamGroup.pop(x)
                teamGroup.pop(y - 1)
                # print "del"
                break
            elif(y == len(teamGroup)-2):
                # ddd=teamGroup[x]
                start = start + 1
                # print "cannot find pair"
                # print ddd
                # tmplist2.append(ddd)
                # tmplist.pop(x)
                break
            else:
                pass
                # print "---"
        # print "start"+str(start)+"len"+str(len(teamGroup))
        if (start == len(teamGroup) - 2):
            break
    return teamNum



def calcrange2(teamGroup, range, candyNumInCan):
    teamNum = 0
    start = 0
    while len(teamGroup):
        x = start
        # print teamGroup
        # print tmplist2
        # print len(teamGroup)
        if(len(teamGroup) <= range + 1):
            teamNum = teamNum + 1
            # print "a111"
            break
        for y in xrange(x+1,len(teamGroup) - 1):
            # print "222"
            # print tmplist
            for z in xrange(y+1,len(teamGroup)):
                # print len(teamGroup)
                if(len(teamGroup) == 2):
                    break;
                sum = teamGroup[x] + teamGroup[y] + teamGroup[z]
                # print int(tmplist2[x]), int(tmplist2[y]), int(tmplist2[z])
                # print sum
                if(sum % candyNumInCan == 0):
                    teamNum = teamNum + 1
                    teamGroup.pop(x)
                    teamGroup.pop(y - 1)
                    teamGroup.pop(z - 2)
                    # print tmplist2
                    # print "del2"
                    break
                elif(z == len(teamGroup)-1):
                    # ddd=tmplist2[x]
                    # print "cannot find pair2"
                    # print ddd
                    start = start + 1
                    # tmplist3.append(ddd)
                    # tmplist2.pop(x)
                    break
                else:
                    # print "---2"
                    pass
        if start == len(teamGroup) - 2:
            break
    return teamNum


def calcrange3(teamGroup, range, candyNumInCan):
    teamNum = 0
    start = 0
    while len(teamGroup):
        x = start
        # print teamGroup
        # print tmplist2
        # print len(teamGroup)
        if(len(teamGroup) <= range + 1):
            teamNum = teamNum + 1
            # print "a111"
            break
        for y in xrange(x+1,len(teamGroup) - 1):
            # print "222"
            # print tmplist
            for z in xrange(y+1,len(teamGroup)):
                # print len(teamGroup)
                if(len(teamGroup) == 2):
                    break;
                sum = teamGroup[x] + teamGroup[y] + teamGroup[z]
                # print int(tmplist2[x]), int(tmplist2[y]), int(tmplist2[z])
                # print sum
                if(sum % candyNumInCan == 0):
                    teamNum = teamNum + 1
                    teamGroup.pop(x)
                    teamGroup.pop(y - 1)
                    teamGroup.pop(z - 2)
                    # print tmplist2
                    # print "del2"
                    break
                elif(z == len(teamGroup)-1):
                    # ddd=tmplist2[x]
                    # print "cannot find pair2"
                    # print ddd
                    start = start + 1
                    # tmplist3.append(ddd)
                    # tmplist2.pop(x)
                    break
                else:
                    # print "---2"
                    pass
        if start == len(teamGroup) - 2:
            break
    return teamNum

def CalcTeamNum(teamGroup, range, candyNumInCan):
    teamNum = 0
    if (range == 0):
        teamNum = calcrange0(teamGroup, range, candyNumInCan)      
    elif (range == 1):
        teamNum = calcrange1(teamGroup, range, candyNumInCan)
    elif(range == 2):
        teamNum = calcrange2(teamGroup, range, candyNumInCan)
     elif(range == 3):
        teamNum = calcrange3(teamGroup, range, candyNumInCan)
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
            candyNumInCan = int(digi[1])
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



def testcode():
    l1 = ['4', '5', '6','4']
    l11 = ['4', '5', '6','4']
    l2 = ['1','1','1']
    l1 = [int(i) for i in l1]
    l11 = [int(i) for i in l1]
    l2 = [int(i) for i in l2]
    # # print  sum(l1[0]+i for i in l1)
    # Case #1: 3
    # Case #2: 4
    # Case #3: 1
    # res = CalcSatisfiedTeamNum(l1,4,3)#
    # print "res1:"+str(res)
    # print "res2:"+str(CalcSatisfiedTeamNum(l11,4,2))
    print "res3:"+str(CalcSatisfiedTeamNum(l2,3,3))



if __name__ == '__main__':
    # testcode()
    # print sum([ll[i,1],ll[0]])
    GetAllSatisfiedTeamNumber('Candy_small_1509165595493')
    GetAllSatisfiedTeamNumber('Candy_large_1509165618808')
    # getDigiStr('Candy_small_1509165595493')
