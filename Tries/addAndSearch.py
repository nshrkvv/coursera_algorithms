class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.trie = TrieNode()

    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        def dfs(node, index):
            if index == len(word):
                return node.is_end
            if word[index] == '.':
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            if word[index] in node.children:
                return dfs(node.children[word[index]], index + 1)
            return False

        return dfs(self.trie, 0)