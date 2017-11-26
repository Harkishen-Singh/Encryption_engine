import random


alpha = []
al = []
dic = {}
wr = ""
trail = {}

class Encryption:

    def code_allocation2(self):

        ch= ""
        val= ""
        '''
        alpha is an array used for the storing of random values for alphabets
        in form of a secret code
        '''
        # where it is declared from 1 to 26 as reserved for the alphabets
        #  after which it can be used for teh storing for numeric codes

        for i in range(33, 3000) :
            a = [4]
            b = [4]
            for j in range(1,5):    # for the string part of the code
                temp=random.randrange(33, 3000)
                a.append(chr(temp))

            for j in range(1,5):
                ch = ch + a[j]

            for j in range(1,5):
                temp= random.randrange(0,9)
                b.append(str(temp))

            for j in range(1,5):
                val = val + b[j]

            alpha.append(ch+val)
            ch=""
            val=""

    r = random.randrange(1, 1000)

    def file_saving(self):
        x=random.randrange(1,1000)
        wx=chr(x)

        wr= str(self.r) +"_encryptCode_"+wx+".txt"  # use this variable to get the file of encrypted code
        fw = open(wr, 'w')
        for i in range(0,len(alpha)):
            fw.write(alpha[i]+ "\n")
        fw.close()


    def dic_alpha_assign(self):
        for i in range(33, 3000):
            al.append(chr(i))

    def dic_assign(self):

        for i in range(2967): # clever to check this..!!!!hehehehe
            trail[al[i]] = alpha[i]
            dic.update(trail)

    # till here, code works perfectly


    new_file = ""
    new_ch = ''
    name = ""
    def open_file(self):
        self.name = input("Enter the name of the file you want to encrypt ")
        self.name = self.name + ".txt"
        file = open(self.name, 'r')
        text = file.read()
        length = len(text)
        for i in range(length):
            ch = text[i]

            for j,k in dic.items():

                if ch == j :
                    self.new_file = self.new_file + k
                    break
        name_new = str(self.r) + "__encrypted_doc_" + self.name
        file_write = open(name_new, 'w')
        file_write.write(self.new_file + "\n")
        file_write.close()

class Continued(Encryption):

    digit =0
    ascii = 0
    def convert(self, ascii):

        num=0
        d=0
        c=0
        temp = ascii
        while temp != 0:
            d = temp % 2
            num +=  d*(10**c)
            c +=1
            temp = temp // 2 # use double slash for int division

        return num

    def ascii_conversion(self):
        ran2 = random.randrange(1,1000)
        ran2_str= str(ran2)

        binary = open(str(self.r)+"_binary_"+".txt" , 'w')

        text = self.new_file

        binary_string=""
        for i in text :
            ascii = ord(i)
            got = self.convert(ascii)
            binary_string = str(got)
            # sizing to the correct 8 length

            # calculating the length of the num
            temp2 = binary_string
            d=0
            len_binary = len(temp2)
            if len_binary != 16 :
                d = 16 - len_binary
                for i in range(d):
                    binary_string = "0" + binary_string
            print(binary_string)

            binary.write(binary_string)
        print("Operation Successfull")


obj2 = Continued()
obj2.code_allocation2()
obj2.file_saving()
obj2.dic_alpha_assign()
obj2.dic_assign()
obj2.open_file()
obj2.ascii_conversion()
