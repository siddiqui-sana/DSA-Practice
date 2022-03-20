class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord in wordList:
            wordList.remove(beginWord)
        wordset=set(wordList)
        Q=deque()
        c=0
        Q.append(beginWord)
        while Q:
            L=len(Q)
            c += 1  
            #To calculate the no.of transformation. Done outside the for loop because                no matter how many possible wordds get appended in Q inside the for loop                only one best possibility needs to be counted.
            for i in range(L):
                curr_word=Q.popleft()
                for j in range(len(curr_word)):
                    for alphabet in ascii_lowercase:
                        word=curr_word[:j]+alphabet+curr_word[j+1:]
                        if word in wordset:
                            Q.append(word)
                            if word == endWord:
                                return c+1
                                ##c+1 because last word also needs to be counted
                            wordset.remove(word)
        return 0
                            

        
        
