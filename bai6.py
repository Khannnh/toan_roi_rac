from itertools import combinations
from math import gcd
from functools import reduce #rút gọn xâu nhị phân

def lcm(a, b):
    return a * b // gcd(a, b) # do python 3.8 < 3.9 nên ko thể dùng math.lcm do đó cần tính qua ước chung nhỏ nhất

def count_numbers(n, primes):
    k = len(primes)   #danh sách các số nguyên tố
    count = 0

    # Sử dụng Inclusion-Exclusion Principle bao hàm loại trừ
    for i in range(1, k+1):
        for comb in combinations(primes, i):
            lcm_value = reduce(lcm, comb)  #tính bội chung nhỏ nhất
            if i % 2 == 1:  # Cộng vào khi số lượng phần tử lẻ
                count += n // lcm_value
            else:           # Trừ đi khi số lượng phần tử chẵn
                count -= n // lcm_value

    # Số các số tự nhiên nhỏ hơn hoặc bằng n và không chia hết cho bất kỳ số nguyên tố nào
    result = n - count
    return result

# Đọc dữ liệu vào
n = int(input("Nhập n: "))
k = int(input("Nhập k: "))
primes = list(map(int, input("Nhập k số nguyên tố: ").split(",")))
# input sẽ nhập chuỗi " 2,3,5"
# split biến chuỗi trên thành danh sách các chuỗi "2" , "3" , "5"
# map(int) biến các chuỗi thành danh sách các số nguyên '[2,3,5]'
# list(...) sẽ chuyển đổi đối tượng map thành danh sách thực sự: [2, 3, 5, 7].

# Tính toán và in kết quả
result = count_numbers(n, primes)
print("Kết quả cần tìm là : " , result)
