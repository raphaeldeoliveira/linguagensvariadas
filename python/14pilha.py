p1=[50, 40, 20, 30, 10]
p2=[]

def fb(p1, p2):
    print("ow michele {}".format(p1))
    if (len(p1)==0):
        return
    x=p1[len(p1)-1]
    del p1[len(p1)-1]
    fb(p1, p2)
    p2.append(x)

fb(p1, p2)
print(p2)