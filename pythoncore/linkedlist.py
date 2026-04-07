class Node: 
    def __init__(self,data):
        self.data=data
        self.next=None

class singlylinkedlist:
    def __init__(self) -> None:
        self.head=None
#display
    def display(self):
        if self.head is None:
            print("empty")
        else:
            curr=self.head
            while curr is not None:
                print(curr.data)
                curr=curr.next


    #input sll using append
    def append(self,data):
        newnode=Node(data)
        #if self.head is None:
        if self.head is None:
            self.head=newnode
        else:
            curr=self.head
            while curr is not None:
                curr=curr.next
            curr.next=newnode

    # traversal
    def traverse(self):
        if self.head is None:
            print("empty head")
        else:
            curr=self.head
            while curr.next is not None:
                print(curr.data,end='->')
                curr=curr.next
            print()
    
    # insert at position
    def insert_At(self,data,pos):
        newnode=Node(data)
        if pos==0:
            newnode.next=self.head
            self.head=newnode
        else:
            current=self.head
            prev=None
            count=0
            while current is not None and count<pos:
                prev=current
                current=current.next
                count+=1
            prev.next=newnode
            newnode.next=current
    
    def insertat(self,data,pos):
        newnode=Node(data)
        if pos==0:
            newnode.next=self.head
            self.head=newnode
        else:
            current=self.head
            prev=None
            count=0
            while current.next is not None and count<pos:
                prev=current.next
                current=current.next
                count+=1
            prev.next=newnode
            newnode.next=current
        
    # delte node

    def delete(self,data):
        temp=self.head
        if temp.next is  not None:
            if temp.data == data:
                self.head=temp.next
            else:
                found=False
                prev=None
                while temp is not None:
                    if temp.data==data:
                        found=True
                        break
                    prev=temp
                    temp=temp.next
                    if found:
                        prev.next=temp.next


sll=singlylinkedlist()
sll.append(50)
