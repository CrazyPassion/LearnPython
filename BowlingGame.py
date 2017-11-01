import re

def CalculateAllScore(file_path):
    fp = open(file_path, 'r')
    linenum = 0
    caseNum = 0
    for line in fp:
        print line
        if (linenum == 0):
            # totalCaseNum =
            # print totalCaseNum
            pass
        else:
            score = CalcScore(line)
            print "Case #" + str(caseNum) +": "+str(score)

        linenum = linenum + 1

        print "line" +str(linenum)
        if linenum == 1:
            break
    fp.close()


def testcode():
    l1 = "X|X|X|X|X|X|X|X|X|X||XX" #300
    l2 = "X|7/|9-|X|-8|8/|-6|X|X|X||81"#167
    # print "l1",CalcScore(l1)
    print "l2",CalcScore(l2)

def CalcScore(line):
    mg=re.match(r"(\w|\d?|\S)\|(\w|\d?|\S)\|(\w|\d?\S)\|(\w|\d?\S)\|(\w|\d?\S)\|(\w|\d?\S)\|(\w|\d?\S)\|(\w|\d?\S)\|(\w|\d?\S)\|(\w|\d?\S)\|\|(\w+|\d+).*",line)
    print line
    length = len(mg.groups())
    print length
    tmplist = []
    for i in xrange(1,length):
        # print mg.group(i)
        tmplist.append(mg.group(i))

    print tmplist
    print "end"
    return 0



if __name__ == '__main__':
    testcode()
    # CalculateAllScore(file)