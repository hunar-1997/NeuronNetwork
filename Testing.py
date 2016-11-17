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
con1 = [[4.708883241745764, 6.0128386218865177], [-0.60197559316918603, 0.82677117396092559], [-8.956112447827973, 4.6175083169722964]]
con2 = [[4.4546012527085974, -7.2395475102008779, -5.7966371932967569], [-4.4145631663192093, 11.097125812070765, -6.8683132455555116], [5.138170011516471, -2.3710836339320807, -0.93006481318575185]]
con3 = [[8.4658533797369344, -18.112125634996591, 5.1313562618864186]]

while True:
    data = []
    for i in range(len(con1[0])):
        data.append(float(input("Input: ")))
    
    # Get the values of layer 1 and 2
    l1 = dot(con1, data)
    l2 = dot(con2, l1)
    l3 = dot(con3, l2)
    for i in range(len(l3)):
        print("Output:", "{:.0f}".format(l3[i]))
    print("-"*10)