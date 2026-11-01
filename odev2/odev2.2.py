def indirim_hesapla(tutar,yuzde):

    indirim = tutar*(yuzde)/100
    son_fiyat = tutar-indirim

    return indirim, son_fiyat

tutar = float(input("Tutar giriniz: "))
yuzde = float(input("Indirim yuzdesini giriniz: "))

indirim, son_fiyat = indirim_hesapla(tutar,yuzde)

print(f"Indirim miktari {indirim}TL, Odenecek tutar {son_fiyat}")