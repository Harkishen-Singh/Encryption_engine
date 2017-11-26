
from code_allocation import code_allocation

class conversion(code_allocation):
    digit =0
    def convert(self,n):

        num=0
        d=0
        c=0
        temp = n
        print(self.wr)
        while temp != 0:
            d = temp % 2
            num +=  d*(10**c)
            c +=1
            temp = temp // 2 # use double slash for int division
        return num


