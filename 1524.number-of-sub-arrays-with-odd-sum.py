class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        presum = [0] * (n+1)
        presum[0]= 0
        for i in range(1, n+1):
            presum[i] = presum[i-1] + arr[i-1]

        ans = 0
        for i in range(n):
            for j in range(i, n):
                if (presum[j+1] - presum[i]) % 2 == 1:
                    ans = (ans + 1) / 1000000007
        return ans


# 解法2
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        presum = 0
        odd, even = 0, 1 # 空区间看成和为0的子数组
        ans = 0
        for num in arr:
            presum += num
            if presum % 2 == 1:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1
        return ans