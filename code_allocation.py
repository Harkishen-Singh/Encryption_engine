import random


class Allocation:

    alpha = []

    def code_allocation(self):

        ch= ""
        val=""
        '''
        alpha is an array used for the storing of random values for alphabets
        in form of a secret code
        '''
        # where it is declared from 1 to 26 as reserved for the alphabets
        #  after which it can be used for teh storing for numeric codes

        for i in range(1,26) :
            a = [4]
            b = [4]
            for j in range(1,5):    # for the string part of the code
                temp=random.randrange(65,97)
                a.append(chr(temp))
            for j in range(1,5):
                ch = ch + a[j]
            for j in range(1,5):
                temp= random.randrange(0,9)
                b.append(str(temp))

            for j in range(1,5):
                val = val + b[j]
            self.alpha.append(ch+val)
            print(ch+val)
            ch=""
            val=""

    def file_saving(self):
        r= random.randrange(1,1000)
        x=random.randrange(1,1000)
        wx=chr(x)

        wr= str(r) +"encrypteCode"+wx+".txt"
        fw = open(wr, 'w')
        for i in range(0,self.alpha.__len__()):
            fw.write(self.alpha[i]+ "\n")
        fw.close()

obj = Allocation()
obj.code_allocation()
obj.file_saving()



