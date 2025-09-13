class node:
    def __init__(self,marks):
        self.marks=marks
        self.next=None
        
n=int(input("Enter how many nodes your are going to enter: "))
head=None
tail=None

for i in range(n):
    marks=int(input("Enter Marks: "))
    new_node=node(marks)
    if head is None:
        head=new_node
        temp=head
    else:
        temp.next=new_node
        temp=temp.next
        
shayan=head
while shayan:
    print(shayan.marks,end="->")
    shayan=shayan.next
    
#--------------------------------------------------------------------------------

# # Insertion at beginning.......\
# class node:
        
#         def __init__(self,marks):
#             self.marks=marks
#             self.next=None
            
# nodes=int(input("Enter Your Nodes: "))
# head=None
# tail=None

# for i in range(nodes):
#     marks=int(input("Enter Your marks: "))
#     new_node=node(marks)
#     if head is None:
#         head=new_node
#         tail=head
#     else:
#         tail.next=new_node
#         tail=tail.next
        
# value=int(input("Enter value"))
# new_node=node(value)
# new_node.next=head
# head=new_node
        
# shayan=head
# while shayan:
#     print(shayan.marks,end="->")
#     shayan=shayan.next

#---------------------------------------------------------------------------
# Insertion at End.......\
# class node:
        
#         def __init__(self,marks):
#             self.marks=marks
#             self.next=None
            
# nodes=int(input("Enter Your Nodes: "))
# head=None
# tail=None

# for i in range(nodes):
#     marks=int(input("Enter Your marks: "))
#     new_node=node(marks)
#     if head is None:
#         head=new_node
#         tail=head
#     else:
#         tail.next=new_node
#         tail=tail.next
        
# value = int(input("Enter value to insert at end: "))
# new_node = node(value)
# tail.next = new_node  # attach to the last node
# tail = new_node 
        
# shayan=head
# while shayan:
#     print(shayan.marks,end="->")
#     shayan=shayan.next