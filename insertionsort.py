def insertionSort(alist):
    karsilastirma=0
    yerdegistirme=0
    for index in range(0,len(alist)):
        yerdegistirme=yerdegistirme+1
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
          karsilastirma=karsilastirma+1
          alist[position]=alist[position-1]
          position = position-1
        alist[position]=currentvalue
    print("karsilastirma sayisi :",karsilastirma)
    print("yerdegistirme sayisi :" ,yerdegistirme)

import random
def  createAnArray(size):
    array=[]
    for i in range(0,size):
        array.append(int(random.uniform(-1000,1000)))
        #print(i,".item",array[i])
    return array
size=int(input("size ?"))   
alist=createAnArray(size)
import time
t_start=time.time()
insertionSort(alist)
t_end=time.time()
for i in range(0,len(alist)):
    print(i,".item",alist[i])
print("time :",t_end-t_start)
