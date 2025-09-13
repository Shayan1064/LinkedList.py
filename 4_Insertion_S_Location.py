class node:
    def __init__(self,marks):
        self.marks=marks
        self.next=None
        
number=int(input("Enter Nodes: "))
head=None
tail=None

for i in range(number):
    marks=int(input("Enter Marks: "))
    new_node=node(marks)
    if head is None:
        head=new_node
        tail=head
    else:
        tail.next=new_node
        tail=new_node
position=int(input("Enter position: "))
n1=int(input("Enter New_Node: "))
new_node=node(n1)
if position==0:
    new_node.next=head
    head=new_node
else:
    tail=head
    for i in range(position-1):
        tail=tail.next
    new_node.next=tail.next
    tail.next=new_node
    
    
shayan=head
while shayan:
    print(shayan.marks,end=" -> ")
    shayan=shayan.next
        