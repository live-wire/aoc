class Trie:
    def __init__(self, c=None):
        self.c = c
        self.d = {}
        self.is_word_end = False
        self.words_end_here = []
    
    def insert(self, word):
        self._insert(word, word)
    
    def _insert(self, word, full_word):
        if word == '':
            self.is_word_end = True
            self.words_end_here.append(full_word)
            return
        if word[0] not in self.d:
            self.d[word[0]] = Trie()
        self.d[word[0]]._insert(word[1:], full_word)
    
    def search(self, word):
        if word == '':
            return self.is_word_end
        if word[0] not in self.d:
            return False
        return self.d[word[0]].search(word[1:])

if __name__ == "__main__":
    trie = Trie()
    trie.insert('one')
    trie.insert('two')
    print(trie.search('one'), trie.search('two'), trie.search('hell'), trie.search('worl'))
