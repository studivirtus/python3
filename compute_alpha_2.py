#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Michael
#
# Created:     12/03/2014
# Copyright:   (c) Michael 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction
from functools import reduce
import copy
#import Breadth_First_Search_depth_limited


def main():
    pass

class node:
    nValue = 0  #probability of reaching this node
    mIndex = []
    pNode = 0
    nCost = 0
    nDepth = 0
    def __init__(self, nodeValue,parentNode,nodeCost,nodeDepth):
        self.nValue = nodeValue
        self.pNode = parentNode
        self.nCost = nodeCost
        self.nDepth = nodeDepth

    def __eq__(self,other):
        for i in range(len(self.mIndex)):
            if self.mIndex[i][1] != other.mIndex[i][1]:
                return False
        return True

    def getNewMIndex(self, react):
        newMIndex = list()
        tempMIndex = list()
        for m in self.mIndex:
            for r in react.reactants:
                if m[0] == r[0]:
                    tempMIndex.append((m[0],m[1]-r[1])) #subtract the reactant(s)
            for p in react.products:
                if m[0] == p[0]:
                    tempMIndex.append((m[0],m[1]+p[1])) #add the product(s)
        nameIndex = list()
        """for m in tempMIndex:
            if m[0] not in nameIndex:
                nameIndex.append(m[0])
        for n in nameIndex:
            num = 0
            for m in tempMIndex:
                if n == m[0]:
                    num += m[1]
            newMIndex.append((n,num))"""

        return tempMIndex

    def getChildren(self,reactIndex):
        """get children of a node"""
        """rNode = pNode.nValue*2
        lNode = pNode.nValue*2+1
        rNodeCost = pNode.nCost+1
        lNodeCost = pNode.nCost+10"""
        children = list()
        num = 0
        for r in reactIndex:
            alpha = computeAlpha(r,self.mIndex)
            if  alpha > 0:
                probabilities = computeProbablity(reactIndex,self.mIndex)
                newNode = node(probabilities[num][1]*self.nValue, self, 0, self.nDepth +1)
                newNode.mIndex = self.getNewMIndex(r)
                children.append(newNode)
            num += 1
        return children


def nCk(n,k):
  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )



class reaction(object):
    reactants = []
    products = []
    k = 0
    reactionName = ""

    def __init__(self, reactants,products,kIn,reactionName):
        self.reactants = reactants
        self.products = products
        self.k = kIn
        self.reactionName = reactionName


def computeAlpha(reaction,mIndex):
    alpha = reaction.k
    for i in reaction.reactants:
        numMols = 0
        numReact = 0
        numMols = findNumMols(i[0],mIndex)
        numReact = i[1]
        if numMols >= numReact:
            alpha = alpha * nCk(numMols,numReact)
        else:
            return 0
    return alpha


def computeProbablity(rIndex, mIndex):
    probabilities = []
    denominator = 0
    alphas = []
    for r in rIndex:
        alphas.append(computeAlpha(r,mIndex))
    for a in alphas:
        denominator += a
    p=0
    for i in alphas:
        p += 1
    for i in range(p):
        probability = alphas[i]/denominator
        probabilities.append((rIndex[i].reactionName,probability))
    return probabilities


def findNumMols(mName,mIndex):
    for i in mIndex:
        if mName == i[0]:
            return i[1]


def setNumMols(mName,mNum,mIndex):
    newMIndex=[]
    for i in mIndex:
        if mName == i[0]:
            newMIndex.append((mName,mNum))
        else:
            newMIndex.append(i)
    return newMIndex

def getDepth(depth, nodeList):
    done = False
    i = 0
    stopdepth = 5
    goalList = list()
    while not done:
        #print("n equals %d" % len(nodeList))
        #print("i equals %d" % i)
        nodeList = nodeList + nodeList[i].getChildren(reactIndex)
        for n in nodeList[i].getChildren(reactIndex):
            #print (n.mIndex)
            if n.nDepth == stopdepth:
                goalList.append(n)
            elif 1 > len(n.getChildren(reactIndex)):
                goalList.append(n)
        i += 1

        if n.nDepth > stopdepth:
            done = True
        #print("n equals %d" % len(nodeList))
        #print("i equals %d" % i)
        if i >= len(nodeList):
            done = True
    return goalList

