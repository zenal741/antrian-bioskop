from collections import deque

class BioskopQueue:
    def __init__(self):
        self.queue = deque()

    def antri(self, nama):
        self.queue.append(nama)
        print(f"{nama} telah masuk ke dalam antrian.")

    def layani(self):
        if self.queue:
            nama = self.queue.popleft()
            print(f"{nama} sedang dilayani.")
        else:
            print("Tidak ada antrian.")

    def tampilkan_antrian(self):
        if self.queue:
            print("Antrian saat ini:", list(self.queue))
        else:
            print("Antrian kosong.")

# Contoh penggunaan
bioskop = BioskopQueue()
bioskop.antri("Andi")
bioskop.antri("Budi")
bioskop.tampilkan_antrian()
bioskop.layani()
bioskop.tampilkan_antrian()
bioskop.layani()
bioskop.layani()
