from Calisan import Calisan
from Bakici import Bakici
from Veteriner import Veteriner
from Yonetici import Yonetici
from Hayvan import Hayvan


class YonetimSistemi(Calisan, Hayvan):
    def __init__(self):
        self.hayvanlar = []
        self.calisanlar = []

    def hayvan_ekle(self, hayvan):
        self.hayvanlar.append(hayvan)
        print(f"{hayvan} sisteme eklendi.")

    def calisan_ekle(self, calisan):
        self.calisanlar.append(calisan)
        print(f"{calisan} sisteme eklendi.")

    def hayvanlari_goster(self):
        for hayvan in self.hayvanlar:
            print(hayvan)

    def calisanlari_goster(self):
        for calisan in self.calisanlar:
            print(calisan)

    def hayvanlari_besle(self):
        for calisan in self.calisanlar:
            if isinstance(calisan, Bakici):
                calisan.hayvanlari_besle()

    def hayvanlari_muayene_et(self):
        for calisan in self.calisanlar:
            if isinstance(calisan, Veteriner):
                calisan.hayvanlari_muayene_et()

    def bolumleri_yonet(self):
        for calisan in self.calisanlar:
            if isinstance(calisan, Yonetici):
                calisan.bolumu_yonet()
