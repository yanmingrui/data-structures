#realize the stack by array-structure
#it would be better to realize and understand the stack by linkedlist while using python
class Stack:
    #initialize:初始化
    def __init__(self):
        self.__top = 0
        self.__length = 0
        self.__data = []

#push the value
    def Push(self, val):
        '''

        :param val:push this value in the stack:入栈
        :return:
        '''
        self.__top += 1
        self.__length += 1
        self.__data.append(val)

#show the value at the top of the stack
    def Top(self):
        data = self.__data[self.__top - 1]
        return data

#delete the value at the top of the stack
    def Pop(self):
        #have no idea to show deleting the top element by array
        #if use linked list,i can make the node before Top point to null to show this Pop process :)
        #maybe use module:array better?
        #在python里，用链表更能动态的表现弹出这一过程。如果用数组表示的话，只能用重新赋值表示。或者可以调用arraymodule
        self.__data = self.__data[:-1]
        self.__top -= 1
        self.__length -= 1

    def __str__(self):
        return str(self.__data[self.__top - 1])
a = Stack()
a.Push(2)
a.Push(3)
a.Push(4)
print(a.Top())
a.Pop()

print(a)
