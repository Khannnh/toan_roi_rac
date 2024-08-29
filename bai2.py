# 2 số tự nhiên n và k thỏa mãn (0 <= k <= n <= 100)

def tinhgiaithua(x):
    giaithua=1
    if x==0 or x ==1:
        return giaithua
    else:
        for i in range(2,x+1,1):
            giaithua=giaithua*i
        return giaithua
n=int(input("Nhập số tự nhiên n: "))
k=int(input("Nhập số tự nhiên k: "))
if (0 <= k<= n <= 100):
    a=tinhgiaithua(n)
    b=tinhgiaithua(k)
    c= tinhgiaithua(n-k)
    d=(a/(b*c))%(10**9+7)
    print("số cấu hình tổ hợp chập k của n là: ",d)
else:
    print("Vui lòng nhập đúng giới hạn của n và k ")


