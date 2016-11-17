import math

seed = 7
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
data=[[0,0],
      [0,1],
      [1,0],
      [1,1]]

# Desired output
output=[[0,1],
        [1,1],
        [1,0],
        [0,0]]

# layer(nodes, inputs)
con1 = shuffle(4,2)
con2 = shuffle(2,4)

errList=[]
for i in range(len(data)):
    errList.append(100)

count=0
for j in range(100000):
    # Random position for the traning data
    rData = count % len(data)
    count += 1
    
    # Get the values of layer 1 and 2
    l1 = dot( con1, data[rData] )
    l2 = dot( con2, l1 )
    
    l2_err = sub( output[rData], l2 )
    l2_delta = mulD( l2_err, l2 )
    
    l1_err = mul( l2_delta, con2 )
    l1_delta = mulD( l1_err, l1 )
    
    con2 = adj( con2, l2_delta, l1 )
    con1 = adj( con1, l1_delta, data[rData] )
    
    if abs(int(l2_err*100)) < errList[rData]:
        errList[rData] = abs(int(l2_err*100))
    if j%10000==0:
        t=0
        for i in errList:
            t += i
        print("Error:", t/len(data), "%")
print("-"*10)
print("result after train:")
for i in data:
    l1 = dot(con1, i)
    l2 = dot(con2, l1)
    print("{:.0f}".format(l2[0]))

if True:
    print("The brain data:")
    print("con1 =",con1)
    print("con2 =", con2)