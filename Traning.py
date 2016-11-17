import math

seed = 4
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
data=[[0,0,1],
      [0,1,1],
      [1,0,1],
      [1,1,1]]

# Desired output
output=[[0],
        [1],
        [1],
        [0]]

# inputs , (hidden layers,), output
layers = [ len(data[0]), 4, 2, len(output[0]) ]

ll = []
for i in range(len(layers)-1):
    ll.append( shuffle(layers[i+1], layers[i]) )

con1 = ll[0]
con2 = ll[1]
con3 = ll[2]

errList=[]
for i in range(len(data)):
    errList.append([])
    for j in range(len(output[0])):
        errList[i].append(100)

count=0
for j in range(60000):
    # Random position for the traning data
    rData = count % len(data)
    count += 1
    
    # Get the values of the layers
    l1 = dot( con1, data[rData] )
    l2 = dot( con2, l1 )
    l3 = dot( con3, l2 )
    
    l3_err = sub( output[rData], l3 )
    l3_delta = mulD( l3_err, l3 )
    
    l2_err = mul( l3_delta, con3 )
    l2_delta = mulD( l2_err, l2 )
    
    l1_err = mul( l2_delta, con2 )
    l1_delta = mulD( l1_err, l1 )
    
    con3 = adj( con3, l3_delta, l2 )
    con2 = adj( con2, l2_delta, l1 )
    con1 = adj( con1, l1_delta, data[rData] )
    
    for i in range(len(output[0])):
        if abs(int(l3_err[i]*100)) < errList[rData][i]:
            errList[rData][i] = abs(int(l3_err[i]*100))
    if j%10000==0:
        t=0
        for i in errList:
            for k in i:
                t += k
        print("Error:", t/(len(errList)*len(errList[0])), "%")
print("-"*10)
print("result after train:")
for i in data:
    l1 = dot(con1, i)
    l2 = dot(con2, l1)
    l3 = dot(con3, l2)
    for j in l3:
        print("{:.3f}".format(j),end="  ")
    print()
if True and False:
    print("The brain data:")
    print("con1 =", con1)
    print("con2 =", con2)
    print("con3 =", con3)