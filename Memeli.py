from Hayvan import Hayvan


class Memeli(Hayvan):
    def __init__(self, tur, yas, cins, yun_rengi):
        super().__init__(tur, yas, cins)
        self.yun_rengi = yun_rengi

    def __str__(self):
        return f"Memeli Türü: {self.tur}, Yaş: {self.yas}, Cins: {self.cins}, Yün Rengi: {self.yun_rengi}"

    def __sesCikar(self):
        print(f"{self.tur} bir ses çıkarıyor: miyav")

    def yemekYe(self):
        print(f"{self.tur} yemek yiyor. Süt içiyor.")

    def yasHesapla(self):
        print(f"{self.tur} {2023 - self.yas} yaşında.")
