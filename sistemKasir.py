
class Produk:
    def __init__(self, nama, harga, stok):
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok

    # Property
    @property
    def nama(self):
        return self.__nama

    @property
    def harga(self):
        return self.__harga

    @property
    def stok(self):
        return self.__stok

    # Setter
    @stok.setter
    def stok(self, jumlah):
        if jumlah >= 0:
            self.__stok = jumlah
        else:
            raise ValueError("Stok tidak boleh negatif!")

    # Method
    def tampilkan_produk(self):
        print(f"{self.nama:<15} Rp{self.harga:>8,} | Stok: {self.stok}")

    # Static Method
    @staticmethod
    def format_rupiah(nominal):
        return f"Rp{nominal:,}"


class SistemKasir:
    # Class Attribute
    nama_toko = "TOKO MAJU JAYA"

    def __init__(self):
        self.__daftar_produk = []
        self.__keranjang = []

    # Class Method
    @classmethod
    def informasi_toko(cls):
        return f"Selamat Datang di {cls.nama_toko}"

    # Menambahkan produk
    def tambah_produk(self, produk):
        self.__daftar_produk.append(produk)

    # Menampilkan produk
    def tampilkan_produk(self):
        print("\n=== DAFTAR PRODUK ===")
        for i, produk in enumerate(self.__daftar_produk, 1):
            print(f"{i}. ", end="")
            produk.tampilkan_produk()

    # Membeli produk
    def beli_produk(self, nomor, jumlah):
        if nomor < 1 or nomor > len(self.__daftar_produk):
            print("Nomor produk tidak tersedia!")
            return

        produk = self.__daftar_produk[nomor - 1]

        if jumlah <= 0:
            print("Jumlah pembelian harus lebih dari 0!")
            return

        if jumlah > produk.stok:
            print("Stok produk tidak mencukupi!")
            return

        self.__keranjang.append({
            "produk": produk,
            "jumlah": jumlah
        })

        produk.stok -= jumlah
        print("Produk berhasil ditambahkan ke keranjang!")

    # Menghitung total belanja
    def hitung_total(self):
        total = 0

        for item in self.__keranjang:
            total += item["produk"].harga * item["jumlah"]

        return total

    # Menampilkan keranjang
    def tampilkan_keranjang(self):
        print("\n=== KERANJANG BELANJA ===")

        if not self.__keranjang:
            print("Keranjang masih kosong!")
            return

        for item in self.__keranjang:
            produk = item["produk"]
            jumlah = item["jumlah"]
            subtotal = produk.harga * jumlah

            print(f"{produk.nama} x{jumlah} = "
                  f"{Produk.format_rupiah(subtotal)}")

        print("-" * 35)
        print("Total:", Produk.format_rupiah(self.hitung_total()))

    # Pembayaran
    def pembayaran(self, uang):
        total = self.hitung_total()

        if total == 0:
            print("Keranjang masih kosong!")
            return

        if uang < total:
            print("Uang pembayaran tidak mencukupi!")
            return

        kembalian = uang - total

        self.cetak_struk(uang, kembalian)

        self.__keranjang.clear()

    # Mencetak struk
    def cetak_struk(self, uang, kembalian):
        print("\n========== STRUK BELANJA ==========")
        print(self.nama_toko)

        for item in self.__keranjang:
            produk = item["produk"]
            jumlah = item["jumlah"]
            subtotal = produk.harga * jumlah

            print(f"{produk.nama} x{jumlah}")
            print(Produk.format_rupiah(subtotal))

        total = self.hitung_total()

        print("-----------------------------------")
        print("Total     :", Produk.format_rupiah(total))
        print("Bayar     :", Produk.format_rupiah(uang))
        print("Kembalian :", Produk.format_rupiah(kembalian))
        print("===================================")
        print("Terima kasih telah berbelanja!")


# Membuat object sistem kasir
kasir = SistemKasir()

# Membuat object produk
kasir.tambah_produk(Produk("Beras", 15000, 20))
kasir.tambah_produk(Produk("Minyak", 18000, 15))
kasir.tambah_produk(Produk("Gula", 14000, 10))
kasir.tambah_produk(Produk("Mie Instan", 3500, 50))
kasir.tambah_produk(Produk("Telur", 28000, 10))


# Menu utama
while True:
    print("\n===================================")
    print(SistemKasir.informasi_toko())
    print("===================================")
    print("1. Lihat Daftar Produk")
    print("2. Beli Produk")
    print("3. Lihat Keranjang")
    print("4. Pembayaran")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        kasir.tampilkan_produk()

    elif pilihan == "2":
        kasir.tampilkan_produk()

        try:
            nomor = int(input("Pilih nomor produk: "))
            jumlah = int(input("Masukkan jumlah: "))

            kasir.beli_produk(nomor, jumlah)
        except ValueError:
            print("Masukkan angka yang valid!")

    elif pilihan == "3":
        kasir.tampilkan_keranjang()

    elif pilihan == "4":
        kasir.tampilkan_keranjang()

        try:
            uang = int(input("Masukkan uang pembayaran: "))
            kasir.pembayaran(uang)
        except ValueError:
            print("Pembayaran harus berupa angka!")

    elif pilihan == "5":
        print("Terima kasih telah menggunakan sistem kasir!")
        break

    else:
        print("Pilihan tidak valid!")
