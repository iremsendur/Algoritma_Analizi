def elemanBul(dizi,aranan):
	bas=0
	son=len(dizi)
	while bas < son:
        	x = bas + (son - bas) // 2
        	deger = dizi[x]
        	if aranan == deger:
            		return x
        	elif aranan > deger:
            		if bas == x:
                		break
            		bas = x
        	elif aranan < deger:
            		son = x
import random
def dizi_olstr(dizi, size):
      dizi = random.sample(range(1, 10000000), size)
      return dizi
size = int(input("Dizi uzunlugu kac olsun:"))
dizi = []
dizi_olstr(dizi, size)
dizi = sorted(dizi_olstr(dizi, size))
aranan = int(input("Sayi girin:"))
import time
start_time=time.time()
print elemanBul(dizi, aranan)
print time.time()-start_time
