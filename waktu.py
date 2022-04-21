lama_pinjam=int(input('Pinjam buku berapa hari? : '))

if lama_pinjam >=3:
    print('Meminjam buku selama {} dikenakan biaya 1000/hari'.format(lama_pinjam))
else:
    print('Meminjam buku selama {} hari, GRATIS..'.format(lama_pinjam))
    