#tính lũy thừa nhanh
#xây dựng công thức đệ quy
# log (2, 10**9) = 29,89.... thay vì tính 10**9 phép tính thì có thể tính 30 lần

import math
def pow(a,x):
    if x ==0 :
        return 1
    return ((pow(a,x//2))**2 +1 if x%2==1 else 0) % (10**9+1)
n = int(input("Nhập số nguyên n : "))
k = int(input("Nhập số nguyên k: "))
print("Số chỉnh hợp lặp chập k của n là: " ,pow(n,k))
