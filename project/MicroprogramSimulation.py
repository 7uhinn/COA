ar = 0
ac = -1
pc = 0
dr = ""
car = 0
ad = 0
sbr = 0
mm = {}
cm = {}
opbin = ""
modebit = ""
opstr = ""


def mainmemory():
    for i in range(2048):
        mm[i] = None


mainmemory()
mm[132] = "0000000000001111"
mm[15] = "00000000000000110"

def controlmemory():
    for i in range(128):
        cm[i] = None


controlmemory()


def dectobin(k):
    z = bin(int(k))
    return z


def strtobin(k):
    z = int(k, 2)
    y = bin((z))
    return y


def prac(x):
    z = bin(int(x))
    y = str(z)
    t = "0"+y[2:]
    return t


def bintodec(k):
    z = int(k, 2)
    return z


def machineinstructions():
    global ar
    global ac
    global pc
    global dr
    global car
    global ad
    global sbr
    global opbin
    o = 0

    with open("input.txt", "r") as q:
        for k in q:
            o += 1
    q.close()

    a = open("input.txt", "r")

    for i in range(o):
        b = a.readline()
        mlins = {"ADD": "0000", "BRN": "0001",
                 "STR": "0010", "EXC": "0011"}
        b = b.split()
        k = b[0]
        mmadd = b[1][:3]
        opstr = k[:3]
        opbin = mlins[opstr]
        opb = opbin
        if k[-1] == "#":
            modebit = "0"
            opb = modebit+opb
        elif k[-1] == "@":
            modebit = "1"
            opb = modebit+opb
        p = opb
        q = prac(mmadd)
        n = len(q)
        b = 11-n
        if n < 11:
            q = ("0"*b)+q
        else:
            q = q
        l = p+q
        mm[i] = l


machineinstructions()


def addressmapper(a):
    opc = a[1:5]
    map = ("0"+opc+"00")
    return map


def f1(x, y):
    global ar
    global ac
    global pc
    global dr
    global car
    global ad
    global sbr

    if x == "000":
        pass
    elif x == "001":
        dr = strtobin(dr)
        dr = bintodec(dr)
        ac = ac+dr
        dr = prac(dr)
    elif x == "010":
        ac = 0
    elif x == "011":
        ac += 1
    elif x == "100":
        ac = dr
    elif x == "101":
        d = dr[5:16]
        ar = strtobin(d)
        ar = bintodec(ar)
    elif x == "110":
        ar = pc
    elif x == "111":
        mm[ar] = dr


def f2(x):
    global ar
    global ac
    global pc
    global dr
    global car
    global ad
    global sbr
    if x == "000":
        pass
    elif x == "001":
        dr = strtobin(dr)
        dr = bintodec(dr)
        ac = ac-dr
        dr = prac(dr)
    elif x == "010":
        ac = ac | dr
    elif x == "011":
        ac = ac & dr
    elif x == "100":
        dr = mm[ar]
    elif x == "101":
        dr = ac
    elif x == "110":
        dr = dr+1
    elif x == "111":
        pracpc = prac(pc)
        temp = dr[0:5]
        pracdr = temp+pracpc
        drbin = strtobin(pracdr)
        dr = bintodec(drbin)


def f3(x):
    global ar
    global ac
    global pc
    global dr
    global car
    global ad
    global sbr
    if x == "000":
        pass
    elif x == "001":
        dr = dr
        ac = ac ^ dr
    elif x == "010":
        ac = ~ac
    elif x == "011":
        ac = ac << 1
    elif x == "100":
        ac = ac >> 1
    elif x == "101":
        pc = pc + 1
    elif x == "110":
        pc = ar
    elif x == "111":
        pass


def cd(x):
    global ar
    global ac
    global pc
    global dr
    global car
    global ad
    global sbr
    if x == "00":
        return "1"
    elif x == "01":
        return dr[0]
    elif x == "10":
        pracac = prac(ac)
        return pracac[0]
    elif x == "11":
        if ac == 0:
            return "1"


def br(x, y):
    global ar
    global ac
    global pc
    global dr
    global car
    global ad
    global sbr

    f = cd(y)

    if x == "00":
        if f == "0":
            car = car+1
        elif f == "1":
            car = ad
    elif x == "01":
        if f == "0":
            car = car+1
        elif f == "1":
            sbr = car+1
            car = ad
    elif x == "10":
        car = sbr
    elif x == "11":
        praccar = prac(car)
        praccar = addressmapper(dr)
        temp = strtobin(praccar)
        car = bintodec(temp)

