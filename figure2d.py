from math import *


class Segitiga :
    jumlah_sisi = 3


class Samasisi(Segitiga):
    # child class Segitiga
    def __init__(self, sisi, tinggi):
        self.sisi = sisi
        self.tinggi = tinggi

    def hitung_luas(self):
        return self.sisi * self.tinggi * 0.5

    def hitung_keliling(self):
        return self.sisi * 3


class Samakaki(Segitiga):
    # child class Segitiga
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

    def hitung_keliling(self):
        return (2 * (sqrt((0.5*self.alas) ** 2 + self.tinggi ** 2))) + self.alas


class Segiempat :
    jumlah_sisi = 4


class Persegi(Segiempat):
    # child class Segiempat
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return (2*self.panjang) + (2*self.lebar)


class Trapesium(Segiempat):
    # child class Segiempat
    def __init__(self,alas, tutup, tinggi):
        self.alas = alas
        self.tutup = tutup
        self.tinggi = tinggi

    def hitung_luas(self):
        return (self.alas + self.tutup) * self.tinggi * 0.5

    def hitung_keliling(self):
        return self.alas + self.tutup + self.tinggi + sqrt((self.alas - self. tutup)**2 + self.tinggi**2)


class Jajargenjang(Segiempat):
    # child class Segiempat
    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return self.alas * self.tinggi

    def hitung_keliling(self):
        return 2*(self.alas + (self.tinggi / sin(45)))
