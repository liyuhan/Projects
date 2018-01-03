class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return (i, j)

def main():
        nums = [3,2,4]
        target = 6

        ret = Solution().twoSum(nums, target)
        print(ret)

if __name__ == '__main__':
    main()