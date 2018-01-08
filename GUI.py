from code_allocation_github_check import Encryption,dic,alpha,wr,trail
from gi.repository import Gtk

class GUI(Encryption, Gtk.Window):
    def window_creation(self):
        Gtk.Window.__init__(self, title='Encryption Engine')
        self.set_border_width(10)
        self.set_default_size(500,500)

        self.box= Gtk.Box(orientation= Gtk.Orientation.VERTICAL, spacing = 10)
        self.add(self.box)


        #fixed = Gtk.Fixed(label='Enter the name of the file to be encrypted here', limit= 0)
        self.input_user = Gtk.Entry()
        self.button = Gtk.Button(label = 'Submit')
        self.button.connect('clicked' , self.calling_clicked_function)
        #self.button.connect('clicked' , Gtk.Widget.destroy)
        self.button.connect('clicked', self.showing_results_in_window)
        self.input_user.set_text('Enter the name of the file to be encrypted here')
        #self.input_user.connect('clicked', self.calling_clicked_function)
        self.box.add(self.input_user)
        self.box.add(self.button)

        self.label3 = Gtk.Label()
        self.label3.set_label('The encrypted code has been stored in the file created is in the same directory')
        self.box.add(self.label3)
        self.label = Gtk.Label()
        #self.label.set_label('The encrypted code of the file is given below' )
        #self.box.add(self.label)

    def calling_clicked_function(self, widget):
        self.name = self.input_user.get_text()

        self.name = self.name  + ".txt"
        file = open(self.name, 'r')
        text = file.read()
        length = len(text)
        for i in range(length):
            ch = text[i]

            for j,k in dic.items():

                if ch == j :
                    self.new_file = self.new_file + k + " "
                    break
        self.name_new = str(self.r) + "__encrypted_doc_" + self.name
        filename = self.name_new
        file_write = open(self.name_new, 'w')
        new_file2 = self.new_file
        file_write.write(self.new_file + "\n")
        file_write.close()

    def showing_results_in_window(self, widget):
        #Gtk.Window.__init__(self, title='Encrypted Code of the Entered File')
        win2 = Gtk.Window()
        win2.set_title('Encrypted')
        win2.set_border_width(10)
        win2.set_default_size(500,500)
        b = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 10)
        win2.add(b)

        print('accessed showing_results_in_window function')
        print('\n value of '+self.name_new)
        laa = Gtk.Label()
        laa.set_label("The Encrypted code of the file " + self.name_new + " is below :")
        b.add(laa)
        laa2 = Gtk.Label()
        laa2.set_label(self.new_file)
        print('\n the encrypted text is \n\n'+ self.new_file)
        b.add(laa2)
        close = Gtk.Button(label='Close')
        close.connect('clicked', Gtk.main_quit)
        b.add(close)
        win2.show_all()
        win2.connect('delete-event', Gtk.main_quit)


obj2 = GUI()
obj2.code_allocation2()
obj2.file_saving()
obj2.dic_alpha_assign()
obj2.dic_assign()
#  obj2.open_file()
obj2.window_creation()
obj2.show_all()
obj2.connect('delete-event', Gtk.main_quit)
Gtk.main()