def fetch(e):
    global ar
    global ac
    global pc
    global dr
    global car
    global ad
    global sbr
    global opbin

    print("FETCH CYCLE:")
    print("==========================================================")

    cm[64] = "11000000000001000001"
    cm[65] = "00010010100001000010"
    if e == "0000":
        cm[66] = "10100000000110000000"
    if e == "0001":
        cm[66] = "10100000000110000100"
    if e == "0010":
        cm[66] = "10100000000110001000"
    if e == "0011":
        cm[66] = "10100000000110001100"

    for i in range(64, 67):
        temp = cm[i]
        print("Microinstruction: ",temp)
        print("==========================================================")
        o = temp[0:3]
        t = temp[3:6]
        th = temp[6:9]
        c = temp[9:11]
        b = temp[11:13]
        add = temp[13:20]
        ad = bintodec(add)
        f1(o, pc-1)
        f2(t)
        f3(th)
        br(b, c)
        print("Value of registers: ")
        print("CAR:", car)
        print("PC:", pc)
        print("AR:", ar)
        print("DR:", dr)
        print("AC:", ac)
        print("SBR:", sbr)
        print("==========================================================")

    print("Fetch Cycle completed!")
    print("==========================================================")
    
"""
def indirect():
    cm[67] = "00010000000001000100"
    if opbin == "0000":
        cm[68] = "10100000000100000000"
    elif opbin == "0001":
        cm[68] = "10100000000100000100"
    elif opbin == "0010":
        cm[68] = "10100000000100001000"
    elif opbin == "0011":
        cm[68] = "10100000000100001100"

    for i in range(67, 69):
        temp = cm[i]
        o = temp[0:3]
        t = temp[3:6]
        th = temp[6:9]
        c = temp[9:11]
        b = temp[11:13]
        add = temp[13:20]
        ad = bintodec(add)
        f1(o, pc)
        f2(t)
        f3(th)
        br(b, c)
"""

def inexecute(e,s):
    global ar
    global ac
    global pc
    global dr
    global car
    global ad
    global sbr
    global opbin
    global modebit
    global opstr

    print("ADDRESS COMPUTATION and EXECUTE CYCLE:")
    print("==========================================================")

    cm[0] = "00000000001011000011"
    cm[1] = "00010000000000000010"
    cm[2] = "00100000000001000000"
    cm[3] = "00000000000001000000"
    cm[4] = "00000000010000000110"
    cm[5] = "00000000000001000000"
    cm[6] = "00000000001011000011"
    cm[7] = "00000010000001000000"
    cm[8] = "00000000001011000011"
    cm[9] = "00010100000000001010"
    cm[10] = "11100000000001000000"
    cm[11] = "00000000000001000000"
    cm[12] = "00000000001011000011"
    cm[13] = "00100000000000001110"
    cm[14] = "10010100000000001111"
    cm[15] = "11100000000001000000"

    cm[67] = "00010000000001000100"
    if e == "0000":
        print("ADD")
        print("==========================================================")
        cm[68] = "10100000000100000000"
    elif e == "0001":
        print("BRN")
        print("==========================================================")
        cm[68] = "10100000000100000100"
    elif e == "0010":
        print("STR")
        print("==========================================================")
        cm[68] = "10100000000100001000"
    elif e == "0011":
        print("EXC")
        print("==========================================================")
        cm[68] = "10100000000100001100"

    if s == "0":
        for i in range(4):
            temp = cm[car]
            print("Microinstruction: ",temp)
            print("==========================================================")
            o = temp[0:3]
            t = temp[3:6]
            th = temp[6:9]
            c = temp[9:11]
            b = temp[11:13]
            add = temp[13:20]
            ad = bintodec(add)
            f1(o, pc-1)
            f2(t)
            f3(th)
            br(b, c)
            print("Value of registers: ")
            print("CAR:", car)
            print("PC:", pc)
            print("AR:", ar)
            print("DR:", dr)
            print("AC:", ac)
            print("SBR:", sbr)
            print("==========================================================")

    if s == "1":
        for i in range(6):
            temp = cm[car]
            print("Microinstruction: ",temp)
            print("==========================================================")
            o = temp[0:3]
            t = temp[3:6]
            th = temp[6:9]
            c = temp[9:11]
            b = temp[11:13]
            add = temp[13:20]
            ad = bintodec(add)
            f1(o, pc-1)
            f2(t)
            f3(th)
            br(b, c)
            print("Value of registers: ")
            print("CAR:", car)
            print("PC:", pc)
            print("AR:", ar)
            print("DR:", dr)
            print("AC:", ac)
            print("SBR:", sbr)
            print("==========================================================")

    print("Address Computation and Execute Cycle completed!")
    print("==========================================================")

o=0
with open("input.txt", "r") as q:
    for k in q:
       o += 1


for i in range(o):
    print("==========================================================")
    print("Machine Language Instruction: ",mm[i])
    print("==========================================================")
    d = mm[pc]
    e = d[1:5]
    s = d[0]
    fetch(e)
    inexecute(e,s)

print("==========================================================")
print("Main Memory")
print("==========================================================")
print("Index: ",132," Value: ",mm[132])
print("Index: ",199," Value: ",prac(mm[199]))