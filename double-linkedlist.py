### python realized double-linkedlist
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : double_linkedList.py
# @Author: yanmingrui
# @Date  : 2018/7/9
# @Desc  :

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoubleLinkedList:
    '''
    the index begins at 0
    '''
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

# judge whethe the linkedlist is empty or not
    def IsEmpty(self):
        if self.head == None:#you can also judge the tail
            return True
        else:
            return False

#add node at the head of linkedlist
    def AddHead(self, val):
        nodeNew = Node(val)

        #judge whethe the linkedlist is empty or not
        # if the list is not Null
        if self.head:
            nodeNew.next = self.head
            self.head.prev = nodeNew
        #if the linkedlist is Null,just intialize the list
        #which means the head and the tail is the same node
        else:
            self.tail = nodeNew
        self.head = nodeNew
        self.length += 1

#delete node at the head of linkedlist
    def DeleteHead(self):
        #firstly,if the list is Null
        #not Null
        if self.head:
            # use id can make the judgement faster
            if id(self.head) != id(self.tail):
                temp = self.head
                self.head.next.prev = None
                self.head = self.head.next
                temp.next = None
            else :
                self.head = None
                self.tail = None
            self.length -= 1
        #Null
        else:
            print("the linkedlist is Null")

#add node at the tail of linkedlist
    def AddTail(self, val):
        nodeNew = Node(val)
        if self.tail:
            nodeNew.prev = self.tail
            self.tail.next = nodeNew
        # if the linkedlist is Null,just intialize the list
        # which means the head and the tail is the same node
        else:
            self.head = nodeNew
        self.tail = nodeNew
        self.length += 1

# delete node at the tail of linkedlist
    def DeleteTail(self):
        # if the list is Null
        if self.tail:
            if id(self.tail) != id(self.head):
                temp = self.tail
                self.tail.prev.next = None
                self.tail = self.tail.prev
                temp.prev = None
            else:
                self.head = None
                self.tail = None
            self.length -= 1
        else:
            print("the list is Null")
#add node in the middle of the linkedlist
    def InsertNode(self,insert_value,index):
        """
        :param insert_value: the value you want to insert
        :param index:the value needs to be inserted just before the index-th node
        :return:no return

        """
        if index > self.length:
            print("error, overflow")
        elif index == 0:
            self.AddHead(insert_value)
        elif index == self.length:
            self.AddTail(insert_value)
        else:
            nodeNew = Node(insert_value)
            nodeFind = self.head
            while(index != 0):
                nodeFind = nodeFind.next
                index -= 1
            nodeNew.next = nodeFind
            nodeFind.prev.next = nodeNew
            nodeNew.prev = nodeFind.prev.next
            nodeFind.prev = nodeNew
            self.length += 1

#delete node in the middle of the linkedlist
    def DeleteNode(self, index):
        '''

        :param after_node: the index-th node to be deleted
        :return: None
        '''
        if index >= self.length:
            print("error, overflow")
        elif index == 0:
            self.DeleteHead()
        elif index == self.length - 1:
            self.DeleteTail()
        else:
            nodeFind = self.head
            while(index != 0):
                index -= 1
                nodeFind = nodeFind.next
            nodeFind.prev.next = nodeFind.next
            nodeFind.next.prev = nodeFind.prev
            nodeFind.next = None
            nodeFind.prev = None
            self.length -= 1

#search node at the index-th
    def SearchNode(self, index):
        if self.length == 0:
            print("it is a null list")
            return None
        else:
            nodeFind = self.head
            while(index != 0):
                index -= 1
                nodeFind = nodeFind.next
            return nodeFind.val
#show the linkedlist in the form of string
    def __str__(self):
        nodeHead = self.head
        print_str=[]
        while(nodeHead):
            print_str.append(str(nodeHead.val))
            if nodeHead.next:
                print_str.append('-->')
                if nodeHead.next.prev:
                    print_str.append('<--')
            nodeHead = nodeHead.next
        return ''.join(print_str)

A = DoubleLinkedList()
A.AddHead(2)
A.AddTail(3)
A.DeleteHead()
A.InsertNode(4,0)
A.InsertNode(4,0)
A.InsertNode(4,3)
A.DeleteNode(2)
print(A.SearchNode(2))
print(A)
```
