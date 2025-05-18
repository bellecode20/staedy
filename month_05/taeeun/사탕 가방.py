# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXdHxTNqC2IDFAS5

def max_candies_per_bag(n, m, candies):
    left, right = 1, max(candies)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        total_bags = sum(candy // mid for candy in candies)

        if total_bags >= m:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    candies = list(map(int, input().split()))
    ans = max_candies_per_bag(n, m, candies)
    print(f"#{tc} {ans}")