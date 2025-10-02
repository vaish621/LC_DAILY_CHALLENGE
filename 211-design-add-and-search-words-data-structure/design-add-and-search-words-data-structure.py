class TrieNode:
    
    def __init__(self):
        self.children={}
        self.isend=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        cur=self.root

        for w in word:
            if w not in cur.children:
                cur.children[w]=TrieNode()
            cur=cur.children[w]
        cur.isend=True
        

    def search(self, word: str) -> bool:
        

        def dfs(node,i):
            if i==len(word):
                return node.isend
            
            ch=word[i]

            if ch=='.':
                for child in node.children.values():
                    if dfs(child,i+1):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(node.children[ch],i+1)
        
        return dfs(self.root,0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)