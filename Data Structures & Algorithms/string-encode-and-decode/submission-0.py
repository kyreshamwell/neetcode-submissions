class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(words)}#{words}' for words in strs)
        

    def decode(self, s: str) -> List[str]:
        i = 0
        arr = []
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j]) 
            word = j + 1 + length
            addWord = s[j+1:word]
            i = word
            arr.append(addWord)
        return arr


        
