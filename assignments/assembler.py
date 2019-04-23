import binascii

def hexacon(k):
    z=bin(int(k, 16))[2:]
    return z

def binacon(k):
    c=hex(int(k,2))
    return c[2:]
    
o=0
with open("new.txt","r") as q:
    for l in q:
        o+=1
q.close()
x=""

j=open("binary.txt","w")
a=open("new.txt","r")
for i in range(o):
    b=a.readline()
    d={"and":"000","lda":"010","add":"001","sta":"011","bun":"100","cal":"101","sub":"110"}
    di={"cla":"7800","cma":"7400","inc":"7200","hlt":"7100","inp":"f800","out":"f400","ski":"f200","sko":"f100","ion":"f080","iof":"f040"}
    c=b.split()
    k=c[0]
    if k in di:
        u=di[k]
        v=hexacon(u)
        if len(v)==16:
            v=v
        else:
            v="0"+v
        j.write(v)
        x+=v
        j.write("\n")
        
    else:
        l=k
        g=c[1][:3]
        w=l[:3]
        z=d[w]
        if l[-1]=="#":
            z="0"+z
        elif l[-1]=="@":
            z="1"+z
        p=z
        q=hexacon(g)
        r=binacon(z)
        z=r+g
        n=len(q)
        b=12-n
        if n<12:
            q=("0"*b)+q
        else:
            q=q
        p=p+q
        j.write(p)
        j.write("\n")
        x+=p


a.close()
j.close()

#-------------writing------------------
original_string = x

bit_strings = [original_string[i:i + 8] for i in range(0, len(original_string), 8)]

byte_list = [int(b, 2) for b in bit_strings]

with open('byte.bin', 'wb') as f:
    f.write(bytearray(byte_list))
f.close()


#----------------reading-----------------

w=open("byte.bin","rb")
q=w.read()
k=binascii.hexlify(q)
z=str(k)
q=z[2:]
e=q[:-1]
o=0
j=4
for i in range(1,len(e),4):
    print(e[o:j])
    o+=4
    j+=4
    
w.close()
