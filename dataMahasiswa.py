
class Mahasiswa:
    # Constructor
    def __init__(self, nama, nim, jurusan, semester, nilai):
        self.__nama = nama
        self.__nim = nim
        self.__jurusan = jurusan
        self.__semester = semester
        self.__nilai = nilai

    # Property dan Setter
    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, nama):
        if nama.strip():
            self.__nama = nama
        else:
            raise ValueError("Nama tidak boleh kosong!")

    @property
    def nim(self):
        return self.__nim

    @property
    def jurusan(self):
        return self.__jurusan

    @property
    def semester(self):
        return self.__semester

    @property
    def nilai(self):
        return self.__nilai

    @nilai.setter
    def nilai(self, nilai):
        if 0 <= nilai <= 100:
            self.__nilai = nilai
        else:
            raise ValueError("Nilai harus 0-100!")

    # Method
    def tampilkan_data(self):
        print(f"NIM      : {self.nim}")
        print(f"Nama     : {self.nama}")
        print(f"Jurusan  : {self.jurusan}")
        print(f"Semester : {self.semester}")
        print(f"Nilai    : {self.nilai}")
        print("-" * 35)

    # Static Method
    @staticmethod
    def tentukan_predikat(nilai):
        if nilai >= 85:
            return "A"
        elif nilai >= 75:
            return "B"
        elif nilai >= 65:
            return "C"
        elif nilai >= 50:
            return "D"
        else:
            return "E"

    # Class Method
    @classmethod
    def buat_mahasiswa_baru(cls, nama, nim, jurusan):
        return cls(nama, nim, jurusan, 1, 0)


class SistemMahasiswa:
    # Constructor
    def __init__(self):
        self.__daftar_mahasiswa = []

    # Menambahkan mahasiswa
    def tambah_mahasiswa(self, mahasiswa):
        if self.cari_mahasiswa(mahasiswa.nim):
            print("NIM sudah terdaftar!")
            return

        self.__daftar_mahasiswa.append(mahasiswa)
        print("Data mahasiswa berhasil ditambahkan!")

    # Menampilkan seluruh mahasiswa
    def tampilkan_semua(self):
        if not self.__daftar_mahasiswa:
            print("Belum ada data mahasiswa.")
            return

        print("\n=== DAFTAR DATA MAHASISWA ===")
        for mahasiswa in self.__daftar_mahasiswa:
            mahasiswa.tampilkan_data()
            print("Predikat :", Mahasiswa.tentukan_predikat(
                mahasiswa.nilai
            ))

    # Mencari mahasiswa
    def cari_mahasiswa(self, nim):
        for mahasiswa in self.__daftar_mahasiswa:
            if mahasiswa.nim == nim:
                return mahasiswa
        return None

    # Mengubah data mahasiswa
    def ubah_mahasiswa(self, nim):
        mahasiswa = self.cari_mahasiswa(nim)

        if mahasiswa:
            try:
                nama = input("Masukkan nama baru: ")
                nilai = float(input("Masukkan nilai baru: "))

                mahasiswa.nama = nama
                mahasiswa.nilai = nilai

                print("Data berhasil diperbarui!")
            except ValueError as error:
                print("Gagal mengubah data:", error)
        else:
            print("Mahasiswa tidak ditemukan!")

    # Menghapus mahasiswa
    def hapus_mahasiswa(self, nim):
        mahasiswa = self.cari_mahasiswa(nim)

        if mahasiswa:
            self.__daftar_mahasiswa.remove(mahasiswa)
            print("Data mahasiswa berhasil dihapus!")
        else:
            print("Mahasiswa tidak ditemukan!")

    # Class Method untuk statistik
    @classmethod
    def nama_sistem(cls):
        return "SISTEM INFORMASI DATA MAHASISWA"

    def jumlah_mahasiswa(self):
        return len(self.__daftar_mahasiswa)


# Membuat object
sistem = SistemMahasiswa()

# Data awal
mhs1 = Mahasiswa("Karim", "23001", "Informatika", 3, 90)
mhs2 = Mahasiswa("Andi", "23002", "Sistem Informasi", 2, 80)

sistem.tambah_mahasiswa(mhs1)
sistem.tambah_mahasiswa(mhs2)


# Menu utama
while True:
    print("\n===================================")
    print(SistemMahasiswa.nama_sistem())
    print("===================================")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Data Mahasiswa")
    print("3. Cari Mahasiswa")
    print("4. Ubah Data Mahasiswa")
    print("5. Hapus Data Mahasiswa")
    print("6. Jumlah Mahasiswa")
    print("7. Keluar")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        nama = input("Nama: ")
        nim = input("NIM: ")
        jurusan = input("Jurusan: ")

        try:
            semester = int(input("Semester: "))
            nilai = float(input("Nilai: "))

            if semester < 1 or not 0 <= nilai <= 100:
                print("Semester atau nilai tidak valid!")
            else:
                mahasiswa = Mahasiswa(
                    nama, nim, jurusan, semester, nilai
                )
                sistem.tambah_mahasiswa(mahasiswa)
        except ValueError:
            print("Input semester atau nilai harus berupa angka!")

    elif pilihan == "2":
        sistem.tampilkan_semua()

    elif pilihan == "3":
        nim = input("Masukkan NIM yang dicari: ")
        mahasiswa = sistem.cari_mahasiswa(nim)

        if mahasiswa:
            print("\nData ditemukan:")
            mahasiswa.tampilkan_data()
        else:
            print("Mahasiswa tidak ditemukan!")

    elif pilihan == "4":
        nim = input("Masukkan NIM: ")
        sistem.ubah_mahasiswa(nim)

    elif pilihan == "5":
        nim = input("Masukkan NIM yang akan dihapus: ")
        sistem.hapus_mahasiswa(nim)

    elif pilihan == "6":
        print("Jumlah mahasiswa:",
              sistem.jumlah_mahasiswa())

    elif pilihan == "7":
        print("Terima kasih telah menggunakan program!")
        break

    else:
        print("Pilihan tidak valid!")
