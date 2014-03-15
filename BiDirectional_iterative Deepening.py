#-------------------------------------------------------------------------------
# Name:        Best-First Search
# Purpose:
#
# Author:      Michael Mullen
#
# Created:      OCT 2013
# Copyright:   Open Source (c) Michael 2013
# Licence:     Open Source
#-------------------------------------------------------------------------------
import bisect
import operator

class node:
    nValue = 0
    pNode = 0
    nCost = 0
    nDepth = 0
    maxDepth = 0
    def __init__(self, nodeValue,parentNode,nodeCost,nodeDepth,maxDepth):
        self.nValue = nodeValue
        self.pNode = parentNode
        self.nCost = nodeCost
        self.nDepth = nodeDepth
        self.maxDepth = maxDepth

    def __lt__(self,other):
        return self.nCost < other.nCost
    def __gt__(self,other):
        return self.nCost > other.nCost

    def hasChildren(self):
        """verify that the node has children"""
        """NOTE if maxDepth set to '0' maxDepth is infinite"""
        if (self.nDepth < self.maxDepth or self.maxDepth == 0):
            return True
        return False

    def getChildren(self,curNode):
        """get children of a node"""
        uNode = node(int(curNode.nValue/2),curNode,curNode.nCost,(curNode.nDepth + 1),curNode.maxDepth)
        lNode = node(curNode.nValue*2,curNode,curNode.nCost,(curNode.nDepth + 1),curNode.maxDepth)
        rNode = node(curNode.nValue*2+1,curNode,curNode.nCost,(curNode.nDepth + 1),curNode.maxDepth)


        if curNode.nValue == 0:
            return []
        elif uNode.nValue == 0:
            return[lNode,rNode]
        elif uNode.nValue == curNode.pNode.nValue:
            return[lNode,rNode]
        elif rNode.nValue == curNode.pNode.nValue:
            return[uNode,lNode]
        elif lNode.nValue == curNode.pNode.nValue:
            return[uNode,rNode]
        elif lNode.nValue >= 16 or rNode.nValue >= 16:
            return[uNode]
        else:
            return[uNode,lNode,rNode]

class BiDirectionalIterativeDeepeningSearch():
    """ Completes a depth first search"""
    frontier = list() #sorted list
    hash = dict()
    nodesVisited = list()
    firstNode = node(0,0,0,0,0)
    secondNode = node(0,0,0,0,0)
    solutionNode = node(0,0,0,0,0)
    goal = 0
    depthLimit = 0

    def __init__(self,firstNode,secondNode):
        self.firstNode = firstNode
        self.secondNode = secondNode

    def explore(self):
        """Explore for a solution"""
        curNode = node(0,node(0,0,0,0,0),0,0,0)

        found = False

        #test child nodes
        while not found:

            if self.depthLimit <= self.firstNode.maxDepth:
                self.frontier.clear()
                #print("----------FIRST NODE----------") #DEBUG
                self.addToFrontier(self.firstNode)
                found = self.itrExplore()
            if self.depthLimit <= self.secondNode.maxDepth and not found:
                self.frontier.clear()
                #print("----------SECOND NODE----------") #DEBUG
                self.addToFrontier(self.secondNode)
                found = self.itrExplore()
            self.depthLimit = self.depthLimit+1



        if(found):
            print("Bidirectional search met at %i" % self.solutionNode.nValue)
            print("here are the nodes visited:")
            self.printlist(self.nodesVisited)
        elif not found:
            print("FAILURE, Bidirectional search did not find a solution")
            print("here are the nodes visited:")
            self.printlist(self.nodesVisited)


    def itrExplore(self,):
        found = False
        futureHash = list()
        while((not self.frontierIsEmpty()) and (not found)):
            reverseChildren = list()
            """print('-----------------new-----------------')#DEBUG
            print('current frontier:')#DEBUG
            self.printlist(self.frontier)#DEBUG
            print('current visited nodes:')#DEBUG
            self.printlist(self.nodesVisited)#DEBUG
            print(self.hash.keys()) #debug
            #self.printlist(self.hash.keys()) #debug"""
            curNode = self.frontier.pop(0)
            #print("current node: %i" %curNode.nValue) #DEBUG"""
            if self.goalReached(curNode.nValue):
                found = True
                self.solutionNode = curNode
                self.addNodesVisited(curNode)
                break
            self.addNodesVisited(curNode)
            if not self.atDepthLimit(curNode):
                if curNode.hasChildren():
                    children = curNode.getChildren(curNode)
                    for x in range(len(children)):
                        reverseChildren.insert(0,children.pop(0))
                    for child in reverseChildren:
                        self.addToFrontier(child)
            if self.atDepthLimit(curNode):
                futureHash.append(curNode)
                """print("FUTURE HASH")#DEBUG
                self.printlist(futureHash) #debug"""
        self.clearHash()
        self.toHash(futureHash)
        futureHash.clear()
        return found

    def toHash(self,frontier):
        for leafNode in frontier:
            self.hash[leafNode.nValue] = leafNode

    def clearHash(self):
        self.hash.clear()

    def atDepthLimit(self,curNode):
        if curNode.nDepth == self.depthLimit:
            return True
        return False

    def addNodesVisited(self,curNode):
        self.nodesVisited.append(curNode)

    def frontierIsEmpty(self):
        """check if frontier is empty"""
        if (len(self.frontier) > 0):
            return False
        return True

    def addToFrontier(self,curNode):
        """add node to frontier"""
        self.frontier.insert(0,curNode)


    def goalReached(self,nValue):
        """YAY GOAL IS REACHED WE"RE DONE"""
        if nValue in self.hash:
            return True
        return False

    def printlist(self,list):
        """Utility for printing lists"""
        for item in list:
            print(item.nValue,end=', ')
        print('')
    def printlist(self,list):
        """Utility for printing lists"""
        for item in list:
            print(item.nValue,end=', ')
        print('')

def main():
    pass


if __name__ == '__main__':
    main()
    goalNode = 15
    maxNodeDepth = 3
    depthLimit = 3


    node1 = 1
    node2 = 15

    startingNode = node(node1,node(0,0,0,0,0),0,0,maxNodeDepth)
    endingNode = node(node2,node(0,0,0,0,0),0,0,maxNodeDepth)

    BIDIR = BiDirectionalIterativeDeepeningSearch(startingNode,endingNode)
    BIDIR.explore()

print("DONE")