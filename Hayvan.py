class Hayvan:
    def __init__(self, tur, yas, cins):
        self.tur = tur
        self.yas = yas
        self.cins = cins

    def __str__(self):
        print(f"{self.tur}, Yaş: {self.yas}, Cins: {self.cins}")

    def __sesCikar(self):
        raise NotImplementedError("Bu metod alt sınıflar tarafından uygulanmalıdır.")

    def yemekYe(self):
        print(f"{self.tur} yemek yiyor.")

    def yasHesapla(self):
        print(f"{self.tur} {2023 - self.yas} yaşında.")
