import math

class Kubus:
    jumlah_sisi = 6
    
    def __init__(self, sisi):
        self.sisi = sisi
        
    def hitung_luas(self) :
        # luas permukaan kubus
        return jumlah_sisi*(self.sisi**2)
    
    def hitung_volume(self) :
        return self.sisi**3
        
class Balok:
    jumlah_sisi = 6
    
    def __init__(self, panjang, tinggi, lebar):
        self.panjang = panjang
        self.tinggi = tinggi
        self.lebar = lebar
        
    def hitung_luas(self) :
        # luas permukaan balok
        return 2*((self.panjang*self.lebar)+(self.panjang*self.tinggi)+(self.lebar*self.tinggi))
    
    def hitung_volume(self) :
        return self.panjang*self.lebar*self.tinggi
        
class Tabung:
    jumlah_sisi = 3
    
    def __init__(self, radius, tinggi):
        self.radius = radius
        self.tinggi = tinggi
        
    def hitung_luas(self) :
        # luas permukaan tabung = luas selimut + 2*luas alas
        return (2*math.pi*self.radius*self.tinggi)+ 2*(math.pi*(self.radius**2))
    
    def hitung_volume(self) :
        return math.pi*self.radius*self.tinggi
        
class Kerucut:
    jumlah_sisi = 2
    
    def __init__(self, radius, tinggi):
        self.radius = radius
        self.tinggi = tinggi
        
    def hitung_luas(self) :
        # luas permukaan kerucut 
        garis_pelukis = math.sqrt((self.radius**2)+(self.tinggi**2))
        return math.pi*self.radius*(self.radius+garis_pelukis)
        
    def hitung_volume(self) :
        return 1/3*self.radius*math.pi*self.tinggi
    
