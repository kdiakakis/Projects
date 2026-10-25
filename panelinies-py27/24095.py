onomata = []
mesos_oros = []


for i in range(200):
    name =raw_input('Onoma diagonizomenou: ')
    sum = 0
    for g in range(2):
        vathm = input('vathmologia: ')
        sum += float(vathm)
    mo = sum/2
    if mo > 7:
        onomata.append(name)
        mesos_oros.append(mo)
perasan = len(onomata)
print 'perasan ',perasan,'atoma stin epomeni fasi'

for i in range(perasan):
    for g in range(perasan -1,0,-1):
        if mesos_oros[g] > mesos_oros[g-1]:
            mesos_oros[g],mesos_oros[g-1] = mesos_oros[g-1],mesos_oros[g]
            onomata[g],onomata[g-1] = onomata[g-1],onomata[g]

print 'ta atoma pou perasan stin epomeni fasi einai:'
for i in range(perasan):
    print onomata[i],mesos_oros[i]