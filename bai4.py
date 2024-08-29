MOD = 10**9 + 7

def count_ways(n):
    dp = [0] * (n + 1) #tạo danh sách dp có kích thước 5 với mỗi ptu đều có gtri ban đầu là 0
    dp[0] = 1  # Có 1 cách để đạt tổng là 0 đó là không lắc xúc sắc

    for i in range(1, n + 1):
        for face in range(1, 7): # duyệt qua các ptu 1,2,3,...6 , ko duyệt qua 7
            if i - face >= 0:
                dp[i] = (dp[i] + dp[i - face]) % MOD

    return dp[n]

if __name__ == "__main__":
    n = int(input("nhập số n: "))
    print(count_ways(n))

