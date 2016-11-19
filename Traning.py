import math

seed = 1
def rand(x):
    global seed
    seed *= 17373172882
    seed %= 64251
    return seed%x

# Returns a number between 0 and 1
def segm(x):
    return 1/(1+math.exp(-x))
def der(x):
    return x*(1-x)

# Return a 2 dimentional list with random values
def shuffle(nodes, inputs):
    t=[]
    for i in range(nodes):
        t.append([])
        for j in range(inputs):
            t[i].append((rand(200)/100)-1)
    return t

# multiply two matrices [hor].[ver]
def dot(m1, m2):
    m3=[]
    for j in range(len(m1)):
        nrx=0
        for i in range(len(m2)):
            nrx += m1[j][i]*m2[i]
        m3.append(segm(nrx))
    return m3

def mul(a,b):
    c=[]
    for i in range(len(b[0])):
        c.append(0)
        for j in range(len(a)):
            c[i] += a[j]*b[j][i]
    return c
def sub(a,b):
    c=[]
    for i in range(len(a)):
        c.append( a[i] - b[i] )
    return c

def mulD(a,b):
    c=[]
    for i in range(len(a)):
        c.append( a[i] * der(b[i]) )
    return c

def adj(a,b,c):
    for i in range(len(b)):
        for k in range(len(c)):
            a[i][k] += b[i] * c[k]
    return a

# Traning data
data=[[0,0,0],
      [0,0,1],
      [0,1,0],
      [1,0,0],
      [0,1,1],
      [1,0,1],
      [1,1,0],
      [1,1,1]]

# Desired output
output=[[0,0],
        [0,1],
        [0,1],
        [0,1],
        [1,0],
        [1,0],
        [1,0],
        [1,1]]

# inputs , (hidden layers,), output
layers = [ len(data[0]), 3, 3, len(output[0]) ]

lenLayer = len(layers)-1

cl = []
for i in range(lenLayer):
    cl.append( shuffle(layers[i+1], layers[i]) )

errList=[]
for i in range(len(data)):
    errList.append([])
    for j in range(len(output[0])):
        errList[i].append(100)

count=0
for j in range(100000):
    # Random position for the traning data
    rData = count % len(data)
    count += 1
    
    # Calculating layer by layer
    ll = []
    for i in range(lenLayer):
        if(i==0):
            ll.append( dot(cl[0], data[rData]) )
        else:
            ll.append( dot(cl[i], ll[i-1]) )
    
    erl = [] # error list
    dll = [] # delta list
    for i in range(lenLayer):
        if i==0:
            erl.append( sub(output[rData], ll[lenLayer-i-1]) )
        else:
            erl.append( mul(dll[i-1], cl[lenLayer-i]) )
        dll.append( mulD(erl[i], ll[lenLayer-i-1]) )
    
    l1_err = erl[2]
    l1_delta = dll[2]
    
    for i in range(lenLayer):
        if i!=lenLayer-1:
            cl[lenLayer-i-1] = adj( cl[lenLayer-i-1], dll[i], ll[lenLayer-i-1] )
        else:
            cl[lenLayer-i-1] = adj( cl[lenLayer-i-1], dll[i],data[rData] )
    
    for i in range(len(output[0])):
        if abs(int(erl[0][i]*100)) < errList[rData][i]:
            errList[rData][i] = abs(int(erl[0][i]*100))
    if j%10000==0:
        t=0
        for i in errList:
            for k in i:
                t += k
        print("Error:", t/(len(errList)*len(errList[0])), "%")

print("-"*10)
print("result after train:")
for i in data:
    ll = []
    for i in range(lenLayer):
        if(i==0):
            ll.append( dot(cl[0], data[rData]) )
        else:
            ll.append( dot(cl[i], ll[i-1]) )
    
    for j in ll[len(ll)-1]:
        print("{:.0f}".format(j),end="  ")
    print()
if True:
    print("The brain data:")
    for i in range(len(cl)):
        print("con"+str(i+1)+" =", cl[i])


