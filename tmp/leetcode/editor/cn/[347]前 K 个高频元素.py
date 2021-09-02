# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [1], k = 1
# 输出: [1] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  k 的取值范围是 [1, 数组中不相同的元素的个数] 
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的 
#  
# 
#  
# 
#  进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。 
#  Related Topics 数组 哈希表 分治 桶排序 计数 快速选择 排序 堆（优先队列） 
#  👍 851 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class small_hat_heap():
    def __init__(self):
        self.heap = []

    #自下而上调整小顶堆
    def adjust2up(self, idx):
        while idx >= 0:
            left = idx * 2 + 1
            right = idx * 2 + 2
            min_idx = idx
            if left < len(self.heap) and self.heap[left][1] < self.heap[min_idx][1]:
                min_idx = left
            if right < len(self.heap) and self.heap[right][1] < self.heap[min_idx][1]:
                min_idx = right
            if min_idx != idx:
                self.heap[min_idx], self.heap[idx] = self.heap[idx], self.heap[min_idx]
                idx = (idx-1) // 2
            else:
                break

    # 自顶而下调整小顶堆
    def adjust2down(self, idx):
        while idx <= len(self.heap)-1-1//2:
            left = idx * 2 + 1
            right = idx * 2 + 2
            min_idx = idx
            if left < len(self.heap) and self.heap[left][1] < self.heap[min_idx][1]:
                min_idx = left
            if right < len(self.heap) and self.heap[right][1] < self.heap[min_idx][1]:
                min_idx = right
            if min_idx != idx:
                self.heap[min_idx], self.heap[idx] = self.heap[idx], self.heap[min_idx]
                idx = min_idx
            else:
                break


    #向小顶堆添加元素
    def add(self, val):
        self.heap.append(val)
        n = len(self.heap)
        idx = n-1
        # 从插入节点的夫节点向上调整小顶堆
        self.adjust2up((idx - 1) // 2)

    #删除小顶堆堆顶元素
    def pop(self):
        n = len(self.heap)
        self.heap[0], self.heap[n-1] = self.heap[n-1], self.heap[0]
        self.heap.pop()
        self.adjust2down(0)

    #获取小顶堆大小
    def size(self):
        return len(self.heap)


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = small_hat_heap()

        memo={}
        for i in nums:
            memo[i] = memo.get(i, 0) + 1

        for key, freq in memo.items():
            heap.add((key,freq))
            if heap.size() > k:
                heap.pop()

        return [i[0] for i in heap.heap]

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().topKFrequent([5,3,1,1,1,3,5,73,1],3)
    print(res)

