import PySimpleGUI as sg
from YonetimSistemi import YonetimSistemi
from Memeli import Memeli
from Kus import Kus
from Surungen import Surungen
from Bakici import Bakici
from Veteriner import Veteriner
from Yonetici import Yonetici

yonetim_sistemi = YonetimSistemi()

hayvan_turleri = ["Memeli", "Kuş", "Sürüngen"]
calisan_pozisyonlari = ["Bakıcı", "Veteriner", "Yönetici"]

layout = [
    [
        sg.Text(
            "Hayvanat Bahçesi Yönetim Sistemi",
            font=("Helvetica", 16),
            justification="center",
        )
    ],
    [
        sg.Text("Hayvan Türü:"),
        sg.Combo(
            hayvan_turleri,
            key="tur",
            default_value=hayvan_turleri[0],
            enable_events=True,
        ),
    ],
    [sg.Text("Yaş:"), sg.InputText(key="yas")],
    [sg.Text("Cins:"), sg.InputText(key="cins")],
    [sg.Text("Ek Özellik:"), sg.InputText(key="ek_ozellik")],
    [sg.Button("Hayvan Ekle"), sg.Button("Hayvanları Listele")],
    [sg.Text("Çalışan Adı:"), sg.InputText(key="ad")],
    [sg.Text("Çalışan Soyadı:"), sg.InputText(key="soyad")],
    [sg.Text("Çalışan Yaşı:"), sg.InputText(key="calisan_yas")],
    [
        sg.Text("Pozisyon:"),
        sg.Combo(
            calisan_pozisyonlari,
            key="pozisyon",
            default_value=calisan_pozisyonlari[0],
            enable_events=True,
        ),
    ],
    [sg.Button("Çalışan Ekle"), sg.Button("Çalışanları Listele")],
    [sg.Multiline(size=(45, 5), key="output", disabled=True)],
    [sg.Exit()],
]

window = sg.Window(
    "Hayvanat Bahçesi Yönetim Sistemi", layout, element_justification="left"
)

while True:
    event, values = window.read()
    if event in (None, "Exit"):
        break
    elif event == "Hayvan Ekle":
        tur = values["tur"]
        yas = int(values["yas"]) if values["yas"].isdigit() else 0
        cins = values["cins"]
        ek_ozellik = values["ek_ozellik"]

        if tur == "Memeli":
            hayvan = Memeli(tur, yas, cins, ek_ozellik)
        elif tur == "Kuş":
            hayvan = Kus(tur, yas, cins, ek_ozellik)
        elif tur == "Sürüngen":
            hayvan = Surungen(tur, yas, cins, ek_ozellik)
        else:
            sg.popup("Bilinmeyen hayvan türü:", tur)
            continue

        yonetim_sistemi.hayvan_ekle(hayvan)
        window["output"].print(f"{tur} eklendi: {hayvan}")
    elif event == "Çalışan Ekle":
        ad = values["ad"]
        soyad = values["soyad"]
        calisan_yas = (
            int(values["calisan_yas"]) if values["calisan_yas"].isdigit() else 0
        )
        pozisyon = values["pozisyon"]

        if pozisyon == "Bakıcı":
            calisan = Bakici(
                ad, soyad, calisan_yas, bakilan_hayvan_turleri="kedi", maas=4000
            )  # Bakılan hayvan türleri örnektir, dinamik olabilir
        elif pozisyon == "Veteriner":
            calisan = Veteriner(
                ad, soyad, calisan_yas, uzmanlik_alani="köpek", maas=8000
            )
        elif pozisyon == "Yönetici":
            calisan = Yonetici(
                ad, soyad, calisan_yas, sorumlu_oldugu_bolum="hayvan bakımı", maas=10000
            )

        else:
            sg.popup("Bilinmeyen pozisyon:", pozisyon)
            continue

        yonetim_sistemi.calisan_ekle(calisan)
        window["output"].print(f"{pozisyon} eklendi: {calisan} ")

window.close()
