from Calisan import Calisan


class Veteriner(Calisan):
    def __init__(self, ad, soyad, yas, uzmanlik_alani, maas):
        super().__init__(ad, soyad, yas, "Veteriner", maas)
        self.uzmanlik_alani = uzmanlik_alani

    def __str__(self):
        return (
            super().__str__()
            + f", Maaş: {self.maas}, Uzmanlık Alanı: {self.uzmanlik_alani}"
        )

    def maas_hesapla(self):
        print(super().maas_hesapla("Veteriner"))

    def hayvanlari_muayene_et(self):
        print(f"{self.ad} hayvanları muayene ediyor.")

    def calis(self):
        print(f"{self.ad} {self.pozisyon} olarak çalışıyor.")

    def bilgileri_goster(self):
        print(
            f"Ad: {self.ad}, Soyad: {self.soyad}, Yaş: {self.yas}, Pozisyon: {self.pozisyon}, Uzmanlık Alanı: {self.uzmanlik_alani}"
        )
