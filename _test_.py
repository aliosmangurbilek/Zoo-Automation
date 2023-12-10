from YonetimSistemi import YonetimSistemi
from Kus import Kus
from Memeli import Memeli
from Surungen import Surungen
from Bakici import Bakici
from Veteriner import Veteriner
from Yonetici import Yonetici

yonetim_sistemi = YonetimSistemi()

kartal = Kus("Kartal", 5, "Erkek", 120)
kedi = Memeli("Kedi", 3, "Dişi", "Gri")
timsah = Surungen("Yılan", 7, "Erkek", "Yeşil")

kedi._Memeli__sesCikar()  ## private method
kartal._Kus__sesCikar()  ## private method
timsah._Surungen__sesCikar()  ## private method

kedi.yemekYe()
kartal.yemekYe()
timsah.yemekYe()

ayse = Bakici("Ayşe", "Yılmaz", 30, ["Kartal", "Papağan"], 3000)
ahmet = Veteriner("Ahmet", "Kara", 40, "Genel Veterinerlik", 5000)
elif_yonetici = Yonetici("Elif", "Çelik", 35, "Hayvan Bakımı", 10000)

yonetim_sistemi.hayvan_ekle(kartal)
yonetim_sistemi.hayvan_ekle(kedi)
yonetim_sistemi.hayvan_ekle(timsah)

yonetim_sistemi.calisan_ekle(ayse)
yonetim_sistemi.calisan_ekle(ahmet)
yonetim_sistemi.calisan_ekle(elif_yonetici)

print("\nHayvanlar Listesi:")
yonetim_sistemi.hayvanlari_goster()

print("\nÇalışanlar Listesi:")
yonetim_sistemi.calisanlari_goster()

# Özel işlemler
ayse.hayvanlari_besle()

ahmet.hayvanlari_muayene_et()

elif_yonetici.bolumu_yonet()
