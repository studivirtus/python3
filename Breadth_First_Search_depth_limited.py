#-------------------------------------------------------------------------------
# Name:        Breadth-First Search depth limited
# Purpose:
#
# Author:      Michael Mullen
#
# Created:      OCT 2013
# Copyright:   Open Source (c) Michael 2013
# Licence:     Open Source
#-------------------------------------------------------------------------------

'''class node:
    nValue = 0
    pNode = 0
    nCost = 0
    nDepth = 0
    def __init__(self, nodeValue,parentNode,nodeCost,nodeDepth):
        self.nValue = nodeValue
        self.pNode = parentNode
        self.nCost = nodeCost
        self.nDepth = nodeDepth
    def getChildren(self,pNode):
        """get children of a node"""
        rNode = pNode.nValue*2
        lNode = pNode.nValue*2+1
        return[node(rNode,pNode.nValue,pNode.nCost,(pNode.nDepth + 1)),node(lNode,pNode.nValue,pNode.nCost,(pNode.nDepth + 1))]
    '''

class breadthFirstSearch():
    """ Completes a breadth-first search"""
    """NOTE providing '0' as a 'maxDepth' value allows an infinit search depth"""
    frontier = list()
    explored = list()
    tested = list()
    goal = 0
    maxDepth = 0
    reactionIndex = 0

    #nodesAtMaxDepth()

    def __init__(self,firstNode,goalValue,maxDepth,reactionIndex):
        self.frontier.append(firstNode)
        self.goal = goalValue
        self.maxDepth = maxDepth
        self.reactionIndex = reactionIndex

    def explore(self):
        """Explore for a solution"""
        curNode = node(0,0,0,0)
        solutionNode = (0,0,0,0,)
        found = False
        self.frontierIsEmpty()

        #test root node
        if not self.frontierIsEmpty():
            curNode = self.frontier[0]
            if(self.goalReached(curNode.nValue)):
                found = True
            if(self.goalReached(curNode.nValue)):
                found = True
            self.tested.append(curNode)

        #test child nodes
        while((not self.frontierIsEmpty()) and (not found)):

            """print('-----------------new-----------------')#DEBUG
            print('current frontier:')#DEBUG
            self.printlist(self.frontier)#DEBUG
            print('current tested nodes:')#DEBUG
            self.printlist(self.tested)#DEBUG
            print('current explored nodes:')#DEBUG
            self.printlist(self.explored)#DEBUG"""

            curNode = self.frontier.pop(0)
            #print('current node is: %i' % curNode.nValue) #DEBUG
            self.explored.append(curNode)
            if (curNode.nDepth < self.maxDepth or  self.maxDepth == 0):
                children = curNode.getChildren(self.reactionIndex)
                for child in children:
                    #print (child.nValue) #DEBUG
                    if self.goalReached(child.nValue):
                        found = True
                        solutionNode = child
                        self.tested.append(child)
                        break
                    elif (not self.inExplored(child.nValue)) and (not self.inFrontier(child.nValue)):
                        self.addToFrontier(child)
                    self.tested.append(child)
        if(found):
            print("Breadth-First Search FOUND A SOLUTION %i" % solutionNode.nValue)
            print("here are the nodes visited:")
            self.printlist(self.tested)
        elif not found and self.frontierIsEmpty():
            print("FAILURE, Breadth-First Search did not find a solution")
            print("here are the nodes visited:")
            self.printlist(self.tested)

    def inExplored(self,curValue):
        """check if node state is in explored list"""
        for x in self.explored:
            if( curValue == x.nValue):
                return True
        return False

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
        self.frontier.append(curNode)

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




def main():
    pass


if __name__ == '__main__':
    '''main()
    goalNode = 15
    maxDepth = 0

    startingNode = node(1,0,0,0)

    BFS = breadthFirstSearch(startingNode,goalNode,0)
    BFS.explore()

    print("DONE")
    '''