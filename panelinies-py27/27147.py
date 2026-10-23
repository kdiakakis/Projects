def charge(xronos,mel):
    if mel == 'NAI':
        if xronos<=120:
            xreosi = xronos * 0.03
        else:
            xreosi = 120 * 0.03 + (xronos-120)*0.01
    else:
        if xronos<=120:
            xreosi = xronos * 0.06
        else:
            xreosi = 120 * 0.06 + (xronos - 120)*0.04
    return xreosi

esoda = 0
oxi = []
xronos = input('xronos: ')
while xronos > 0:
    melos = raw_input('eisai melos («NAI» ή «OXI    »)?: ')
    xreosi = charge(xronos,melos)
    print 'i xreosi tou pelati einai: ',xreosi
    if melos == 'NAI':
        esoda +=xreosi
    else:
        oxi.append(xreosi)
    xronos = input('xronos: ')
for i in range (len(oxi)):
    for j in range (len(oxi)-1, 0, -1):
        if oxi[j]>oxi[j-1]:
            oxi[j], oxi[j-1] = oxi[j-1], oxi[j]
print 'ta esoda tou Internet Cafe apo pelates meloi einai: ', esoda
print 'ta esoda tou Internet Cafe apo pelates pou den einai meloi einai: ', oxi
