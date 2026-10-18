f1 =open('demo.txt', 'r')
onom = []
therm = []
pl = 1
for line in f1:
    if pl%2 == 1:
        onom.append(line)
    else:
        therm.append(float(line))
    pl +=1
f1.close()
mo = 0.0
for item in therm:
    mo += item
mo = mo/len(therm)
print 'mesos oros thermokrasias einai: ', mo
N = len(therm)
for i in range(1,N,1):
    for j in range(N-1,i-1,N-1):
        if therm[j]< therm[j-1]:
            therm[j],therm[j-1] = therm[j-1],therm[j]
            onom[j],onom[j-1] = onom[j-1],onom[j]
