#bai 1
#y = int (input("nhap thang: "))
#x = int(input("nhap nam: "))
#if x < 0 or y < 0 or y >12 :
    #print ("nhap lai thang nam")
#if y == 1 or y == 3 or y ==5 or y ==7 or y == 8 or y == 10 or y == 12 :
    #print ("co 31 ngay") 
#if y ==4 or y ==6 or y==9 or y ==11 :
    #print("co 30 ngay")
#if  y == 2 and x % 4 == 0 :
    #print ("co 29 ngay")
#if y ==2 and x % 4 != 0 :
    #print("co 28 ngay") 

#bai2 
#x = int(input("nhap tien luong: "))
#if x < 0:
    #print ("nhap lai")
#elif x < 7000000 :
    #print ("thue là: ",x *0.1 ,"thu nhap là: " ,x - x *0.1)
#elif x < 150000000 :
 #   print ("thue la: ", x * 0.2 , "thu nhap la: ", x - x *0.2 )
#else :
#    print ("thue la: " , x * 0.3, "thu nhap la: ", x - x * 0.3 )
#Bai3
#N = int(input("nhap vao so nguyen N: "))
#tong = 0
#dem = 0
#while N != 0 :
#  tong +=  N % 10
#  N //= 10
#  dem += 1
#print ("tong cac chu so la: ", tong, "so chu so la: ", dem)
#bai 4:
x = int(input("nhap so xu: "))
y = x // 28
z = y // 3
print ("so chai bia co the mua la: ", y+z)