class Solution:
    def canCross(self, stones: List[int]) -> bool:
        d={}
        for i in stones:
            if i==0:
                d[i]={1}
            else:
                d[i]=set()
        
        for i in d:
            for j in d[i]:
                if j+i==stones[-1]:
                    return True
                else:
                    if (i+j) in d:
                        if j-1<=0:
                            d[i+j].add(j)
                            d[i+j].add(j+1)
                        else:
                            d[i+j].add(j-1)
                            d[i+j].add(j)
                            d[i+j].add(j+1)
        return False
        
            
            
