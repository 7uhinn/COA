import binascii

ac=0
pc=0
u=[]

#---------creating memory array-------

def create():
    for i in range(4095):
        u.append(None)

def hexacon(k):
    z=bin(int(k, 16))[2:]
    return z

#---------displaying-------------

def display(n):
    global ac
    if n==1:
        print("\n")
        print("ac is : ",ac)
    elif n==2:
        print("pc is : ",pc)
        print("\n")
    else:
        print("\n")
        g=int(input("Enter the index value: "))
        print("The value is:  ",u[g])
            
#---------memory reference-------
            
def reference(e,f):
    global ac
    global pc
    global u
    if e=="000":
        ac=ac and u[f]
    elif e=="001":
        ac=ac+u[f]
    elif e=="010":
        ac=u[f]
    elif e=="011":
        u[f]=ac
    elif e=="100":
        pc=f
    elif e=="101":
        pc=f
    elif e=="110":
        ac=ac-u[f]
        
def memory(i):
    r=hexacon(i)
    if len(r)<16:
        n=16-len(r)
        r=(("0")*n)+r
        return r
    else:
        return r

    
#---------start-------------
    
w=open("byte.bin","rb")
q=w.read()
k=binascii.hexlify(q)
w.close()
z=str(k)
q=z[2:]
e=q[:-1]
l=[]

create()#creating memory array

j=4
o=0
for i in range(1,len(e),4):
    l.append(e[o:j])
    o+=4
    j+=4

d={"000":"and","010":"lda","001":"add","011":"sta","100":"bun","101":"cal","110":"sub"}

for i in l:
    p=memory(i)
    y=p[1:4]
    n=p[0]
    #--------giving memory-----------
    u[330]=6
    u[681]=5
    u[1549]=330
    h=p[4:]
    f=int(h,2)
    if n=="0":
        f=f
    else:
       f=u[f]
    reference(y,f)
    
while True: 
    print("enter 1-Accumulator   2-Program Counter   3-Memory   4-Quit")
    print("\n")
    j=int(input("Enter the block you want to display: "))
    if j==4:
        break
    display(j)
    print("\n")




        


