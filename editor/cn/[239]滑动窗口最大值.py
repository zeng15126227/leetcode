class dequeue:
    def __init__(self):
        self.list = []
    #添加元素时，操作在队尾
    def add(self, x):
        while self.list and self.list[-1] < x:
            self.list.pop()
        self.list.append(x)
    #移除元素，操作在队头
    def remove(self, x):
        if x == self.list[0]:
            self.list.pop(0)
    #队头是最大元素
    def getmax(self):
        return self.list[0]

class Solution:

    def maxSlidingWindow(self, nums: list, k: int) -> list:
        res = []
        queue = dequeue()
        for i in range(k):
            queue.add(nums[i])
        res.append(queue.getmax())

        for i in range(k,len(nums)):
            queue.remove(nums[i-k])
            queue.add(nums[i])
            res.append(queue.getmax())

        return res

if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    res=Solution().maxSlidingWindow(nums,3)
    print(res)
