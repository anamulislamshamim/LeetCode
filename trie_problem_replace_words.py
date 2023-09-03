#!/usr/bin/env python3


class Node:
    def __init__(self):
        self.children = dict()
        self.isComplete = False
        self.count = 1


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        temp = self.root
        for char in word:
            if not temp.children.get(char):
                temp.children[char] = Node()
            else:
                temp.children[char].count += 1
            temp = temp.children[char]
        temp.isComplete = True

    def search(self, word):
        temp = self.root
        for char in word:
            if not temp.children.get(char):
                return False
            temp = temp.children[char]
        return temp.isComplete

    def prefix(self, word):
        temp = self.root
        for char in word:
            if not temp.children.get(char):
                return False
            temp = temp.children[char]
        return True
    # find how many words are in the trie with the particular prefix
    def find(self, word):
        temp = self.root
        res = 0
        for char in word:
            if not temp.children.get(char):
                return 0
            res = temp.children[char].count
            temp = temp.children[char]
        return res

    def check(self, word):
        temp = self.root
        sub = ""
        for char in word:
            # check if the char doesn't exist in the trie and also
            # check current.isComplete is False since it is root
            # the root node is look like:
            # Node() -> self.children = {a: something}, self.isComplete = False
            # for example: if the test case string is following
            # s = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
            # if word = baba, word[0] = 'b' is not exist in the trie
            # if 'b' does not exist in the trie then temp.isComplete should be False 
            if not temp.children.get(char) and not temp.isComplete:
                return word
            # check whether temp.isComplete is True or False
            # if true that means the substring is actually the word in the trie
            # with what we want to replace the string's existing word
            # for example: if word = cattled then sub string sub is 'cat' that
            # is exist in cat. so true means we retrieve the word
            # so, return sub
            if temp.isComplete:
                return sub
            sub += char
            if temp.children.get(char):
                temp = temp.children[char]
        return word




def build_trie(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie
if __name__ == "__main__":
    trie = build_trie(["a", "aa", "aaa", "aaaa"])
    # print(trie.find('a'))
    s = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
    res = []
    for word in s.split():
        res.append(trie.check(word))
    print(" ".join(res))
