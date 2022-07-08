def solution(n, nums):
    res  = 0
    if n < 3:  # 特殊情况判断
      return 0
    maxLeft, maxRight = [0] * n, [0] * n
    maxLeft[0], maxRight[-1] = nums[0], nums[-1]
    for i in range(1, n):
      maxLeft[i] = max(maxLeft[i-1], nums[i])
    for i in range(n-2, -1, -1):
      maxRight[i] = max((maxRight[i+1], nums[i])
    for i in range(n):
      res += min(maxLeft[i], maxRight[i]) - nums[i]
    return res
                        
                     
