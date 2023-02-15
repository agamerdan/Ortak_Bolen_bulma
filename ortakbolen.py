
sayi1=input("Sayi1: ")
sayi2=int(input("Sayi2: "))
while True:
  
    sayi1=int(sayi1)
    if sayi1<sayi2:
       s=sayi2-sayi1
       sayi2=s
    else:
       s=sayi1-sayi2
       sayi1=s
    if(sayi1%s==0 and sayi2%s==0):
           print(s)
           break
