class node:
    def __init__(self,marks):
        self.marks=marks
        self.next=None
        
m1=node(99)
m2=node(98)
m3=node(97)
m4=node(96)
m5=node(95)
m6=node(94)

m1.next=m2
m2.next=m3
m3.next=m4
m4.next=m5
m5.next=m6

new_node=node(100)
new_node.next=m1
m1=new_node

shayan=m1
while shayan:
    print(shayan.marks,end=" -> ")
    shayan=shayan.next