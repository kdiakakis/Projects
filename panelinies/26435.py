epid = 0
fort = 0
moto = 0
t_epid = 0
t_fort = 0
t_moto = 0
total_amax = 0
total_xrim = 0

typos_oxim = raw_input('τυπος οχήματος( «E» για Επιβατικό, «F» για Φορτηγό και «M» για Μοτοσυκλέτα) γιά τέλος «TELOS»: ')
while typos_oxim != 'E' and typos_oxim != 'F' and typos_oxim != 'M' and typos_oxim != 'TELOS':
    typos_oxim = raw_input('Μή έγκιρη τιμή, ξανα προσπαθήστε: ')
while typos_oxim != 'TELOS':
    if typos_oxim == 'E':
        epid += 1
        t_epid += 60
    elif typos_oxim == 'F':
        fort += 1
        t_fort += 80
    else:
        moto += 1
        t_moto += 40
    typos_oxim = raw_input('τυπος οχήματος( «E» για Επιβατικό, «F» για Φορτηγό και «M» για Μοτοσυκλέτα) γιά τέλος «TELOS»: ')
    while typos_oxim != 'E' and typos_oxim != 'F' and typos_oxim != 'M' and typos_oxim != 'TELOS':
        typos_oxim = raw_input('Μή έγκιρη τιμή, ξανα προσπαθήστε: ')
total_amax = epid + fort + moto
total_xrim = t_moto + t_epid + t_fort
print mpla mpla mpla