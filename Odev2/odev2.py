import itertools

file=open("tablo.txt", "r")
header=file.readline().split(",")
veri=file.readlines(1)
boyut=len(header)

for i in range(1,boyut+1):
    comb=list(itertools.combinations(range(0,boyut), i))
    max=0
    for eleman in comb:
        curmaks=0
        for satir in veri:
            durum=1
            for indis in eleman:
                deger=satir.split(",")[indis].replace('\n','')
                if(deger=='0'):
                    durum=0
            if durum==1:
                curmaks=curmaks+1

        if(curmaks>max):
            max=curmaks
            indisler=eleman


    urun=""
    for i in indisler:
        urun=urun+header[i].replace('\n','')

    print("------- %s karsilastirma ------"%i)
    if(max==0):
        print ("%s i urun icin maks bulunamadi"%i)
    else:
        print ("%s urunleri %s kere satildi"%(urun,max))
    print("")
