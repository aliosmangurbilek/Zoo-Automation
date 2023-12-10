from Calisan import Calisan


class Yonetici(Calisan):
    def __init__(self, ad, soyad, yas, sorumlu_oldugu_bolum, maas):
        super().__init__(ad, soyad, yas, "Yönetici", maas)
        self.sorumlu_oldugu_bolum = sorumlu_oldugu_bolum

    def __str__(self):
        return (
            super().__str__()
            + f", Maaş: {self.maas}, Sorumlu Olduğu Bölüm: {self.sorumlu_oldugu_bolum}"
        )

    def bolumu_yonet(self):
        print(f"{self.ad} {self.sorumlu_oldugu_bolum} bölümünü yönetiyor.")

    def calis(self):
        print(f"{self.ad} {self.pozisyon} olarak çalışıyor.yonetici")

    def maas_hesapla(self):
        print(self.pozisyon + " için maaş hesaplandı. yonetici")

    def bilgileri_goster(self):
        print(
            f"Ad: {self.ad}, Soyad: {self.soyad}, Yaş: {self.yas}, Pozisyon: {self.pozisyon}, Sorumlu Olduğu Bölüm: {self.sorumlu_oldugu_bolum}"
        )
