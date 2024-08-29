def derangement(n):
    MOD = 10**9 + 7

    # Xử lý các trường hợp cơ bản
    if n == 1:
        return 0
    if n == 2:
        return 1

    # Khởi tạo mảng dp với kích thước n + 1
    dp = [0] * (n + 1)
    dp[1] = 0
    dp[2] = 1

    # Tính toán số mất thứ tự cho các giá trị từ 3 đến n
    for i in range(3, n + 1 ,1):
        dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % MOD

    return dp[n]

# Đọc số n từ đầu vào
n = int(input("Nhập số nguyên n : ").strip())
if (1 <= n <= 10**6):
    print(derangement(n))
else:
    print("Vui lòng nhập đúng giới hạn của n")


