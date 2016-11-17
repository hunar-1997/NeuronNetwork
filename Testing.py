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
con1 = [[-8.6531641190272239, 4.0658035727646764], [4.0705008919347341, -8.6644709907493738], [0.20959374278758772, 0.20887653240681181], [-5.8441846660663934, -5.8498152321397106]]
con2 = [[8.8108798524350984, 8.8117737505755542, -7.591598944170463, -18.546334157519723]]

while True:
    data = []
    for i in range(len(con1[0])):
        data.append(float(input("Input: ")))
    
    # Get the values of layer 1 and 2
    l1 = dot(con1, data)
    l2 = dot(con2, l1)
    for i in range(len(l2)):
        print("Output:", "{:.0f}".format(l2[i]), end="   ")
    print()
    print("-"*10)