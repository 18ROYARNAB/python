# class Node:
#     def __init__ (self,data):
#         self.data=data
#         self.next=None
        
# class singlylinkedlist:
#     def __init__ (self)->None:
#         self.head=None

#     def append(self,data):
#         newnode=Node(data)
#         if self.head is None:
#             self.head=newnode
#         else:
#             current=self.head
#             while current.next is not None:
#                 current=current.next
#             current.next = newnode
            
#     def traverse(self):
#         if self.head is  None:
#             print("empty linked list")
#         else:
#             current=self.head
#             while current is not None:
#                 if current.next is not None:
#                     print(current.data,end="->")
#                 else:
#                     print(current.data)
#                 current=current.next
            

# sll=singlylinkedlist()
# sll.append(29)
# sll.append(20)
# sll.append(38)

# sll.traverse()
# sll.append(39)
# sll.traverse()


class Node: 
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self)->None:
        self.head=None
    def append(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=newnode
            
    def traverse(self):
        if not self.head:
            print("empty linked list")
        else:
            curr=self.head
            while curr is not None:
                if curr.next is not None:
                    print(curr.data,end="->")
                else:
                    print(curr.data)
                curr=curr.next
                
sll= singlelinkedlist()
sll.append(30)
sll.append(40)
sll.traverse()