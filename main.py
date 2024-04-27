from ui import Ui
from json_reader import ReadJson

def GetCountry():
    try:
        text = input("lütfen aradığınız ülkenin en az 3 harfini giriniz: ")
        assert len(text)>=3, "en az 3 harf giriniz..."
        for nameKey, nameValue in names.items():
            if text.lower() in nameValue.lower():
                print(f"***ülkenin adı={nameValue}, kısaltması={iso3[]}, telefon kodu={phone[nameKey]}, kitasi={}, parabirimi={}")
    except AssertionError as e:
        print(e)
    except Exception:
        print("hatalı giriş")

menu = Ui({"isimden veri getir",
           "telefon kodundan getir",
           "kıtadaki ülkeleri getir",
           "para biriminden ülke getir"})
reader = ReadJson
continent = reader.ReadToDict("continent.json")
currency = reader.ReadToDict("currency.json")
iso3 = reader.ReadToDict("iso3.json")
names = reader.ReadToDict("names.json")
phone = reader.ReadToDict("phone.json")

while True:
    menu.Show_Menu()
    choise = menu.GetChoise()
    if choise == 1:
        GetCountry()