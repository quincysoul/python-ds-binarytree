class Node:
    def __init__(self, character=None, is_leaf=False):
        self.character = character
        self.nexts = {
            ch: None for ch in "abcdefghijklmnopqrstuvwxyz"
        }  # "s": Node(s... nexts:[], isleaf: False)
        self.is_leaf = is_leaf


node = Node()
print(vars(node))


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, key):
        if key is None:
            return False
        print("inserting key:", key)
        node = self.root
        for ch in key:
            ch = ch.lower()
            # key = dogs
            # level= 0123
            if node.nexts[ch] is None:
                node.nexts[ch] = Node(ch)

            print("Node inserting on:{}", node.character)

            node = node.nexts[ch]

        node.is_leaf = True
        print("Setting leaf on node:", vars(node))

    def search(self, key):

        node = self.root
        for ch in key:
            ch = ch.lower()
            if node[ch] is None:
                return False


trie = Trie()
trie.insert("Dogs")