def summerize(goalList):
    """goes through a list: it finds molindex's that are the same and compiles
    them together"""

    returnList = list()
    while 0 < len(goalList):
        tempList = list()
        i = 0
        firstNode = goalList[i]

        #print (firstNode.mIndex, firstNode.nValue)

        i+=1
        while i < len(goalList):
            #print(i,len(goalList))
            #print (firstNode.mIndex, firstNode.nValue, "-")
            #print(goalList[i].mIndex, goalList[i].nValue)
            if firstNode == goalList[i]:
               firstNode.nValue = firstNode.nValue + goalList[i].nValue
            else:
                tempList.append(goalList[i])
            i += 1

        returnList.append(firstNode)
        goalList = tempList
    return returnList

def summerizeMolList(goalList):
    """goes through a list: it finds mol's that are the same and compiles
    them together"""

    returnList = list()
    while 0 < len(goalList):
        tempList = list()
        i = 0
        firstNode = goalList[i]

        #print (firstNode.mIndex, firstNode.nValue)

        i+=1
        while i < len(goalList):
            #print(i,len(goalList))
            #print (firstNode.mIndex, firstNode.nValue, "-")
            #print(goalList[i].mIndex, goalList[i].nValue)
            if firstNode == goalList[i]:
               firstNode.nValue = firstNode.nValue + goalList[i].nValue
            else:
                tempList.append(goalList[i])
            i += 1

        returnList.append(firstNode)
        goalList = tempList
    return returnList


if __name__ == '__main__':
    main()

    molIndex = []
    molA = ('a',3)
    molB = ('b',5)
    molC = ('c',7)
    molIndex = [molA,molB,molC]
    print (molIndex)
    nodeList = list()

    reactIndex = []
    r1 = reaction([('a',2),('b',1)],[('c',4)],1,'r1')
    r2 = reaction([('a',1),('c',2)],[('b',3)],1,'r2')
    r3 = reaction([('b',1),('c',1)],[('a',2)],1,'r3')
    reactIndex = [r1, r2, r3]

    stateIndex = []


    print(r1.reactants, r1.products, r1.k)
    for i in r3.reactants:
        print("number of molicules of type")
        print(i[0])
        print(findNumMols(i[0],molIndex))

    for i in r1.products:
        print (i)
    print (computeAlpha(r1,molIndex))
    print(computeProbablity(reactIndex,molIndex))

    startingNode = node(1,0,0,0)
    startingNode.mIndex = molIndex
    print('starting mols')
    print(molIndex)

    print('reaction mols')
    for n in startingNode.getChildren(reactIndex):
        print (n.mIndex)
    nodeList.append(startingNode)


    goalList = getDepth(5,nodeList)

    a = 0
    """for g in goalList:
        print(g.mIndex, g.nValue)
        a += g.nValue
        print (a)
        """

    probMol = list()
    for i in range(len(molIndex)):
        mol = list()
        for g in goalList:
            mol.append([g.mIndex[i],g.nValue])
        probMol.append(mol)

    '''for p in probMol:
        for p2 in p:
            print(p2)
        print("------------------------------------")
    '''
    summerizedMols = list()
    someMols = list()
    doneList = list()
    for p in probMol:
        hackList = ()
        someMols = list()
        hackList = copy.deepcopy(p)
        while 0 < len(hackList):
            tempList = list()
            i = 0
            firstVal = hackList[i]

            #print (firstVal[0], firstVal[1])

            i+=1
            while i < len(hackList):
                #print(i,len(hackList))
                #print (firstVal[0], firstVal[1], "-")
                #print(hackList[i][0], hackList[i][1])
                if firstVal[0][1] == hackList[i][0][1]:
                   firstVal[1] = firstVal[1] + hackList[i][1]
                else:
                    tempList.append(hackList[i])
                i += 1
            someMols.append(firstVal)
            hackList = tempList
        summerizedMols.append(someMols)

    #return summerizedMols
    for s in summerizedMols:
        total = 0
        print("-----------------------")
        print(s[0][0][0])
        for s2 in s:
            total += s2[1]
            print("%d\t%.8f\t%.8f" % (s2[0][1],s2[1], total,))



    '''print('total end cost')
    for g in returnList:
        print(g.mIndex, g.nValue)'''