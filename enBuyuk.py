#girilen sayılardan en büyüğünü ekrana yazdırma

sayilar=[]
for i in range(5):
    sayi=int(input(f"{i+1}. sayıyı giriniz:"))
    sayilar.append(sayi)

print(max(sayilar))
