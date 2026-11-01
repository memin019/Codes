def harf_notu_hesapla(vize,final):

    ort = vize*(40/100)+final*(60/100)

    if ort>=90: harf_notu = "AA"
    elif ort>=80: harf_notu = "BA"
    elif ort>=70: harf_notu = "BB"
    elif ort>=60: harf_notu = "CB"
    elif ort>=50: harf_notu = "CC"
    elif ort>=40: harf_notu = "DC"
    elif ort>=30: harf_notu = "DD"
    elif ort>=20: harf_notu = "FD"
    else: harf_notu = "FF"

    return ort, harf_notu

vize = float(input("Vize notunuzu giriniz: "))
final = float(input("Final notunuzu giriniz: "))

ort, harf_notu = harf_notu_hesapla(vize,final)

print(f"Ortalama: {ort:.2f}  Harf notu: {harf_notu}")
