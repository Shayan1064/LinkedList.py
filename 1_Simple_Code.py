class node:
    def __init__(self,marks):
        self.marks=marks
        self.next=None
        
n1=node(99)
n2=node(98)
n3=node(97)
n4=node(96)
n5=node(95)
        
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5

shayan=n1
while shayan:
    print(shayan.marks,end=" -> ")
    shayan=shayan.next
print("None")