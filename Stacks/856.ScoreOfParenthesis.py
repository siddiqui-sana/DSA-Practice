class Solution:
    def scoreOfParentheses(self, st: str) -> int:
        s=[]
        for i in st:
            if i =='(':
                s.append(i)
            else:
                t=s[-1]
                if t=='(':
                    s.pop()
                    s.append(1)
                else:
                    sm=0
                    while s[-1]!='(':
                        j=s.pop()
                        if j!='(' and j!=')':
                            sm=sm+j
                    s.pop()
                    s.append(2*sm)
        z=0
        while(len(s)!=0):
            z=z+s.pop()
        return z
