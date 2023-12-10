from Hayvan import Hayvan


class Surungen(Hayvan):
    def __init__(self, tur, yas, cins, deri_rengi):
        super().__init__(tur, yas, cins)
        self.deri_rengi = deri_rengi

    def __str__(self):
        return f"Surungen Türü: {self.tur}, Yaş: {self.yas}, Cins: {self.cins}, Deri Rengi: {self.deri_rengi}"

    def __sesCikar(self):
        print(f"{self.tur} tıslıyor.")

    def yemekYe(self):
        print(f"{self.tur} yemek yiyor. Böcek yiyor.")

    def yasHesapla(self):
        print(f"{self.tur} {2023 - self.yas} yaşında.")
