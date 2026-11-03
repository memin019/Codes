from datetime import datetime


str = input("Sinav tarihini giriniz (GG.AA.YYYY SS.DD formatinda): ")

sinav = datetime.strptime(str, "%d.%m.%Y %H.%M")
now = datetime.now()

fark = sinav - now

gun = fark.days
saat = fark.seconds/3600

print(f"Sinava {gun} gun {saat:.0f} saat kalmistir.")

    