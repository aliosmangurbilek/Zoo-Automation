from Calisan import Calisan


class Bakici(Calisan):
    def __init__(self, ad, soyad, yas, bakilan_hayvan_turleri, maas):
        super().__init__(ad, soyad, yas, "Bakıcı", maas)
        self.bakilan_hayvan_turleri = bakilan_hayvan_turleri

    def __str__(self):
        return (
            super().__str__()
            + f", Maaş: {self.maas}, Bakılan Hayvan Türleri: {self.bakilan_hayvan_turleri}"
        )

    def hayvanlari_besle(self):
        print(f"{self.ad} hayvanları besliyor.")

    def hayvanlari_kontrol_et(self):
        print(f"{self.ad} hayvanları kontrol ediyor.")

    def calis(self):
        print(f"{self.ad} {self.pozisyon} olarak çalışıyor.")

    def bilgileri_goster(self):
        print(
            f"Ad: {self.ad}, Soyad: {self.soyad}, Yaş: {self.yas}, Pozisyon: {self.pozisyon}, Bakılan Hayvan Türleri: {self.bakilan_hayvan_turleri}"
        )

    def maas_hesapla(self):
        print(self.pozisyon + " için maaş hesaplandı. bakıcı")
