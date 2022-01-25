#!/usr/bin/python3
""" Creates a class called Node
"""


class Node:
    
    def __init__(self, data, next_node=None):
        """
                Instantiation with size
        Args:
            data: data of the node
            next_node: next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Returns data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        sets data of node
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Returns next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        sets next node value
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


""" Creates an class called SinglyLinkedList
"""

class SinglyLinkedList:
    def __str__(self):
        """
             Instantiation with size
        Args:
            data: data of the node
            next_node: next node
        """
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self):
        """
        sets data of node
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        sets data of node
        """
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
