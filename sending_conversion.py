from conversion import conversion

class sending(conversion) :


    def ascii_conversion(self):

        binary = open("binary_" , 'w')

        text = self.new_file
        converted_alphabet = ""
        ascii = 0

        binary_string=""
        for i in text :
            ascii = ord(i)
            got = self.convert(ascii)
            binary_string = str(got)
            binary.write(binary_string)
            print(binary_string)
        print("Operation Successfull")


obj2 = sending()
obj2.calling_fun()
obj2.ascii_conversion()


