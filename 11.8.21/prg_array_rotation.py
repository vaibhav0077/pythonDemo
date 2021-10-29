
arr = int(input("Size of Array : "))
aaaa = []
arrMod = []
for i in range(0, arr):
    aaaa.append(int(input("Enter Number for index "+ str(i) + " : ")))

bbbb = aaaa

rotaSize = int(input("Enter size of Rotation array  :"))

rotaSize %= len(aaaa)

arrMod = []

for j in range(0, arr):
    temp = j+rotaSize
    if j+rotaSize >= arr:
        x = arr
        temp = j + rotaSize - x
        x+= x

    
    arrMod.append(aaaa[temp])
    print(arrMod[j] , end=' ')




    

