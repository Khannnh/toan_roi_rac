# 2 số tự nhiên n và k thỏa mãn 0 <= k <= n <= 10^9
n= int(input("Nhập số nguyên n : "))
k= int(input("Nhập số nguyên k : "))
if (0 <= k <= n <= 10**9):
    x = (n**k)%(10**9+7)
    print("số chỉnh hợp lặp chập k của n là : " , x)
else:
    print("Vui lòng nhập đúng giới hạn của n và k")
