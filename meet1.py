import random

class Ular:
    def __init__(self, panjang):
        self.panjang = panjang

    def gerak(self):
        if random.randint(0, 1):
            self.panjang += 1
        else:
            self.panjang -= 1

    def tampil(self):
        print(f"Panjang ular: {self.panjang}")

class Player:
    def __init__(self, nama):
        self.nama = nama
        self.skor = 0

    def tambah_skor(self):
        self.skor += 1

    def tampil(self):
        print(f"Nama: {self.nama}, Skor: {self.skor}")

def main():
    ular = Ular(5)
    player = Player("Player")

    while True:
        ular.tampil()
        player.tampil()
        print("1. Gerak ular")
        print("2. Keluar")
        pilihan = input("Pilih: ")

        if pilihan == "1":
            ular.gerak()
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid")

    print(f"Game selesai. Skor akhir: {player.skor}")

if __name__ == "__main__":
    main()