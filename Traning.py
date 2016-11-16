import math

seed = 426
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

# Traning data
data=[[0,0],
      [0,1],
      [0.1,0.1],
      [0.1,0.2],
      [0.2,0.3],
      [0.5,0.1],
      [0.3,0.3],
      [0.8,0.1]]

# Desired output
output=[0,
        1,
        0.2,
        0.3,
        0.5,
        0.6,
        0.6,
        0.9]

# layer(nodes, inputs)
con1 = shuffle(20,2)
con2 = shuffle(1,20)

errList=[]
for i in range(len(data)):
    errList.append(100)

count=0
for j in range(50000):
    # Random position for the traning data
    rData = count % len(data)
    count += 1
    
    # Get the values of layer 1 and 2
    l1 = dot(con1, data[rData])
    l2 = dot(con2, l1)
    
    l2_err = output[rData] - l2[0]
    l2_delta = l2_err * der(l2[0])
    
    l1_err = []
    for i in range(len(con2[0])):
        l1_err.append( l2_delta*con2[0][i] )
    
    l1_delta = []
    for i in range(len(l1_err)):
        l1_delta.append( l1_err[i]*der(l1[i]) )
    
    for i in range(len(con2)):
        con2[0][i] += l1[i] * l2_delta
    
    for i in range(len(con1)):
        for k in range(len(con1[0])):
            con1[i][k] += data[rData][k] * l1_delta[i]
    
    if abs(int(l2_err*100)) < errList[rData]:
        errList[rData] = abs(int(l2_err*100))
    if j%1000==0:
        t=0
        for i in errList:
            t += i
        print("Error:", t/len(data), "%")
print("-"*10)
print("result after train:")
for i in data:
    l1 = dot(con1, i)
    l2 = dot(con2, l1)
    print("{:.1f}".format(l2[0]))

if True:
    print("The brain data:")
    print("con1 =",con1)
    print("con2 =", con2)