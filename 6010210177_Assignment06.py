import random
import string

class LinkedList(object):

    class Node(object):
        def __init__(self,item, next=None):

            self.data = item
            self.next = next

    def __init__(self):

        self._head = None


    def insertBegin(self, item):

        if self._head is None:
            self._head = LinkedList.Node(item)
        else:
            newNode = LinkedList.Node(item)
            newNode.next = self._head
            self._head = newNode

    def appendvalue(self, item):

        if self._head is None:
            self._head = LinkedList.Node(item)
        else:
            newNode = LinkedList.Node(item)
            curNode = self._head
            while curNode.next is not None:
                curNode = curNode.next
            curNode.next = newNode
    def search(self):
        curNode = self._head
        index = 0
        found = False
        while curNode is not None and found is not True:
            if curNode.data is 'a':
                curNode.data = None
                found = True
            else:
                curNode = curNode.next
                index += 1

    def visitNode(self):
        curNode = self._head
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.next

def randomString(stringLength):

    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(int(stringLength)))

def main(listitem):
    strlist = []
    for i in range(len(listitem)): #split the string to list
        strlist.append(listitem[i])
    stringlist = LinkedList()
    for i in range(len(charlist)): #append the string in list to linklist
        stringlist.appendvalue(strlist[i])

    stringlist.search()
    print("Linked list")
    stringlist.visitNode()


if __name__ == '__main__':
    charlist = randomString(20)
    main(charlist)
