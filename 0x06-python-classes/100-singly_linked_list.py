#!/usr/bin/python3
class Node:
    """defines a node of a singly linked list
    Attributes:
        __data (int): Node object data
        __next_node (Node or Node): Node object's next node
    """
    def __init__(self, data, next_node=None):
        """instantiates the node object
        Args:
            data (int): node's data
            next_node (Node or None): node's next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """data setter
        Args:
            value (int): new data of node object
        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """next node getter"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """next node setter
        Args:
            value (Node or None): next node
        """
        if value == None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """defines a singly linked list
    Attributes:
        __head (Node or None): head of linked list object
    """
    def __init__(self):
        """instantiates the linked list object"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list 
        (increasing order)
        Args:
            value (int): data of new node"""
        if isinstance(value, int):
            if self.__head == None or self.__head.data >= value:
                node = Node(value, self.__head)
                self.__head = node
            else:
                tmp = self.__head
                while tmp.next_node is not None:
                    if tmp.next_node.data >= value:
                        break
                    tmp = tmp.next_node
                node = Node(value, tmp.next_node)
                tmp.next_node = node
        else:
            raise TypeError("value is not an integer")

    def __str__(self):
        """makes the list printable (one node number per line)"""
        plist = ""
        tmp = self.__head
        while tmp:
            plist += f"{tmp.data}"
            if tmp.next_node != None:
                plist += "\n"
            tmp = tmp.next_node
        return (plist)

