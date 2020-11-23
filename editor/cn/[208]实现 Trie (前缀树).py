# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。 
# 
#  示例: 
# 
#  Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");   
# trie.search("app");     // 返回 true 
# 
#  说明: 
# 
#  
#  你可以假设所有的输入都是由小写字母 a-z 构成的。 
#  保证所有输入均为非空字符串。 
#  
#  Related Topics 设计 字典树 
#  👍 468 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.childs = [None for _ in range(26)]
        self.isword=False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode(-1)



    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for i in word:
            index = ord(i)-ord('a')
            if not cur.childs[index]:
                cur.childs[index] = TreeNode(i)
            cur = cur.childs[index]
        cur.isword=True



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for i in word:
            index = ord(i)-ord('a')
            if not cur.childs[index]:
                return False
            cur = cur.childs[index]
        if cur.isword:
            return True
        else:
            return False



    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for i in prefix:
            index = ord(i) - ord('a')
            if not cur.childs[index]:
                return False
            cur = cur.childs[index]

        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    obj = Trie()
    obj.insert('word')
    obj.insert('prefix')
    param_2 = obj.search('word')
    param_3 = obj.startsWith('pre')
    print(param_2)
    print(param_3)
