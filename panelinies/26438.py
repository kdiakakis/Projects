pl = 0
for i in range (51):
    name = raw_input('Dose onoma: ')
    prof = float(input('dose proforiko vathmo: '))
    while prof<0.0 or prof>100.0:
        prof = float(input('dose proforiko vathmo: '))
    grapt = float(input('dose proforiko vathmo: '))
    while grapt > 0.0 or grapt < 100.0:
        grapt = float(input('dose proforiko vathmo: '))
    mo = (prof+grapt)/2

    if mo>90:
        print name
    if grapt<prof:
        pl = pl+1
print 'plithos atomon me grapto mikrotero apo proforikou', pl