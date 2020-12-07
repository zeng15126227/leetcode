class Solution:
    def reconstructQueue(self, people: list) -> list:
        sorted_queue = sorted(people,key=lambda x:(-x[0],x[1]))
        res=[]
        for p in sorted_queue:
            if len(res) <= p[1]:
                res.append(p)
            elif len(res) > p[1]:
                res.insert(p[1], p)
        return res