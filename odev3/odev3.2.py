n = int(input("Bir sayi giriniz: "))
total=0

for i in range(n+1):
    total+= i

print(f"1'den {n}'e kadar sayilarin toplami = {total}")