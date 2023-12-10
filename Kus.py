from Hayvan import Hayvan


class Kus(Hayvan):
    def __init__(self, tur, yas, cins, kanat_uzunlugu):
        super().__init__(tur, yas, cins)
        self.kanat_uzunlugu = kanat_uzunlugu

    def __str__(self):
        return f"Kuş Türü: {self.tur}, Yaş: {self.yas}, Cins: {self.cins}, Kanat Uzunluğu: {self.kanat_uzunlugu}"

    def __sesCikar(self):
        print(f"{self.tur} ötüyor.")

    def yemekYe(self):
        print(f"{self.tur} yemek yiyor. Tohum yiyor.")

    def yasHesapla(self):
        print(f"{self.tur} {2023 - self.yas} yaşında.")
