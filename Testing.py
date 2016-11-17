import math

# Returns a number between 0 and 1
def segm(x):
    return 1/(1+math.exp(-x))

# multiply two matrices [hor].[ver]
def dot(m1, m2):
    m3=[]
    for j in range(len(m1)):
        nrx=0
        for i in range(len(m2)):
            nrx += m1[j][i]*m2[i]
        m3.append(segm(nrx))
    return m3

# layer(nodes, inputs)
con1 = [[2.1, -5.4],
        [2.6, 4], 
        [-5.7, 1]]

con2 = [[-0.1, -5.2, 14.6],
        [13.5, -6.2, 1.7]]

while True:
    data = []
    for i in range(len(con1[0])):
        data.append(float(input("Input: ")))
    
    # Get the values of layer 1 and 2
    l1 = dot(con1, data)
    l2 = dot(con2, l1)
    for i in range(len(l2)):
        print("Output:", "{:.0f}".format(l2[i]))
    print("-"*10)