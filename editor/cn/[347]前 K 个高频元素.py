class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        def insert(node, heap):
            if len(heap) < k:
                heap.append(node)
                adjust2down((len(heap) - 2) // 2, heap)
            elif len(heap) >= k and node[1] > heap[0][1]:
                heap[0] = node
                adjust2down(0, heap)

        def adjust2down(idx, heap):
            min = idx
            left = idx * 2 + 1
            right = idx * 2 + 2
            print(idx)
            if left < len(heap) and heap[left][1] < heap[min][1]:
                min = left
            if right < len(heap) and heap[right][1] < heap[min][1]:
                min = right
            if min != idx:
                heap[min], heap[idx] = heap[idx], heap[min]
                adjust2down(min, heap)

        from collections import Counter
        fre_list=[]
        c=Counter(nums)
        for i in c:
            fre_list.append((i,c[i]))

        heap = []
        for i in fre_list:
            insert(i,heap)

        return [i[0] for i in heap]



if __name__ == "__main__":
    res = Solution().topKFrequent([1],1)
    print(res)