""" MAKING A LINKED LIST """
class Node:
    """ NODE LINKED LIST"""
    def __init__(self,data :int)->None:
        self.data=data # INITAL DATA
        self.head=None # NULL AS LOCATION YET TO ADD
# END-OF-BLOCK

class Singly:
    """Creating a linked list """
    def __init__(self)->None:
        self.head=None
    def append(self,data):
        """Append function helps to connect newnode to linkedlist"""
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            current=self.head
            while current.next is not None:
                current.next=newnode
                current=current.next
                
