class Calisan:
    def __init__(self, ad, soyad, yas, pozisyon, maas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.pozisyon = pozisyon
        self.maas = maas

    def __str__(self):
        return f"{self.ad} {self.soyad}, Yaş: {self.yas}, Pozisyon: {self.pozisyon}"

    def calis(self):
        print(f"{self.ad} {self.pozisyon} olarak çalışıyor.")

    def maas_hesapla(self):
        if self.pozisyon == "Yönetici":
            print(10000)
        elif self.pozisyon == "Veteriner":
            print(8000)
        elif self.pozisyon == "Bakıcı":
            print(4000)
        else:
            return 0

    def bilgileri_goster(self):
        print(
            f"Ad: {self.ad}, Soyad: {self.soyad}, Yaş: {self.yas}, Pozisyon: {self.pozisyon}"
        )
