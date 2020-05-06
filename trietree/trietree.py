# 前缀树  leetcode208. 实现Trie(前缀树)
# 例子
# 1.一个字符串类型的数组arr1,另一个字符串类型的数组arr2.arr2中有哪些字符,是arr1中出现的,请打印。
# 2.arr2中哪些字符是作为arr1中某个字符串的前缀出现的？请打印
# 3.请打印arr2中出现次数最大的前缀

class TrieNode:
    def __init__(self):
        self.path=0
        self.end=0
        self.next={}
class TrieTree:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word:str) ->None:
        cur=self.root
        for i in range(len(word)):
            cur.path+=1
            if word[i] not in cur.next.keys(): 
                cur.next[word[i]]=TrieNode()
            cur=cur.next[word[i]]
        cur.end+=1
    def search(self,word:str) ->bool:
        cur=self.root
        for i in range(len(word)):
            if word[i] not in cur.next.keys():
                return False
            cur=cur.next[word[i]]
        if cur.end>=1:return True
        else:return False
    def startsWith(self,prefix:str) ->bool:
        cur=self.root
        for i in range(len(prefix)):
            if prefix[i] not in cur.next.keys():
                return False
            cur=cur.next[prefix[i]]  
        return True
if __name__=="__main__":
    trie = TrieTree()
    trie.insert("apple")
    trie.search("apple")
    trie.search("app")
    trie.startsWith("app")
    trie.insert("app")
    trie.search("app")

