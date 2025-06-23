# swea 9999 광고 시간 정하기

def upper_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo

T = int(input())
for tc in range(1, T + 1):
    L = int(input())
    N = int(input())

    starts, ends, segment_sum = [], [], [0]
    for _ in range(N):
        s, e = map(int, input().split())
        starts.append(s)
        ends.append(e)
        segment_sum.append(segment_sum[-1] + (e - s))

    best = 0

    # 스타트에 맞추는 경우
    for i in range(N):
        w_end = starts[i] + L                   
        r = upper_bound(ends, w_end)            
        covered = segment_sum[r] - segment_sum[i]             
        if r < N and starts[r] < w_end:        
            covered += w_end - starts[r]
        if covered > best:
            best = covered

    # 엔드에 맞추는 경우
    for j in range(N):
        w_start = ends[j] - L                 
        l = upper_bound(ends, w_start)         
        if l > j:       
            continue
        covered = segment_sum[j + 1] - segment_sum[l]       
        if w_start > starts[l]:                 
            covered -= (w_start - starts[l])
        if covered > best:
            best = covered

    print(f"#{tc} {best}")
