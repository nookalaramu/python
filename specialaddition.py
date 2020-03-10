#if a,b,c,d are positive integers with a sum of 63, what is the max value of ab+bc+cd

#4b5dgthjguojiimport random
a=0
b=0
c=0
d=0
list1=[]
aa=0
bb=0
cc=0
dd=0
for a in range(1,64):
    for b in range(1,64):
        for c in range(1,64):
            for d in range(1,64):
                #xsum= a+b+c+d
                #xmax= (a*b)+(b*c)+(c*d)
                #print("x1=: ", xsum, "x2= : ", xmax)
                #if (a+b+c+d==63) and ((a*b)+(b*c)+(c*d)>max):
                if (a+b+c+d==63):
                    list1.append((a*b)+(b*c)+(c*d))
                    # aa=a
                    # bb=b
                    # cc=c
                    # dd=d 
                #max = (a*b)+(b*c)+(c*d)
maxvalue = max(list1)
print(aa,bb,cc,dd,maxvalue)
for e in range(1,64):
    for f in range(1,64):
        for g in range(1,64):
            for h in range(1,64):
                if ((e*f)+(f*g)+(g*h)==max(list1)):
                    aa=e
                    bb=f
                    cc=g
                    dd=h
                    break
print(aa,bb,cc,dd)
                    