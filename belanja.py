belanja=int(input('total belanja Rp. '))
if belanja > 50000:
    print('selamat anda mendapatkan diskon 5%')

    diskon = belanja * 5/100
    bayar = belanja - diskon

    print('total belanja anda, Rp. ', belanja)
    print('potongan harga, Rp. ', diskon)
    print('anda cukup bayar, Rp. ',bayar)
    print('Terimakasih sudah berbelanja')