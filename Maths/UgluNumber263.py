##Ugly numbers are those number whose prime factors are 2, 3 or 5.

## Check if n is ugly NUmber or not.

class Solution:
    def isUgly(self, n: int) -> bool:
        if n==1:
            return True
        if n<1:
            return False
        else:
            l=[2,3,5]
            for i in l:
                while n%i==0:
                    n=n//i
                if n==1:
                    return True
                
            return False
