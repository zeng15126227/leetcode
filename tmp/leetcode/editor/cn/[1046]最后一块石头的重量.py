# 有一堆石头，每块石头的重量都是正整数。 
# 
#  每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下： 
# 
#  
#  如果 x == y，那么两块石头都会被完全粉碎； 
#  如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。 
#  
# 
#  最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：[2,7,4,1,8,1]
# 输出：1
# 解释：
# 先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
# 再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
# 接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
# 最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= stones.length <= 30 
#  1 <= stones[i] <= 1000 
#  
#  Related Topics 数组 堆（优先队列） 
#  👍 174 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """


class heap:
    def __init__(self):
        """
        初始化，默认创建一个大顶堆
        """
        self.heap = []

    def size(self):
        return len(self.heap)

    def top(self):
        if self.size:
            return self.heap[0]
        return None

    def push(self, item):
        """
        添加元素
        第一步，把元素加入到数组末尾
        第二步，把末尾元素向上调整
        """
        self.heap.append(item)
        self._sift_up(self.size - 1)

    def _sift_up(self, index):
        """
        向上调整
        如果父节点和当前节点满足交换的关系，
        交换后持续将当前节点向上调整
        """
        while index:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                break
            self._swap(parent, index)
            index = parent

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def pop(self):
        """
        弹出堆顶
        第一步，记录堆顶元素的值
        第二步，交换堆顶元素与末尾元素
        第三步，删除数组末尾元素
        第四步，新的堆顶元素向下调整
        第五步，返回答案
        """
        item = self.heap[0]
        self._swap(0, self.size - 1)
        self.heap.pop()
        self._sift_down(0)
        return item

    def _sift_down(self, index):
        """
        向下调整
        如果子节点和当前节点满足交换的关系，
        交换之后，则持续将当前节点向下调整
        """
        # 若存在子节点，下标从0开始
        while index * 2 + 1 < self.size:
            bigest = index
            left = index * 2 + 1
            right = index * 2 + 2
            if self.heap[left] > self.heap[bigest]:
                bigest = left
            if right < self.size and self.heap[right] > self.heap[bigest]:
                bigest = right
            if bigest == index:
                break
            self._swap(index, bigest)
            index = bigest

# leetcode submit region end(Prohibit modification and deletion)
