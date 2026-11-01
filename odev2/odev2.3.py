yil = int(input("Dogum yilinizi giriniz: "))

yas = 2026-yil

if yas>=18:
    print(f"Şahis {yas} yasinda oldugundan ehliyet alabilir.")
else:
    print(f"Şahis {yas} yasinda oldugundan ehliyet alamaz.")