#-------------------------------------------------------------------------------
# Name:        Depth First Search
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
    def __init__(self, nodeValue,parentNode,nodeCost,nodeDepth):
        self.nValue = nodeValue
        self.pNode = parentNode
        self.nCost = nodeCost
        self.nDepth = nodeDepth

    def __lt__(self,other):
        return self.nCost < other.nCost
    def __gt__(self,other):
        return self.nCost > other.nCost

    def getChildren(self,pNode):
        """get children of a node"""
        rNode = pNode.nValue*2
        lNode = pNode.nValue*2+1
        rNodeCost = pNode.nCost+1
        lNodeCost = pNode.nCost+10
        return[node(rNode,pNode.nValue,rNodeCost,(pNode.nDepth + 1)),node(lNode,pNode.nValue,lNodeCost,(pNode.nDepth + 1))]


class depthFirstSeach():
    """ Completes a best-first search"""
    """NOTE providing '0' as a 'maxDepth' value allows an infinit search depth"""
    frontier = list() #sorted list
    explored = list()
    tested = list()
    goal = 0
    maxDepth = 0

    def __init__(self,firstNode,goalValue,maxDepth):
        self.frontier.append(firstNode)
        self.goal = goalValue
        self.maxDepth = maxDepth

    def explore(self):
        """Explore for a solution"""
        curNode = node(0,0,0,0)
        solutionNode = (0,0,0,0)
        found = False
        self.frontierIsEmpty()

        #test child nodes
        while((not self.frontierIsEmpty()) and (not found)):

            """print('-----------------new-----------------')#DEBUG
            print('current frontier:')#DEBUG
            self.printlist(self.frontier)#DEBUG
            print('current explored nodes:')#DEBUG
            self.printlist(self.explored)#DEBUG"""

            curNode = self.frontier.pop(0)
            if self.goalReached(curNode.nValue):
                self.addToExplored(curNode)
                found = True
                solutionNode = curNode
                break
            self.addToExplored(curNode)
            print('current node is: %i' % curNode.nValue) #DEBUG
            if (curNode.nDepth < self.maxDepth or  self.maxDepth == 0):
                children = curNode.getChildren(curNode)
                for child in children:
                    print ("current child value: %i" % child.nValue) #DEBUG
                    if (not self.inExplored(child.nValue)) and (not self.inFrontier(child.nValue)):
                        self.addToFrontier(child)
                    else:
                        childBetter(child)
        if(found):
            print("Best First Seach FOUND A SOLUTION %i" % solutionNode.nValue)
            print("here are the nodes visited:")
            self.printlist(self.explored)
        elif not found and self.frontierIsEmpty():
            print("FAILURE, Best First Search did not find a solution")
            print("here are the nodes visited:")
            self.printlist(self.explored)

    def childBetter(child):
        x = 0
        max = len(self.frontier)
        while x < max:
            if (child.nValue == self.frontier[x].nValue and
                child.nCost < self.frontier[x].nCost):
                frontier[x] = child
                break



    def inExplored(self,curValue):
        """check if node state is in explored list"""
        for x in self.explored:
            if( curValue == x.nValue):
                return True
        return False

    def addToExplored(self,curNode):
        self.explored.append(curNode)

    def inFrontier(self,curValue):
        """check if node state is in frontier list"""
        for x in self.frontier:
            if( curValue == x.nValue):
                return True
        return False

    def frontierIsEmpty(self):
        """check if frontier is empty"""
        if (len(self.frontier) > 0):
            return False
        return True

    def addToFrontier(self,curNode):
        """add node to frontier"""
        if self.frontierIsEmpty():
            self.frontier.append(curNode)
        else:
            bisect.insort_right(self.frontier,curNode)


    def goalReached(self,nValue):
        """YAY GOAL IS REACHED WE"RE DONE"""
        if nValue == self.goal:
            return True
        return False

    def printlist(self,list):
        """Utility for printing lists"""
        for item in list:
            print(item.nValue,end=', ')
        print('')
    def printListAndCost(self,list):
        for item in list:
            print(item.nValue,end=':')
            print(item.nCost,end=", ")
        print('')





def main():
    pass


if __name__ == '__main__':
    main()
    goalNode = 15
    maxDepth = 3

    startingNode = node(1,0,0,0)

    DFS = depthFirstSeach(startingNode,goalNode,maxDepth)
    DFS.explore()

print("DONE")