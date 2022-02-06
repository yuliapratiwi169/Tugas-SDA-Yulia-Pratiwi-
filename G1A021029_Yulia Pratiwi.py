def pertama():
  print("=======================================")
  print("SELAMAT DATANG DI LION AIR TIKET")
  print("=======================================")
  
  def welcome():
    print("\nApakah Anda Ingin Melakukan Pemesanan Tiket ? ")
    print("1.Ya" "\n2.Tidak")
    awal = input("Pilihan : ")
    if awal=="1" :
      print("Selamat Datang di Menu Pemesanan Tiket Pesawat Lion Air  ")
    elif awal=="2":
      print("Transaksi Anda dibatalkan")
      quit()
    else:
      print("input yang anda masukkan salah")
      welcome()
  welcome()
  
  print('')
  Nama=input("Silahkan Masukkan Nama Lengkap Anda : ") 
  Kontak=int(input("Masukkan No HP/WA Anda : "))
 
  
  print("\nRUTE Lion Air")
  Rute_Pesawat=["1.Bengkulu-Jakarta","2.Bengkulu-Bali\n"]
  for menu1 in Rute_Pesawat:
    print(menu1,end="\n")

  def rute():
    Rute=int(input("Masukkan Angka  Berdasarkan Rute yang Anda Inginkan : "))
    if Rute==1:
      print('')
      print("Anda Memilih Kereta dengan Tujuan Bengkulu-Jakarta")
    elif Rute==2:
      print('')
      print("Anda Memilih Kereta dengan Tujuan Bengkulu-Bali")
    else:
      print('')
      print("input yang anda masukkan salah")
      rute()
  rute()
  
  print('')
  print("Tiket Pesawat Berdasarkan Kelas:")
  Kelas=["1.VIP","2.EKONOMI","3.BISNIS"]
  for menu2 in Kelas:
    print(menu2,end="\n")

  def kelas():
    Pilihan_Kelas=int(input("Silahkan Memasukkan Angka Berdasarkan Kelas yang anda pilih : "))
    if Pilihan_Kelas==1:
      print("=============================")
      print("Selamat Datang di Kelas VIP")
      print("Harga tiket Rp.3.000.000,00")
      Harga = 3000000
      penumpang = int(input("Masukkan Jumlah Penumpang : "))
      Total_Harga = (Harga*penumpang)
      print("Total harga yang harus dibayar : Rp.",Total_Harga,)
      print("=============================")
    elif Pilihan_Kelas==2:
      print("===============================")
      print("Selamat Datang di Kelas EKONOMI")
      print("Harga tiket Rp.1.500.000,00")
      Harga = 1500000
      penumpang = int(input("Masukkan Jumlah Penumpang : "))
      Total_Harga = (Harga*penumpang)
      print("Total harga yang harus dibayar : Rp.",Total_Harga,)
      print("===============================")
    elif Pilihan_Kelas==3:
      print("===============================")
      print("Selamat Datang di Kelas BISNIS")
      print("Harga tiket Rp.2.500.000,00")
      Harga = 2500000
      penumpang = int(input("Masukkan Jumlah Penumpang : "))
      Total_Harga = (Harga*penumpang)
      print("Total harga yang harus dibayar : Rp.",Total_Harga,)
      print("===============================")
    else:
      print("Input yang anda masukkan salah")
      kelas()
  kelas()

  print("======Metode Pembayaran======")
  Pembayaran=["1.Tunai \n2.Non Tunai"]
  for menu3 in Pembayaran:
    print(menu3,end="\n")

  def metode():
    Metode_Pembayaran=int(input("Masukkan Angka Berdasarkan Metode Pembayaran : "))
    if Metode_Pembayaran==1:
      print('')
      print("Silahkan Mengambil Struk dan Langsung Bayar Tiket Anda ke Loket Pembayaran")
      print('')
      print("====Terima Kasih Sudah Melakukan Pemesanan Tiket di Lion Air Tiket=====")

    elif Metode_Pembayaran==2:
      print('')
      print("Silahkan Menyelesaikan Pemesanan Tiket Anda,\nBayar Melalui NO.Rekening 76892034 a.n KAI EXPRESS")
      print('')
      print("=======Terima Kasih Telah Melakukan Pemesanan di Lion Air Tiket======")

    else:
      print("input yang anda masukkan salah")
      metode()
  metode()

  def last():
    print("")
    print("Apakah Anda Ingin Melakukan Pemesanan Lagi? ")
    print("1.Ya \n2.Tidak")
    Again =input("pilihan : ")
    if Again=="1":
      pertama()
    elif Again=="2":
      print("=======TERIMA KASIH TELAH MENGGUNAKAN LAYANAN LION AIR TIKET=======")
      quit()
    else:
      print("input yang anda masukkan salah")
      last()
  last()

pertama()