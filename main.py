#input fed thru command line
import random
lol = [1,2,3]
f = open("out.txt", "w")
D,I,S,V,F =  [int(x) for x in input().split()]
edges = []
endpoints = []
for i in range(S):
    x,y,z,r = input().split()
    edges.append([int(y),z])
    endpoints.append(int(y))
endpoints = list(set(endpoints))
k = []
for i in range(V):
    l = list(input().split())
    l = l[1:]
    k.append(l)
f.write(str(len(endpoints)))
f.write("\n")
for i in range(len(endpoints)):
    f.write(str(endpoints[i])+"\n")
    c = 0
    for j in edges:
        if(j[0] == endpoints[i]):
            c=c+ 1
    f.write(str(c)+"\n")
    for j in edges:
        if(j[0] == endpoints[i]):
            f.write(j[1]+" "+str(random.choice(lol))+"\n")
