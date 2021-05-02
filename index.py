taple=(1,1,1,3,4,4,3,5,6,7,6,4,6,3,4,6,2,4,6,2,5,8,7,4
,4,2,7,8,9,0,1,2,5,4,3,5,4,3,5,6,7,5,6,4,3,6,4,5,3,5,4,
5,3,5,6,4,3,4,5,3,5,7,6,3,5,7,9,5,4,3,2,3,4,5,4,5,3,7)

lista=[]
for i in taple:
    lista.append(i)
lista.sort()
Ukey=[]
for i in range(len(lista)):
    if lista[i-1]!=lista[i]:
        Ukey.append(lista[i-1])
tampung={}
for i in Ukey:
    tampung[i]=len([ x for x in lista if x==i ])
for key, value in tampung.items():
    print('Angka', key,'ada',value,'buah')