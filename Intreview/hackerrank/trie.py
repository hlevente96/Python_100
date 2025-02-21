class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.word_count = 0

class Trie:
    def __init__(self):
        self.root = Node("")

    def add(self, string):
        node = self.root
        for c in string:
            if c not in node.children:
                node.children[c] = Node(c)
            node = node.children[c]
            node.word_count += 1

    def find(self, string):
        node = self.root
        for c in string:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.word_count


t = Trie()
t.add("test")
t.add("term")
t.add("tool")
t.add("tell")
t.add("tes")
print(t.find("test"))
