import random

sayi = random.randint(1,100)
i=0

while True:
    try:
        n = int(input(f"{i+1}. Tahmin: "))
        i+=1

    except ValueError:
        print("Lutfen bir sayi giriniz.")
        continue
    
    if n==sayi:
        print("Tebrikler, sayiyi buldunuz!")
        break

    elif n>sayi:
        print("Asagi in!")

    elif n<sayi:
        print("Yukari cik!")