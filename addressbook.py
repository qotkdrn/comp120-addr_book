# File: addressbook.py
# Author: Alex Bae, Galen Forbes-Roberts
# Date: 2/26/21
# Description: This program keeps track of a list of addresses that can be edited by the user. 
# This address list can then be saved to other files. This program also provides the user
# with a GUI that can be used to navigate the address list. 


import tkinter as tk

class SomeError(Exception):
    pass

class Address:
    def __init__(self, name, street, city, state, zip):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip

    def __repr__(self):
        return 'Name: {} Street: {} City: {} State: {} zip: {}'.format(self.name, self.street, self.city, self.state, self.zip)

class AddressBook:
    def __init__(self):
        """ Constructor for AddressBook class """
        #Create list to store addresses
        self.address_list = []
        self.index = 0

        self.window = tk.Tk()  
        self.window.title("AddressBook") 
        #Create 1st Frame. This frame contains label and entry for name.
        frame1 = tk.Frame(self.window)
        frame1.grid(row = 1, column = 1)
        NameLabel = tk.Label(frame1, text = 'Name')
        NameLabel.grid(row = 1,column = 1)
        self.name = tk.StringVar()
        entryName = tk.Entry(frame1, textvariable = self.name, width = 50)
        entryName.grid(row = 1, column = 2)
        
        #Create 2nd Frame. This frame contains label and entry for street.
        frame2 = tk.Frame(self.window)
        frame2.grid(row = 2, column = 1)
        StreetLabel = tk.Label(frame2, text = 'Street')
        StreetLabel.grid(row = 1,column = 1)
        self.street = tk.StringVar()
        entryStreet = tk.Entry(frame2, textvariable = self.street, width = 49)
        entryStreet.grid(row = 1, column = 2) 
        
        #Create 3rd Frame. This frame contains the labels and entries for city, state, and zip.
        frame3 = tk.Frame(self.window)
        frame3.grid(row = 3, column = 1)
        CityLabel = tk.Label(frame3, text = 'City')
        CityLabel.grid(row = 1,column = 1)
        self.city = tk.StringVar()
        entryCity = tk.Entry(frame3, textvariable = self.city, width = 14)
        entryCity.grid(row = 1, column = 2)
        
        #State label and entry
        StateLabel = tk.Label(frame3, text = 'State')
        StateLabel.grid(row = 1,column = 3)
        self.state = tk.StringVar()
        entryState = tk.Entry(frame3, textvariable = self.state, width = 5)
        entryState.grid(row = 1, column = 4)
        
        #zip entry and label
        ZipLabel = tk.Label(frame3, text = 'ZIP')
        ZipLabel.grid(row = 1,column = 5)
        self.zip = tk.StringVar()
        entryZip = tk.Entry(frame3, textvariable = self.zip, width = 20)
        entryZip.grid(row = 1, column = 6)

        #Create 4th Frame. This frame contains the buttons for the 
        #necessary functions: add, delete, first, next, previous, last.
        frame4 = tk.Frame(self.window)
        frame4.grid(row = 4, column = 1)
        add_button = tk.Button(frame4, text = 'add', command = self.add_new_address)
        del_button = tk.Button(frame4, text = 'delete', command = self.delete_active_address)
        fir_button = tk.Button(frame4, text = 'first', command = self.display_first_address)
        next_button = tk.Button(frame4, text = 'next', command = self.display_next_address)
        prev_button = tk.Button(frame4, text = 'previous', command = self.display_previous_address)
        last_button = tk.Button(frame4, text = 'last', command = self.display_last_address)

        #Format buttons in frame 4
        add_button.grid(row = 4, column = 1)
        del_button.grid(row = 4, column = 2)
        fir_button.grid(row = 4, column = 3)
        next_button.grid(row = 4, column = 4)
        prev_button.grid(row = 4, column = 5)
        last_button.grid(row = 4, column = 6)

        #Create 5th Frame. Create label and entry for the filename. 
        #This frame will also contain buttons for the load, save, and quit functions
        frame5 = tk.Frame(self.window)
        frame5.grid(row = 5, column = 1)
        FilenameLabel = tk.Label(frame5, text = 'Filename')
        FilenameLabel.grid(row = 1, column = 1)
        self.filename = tk.StringVar()
        entryFilename = tk.Entry(frame5, textvariable = self.filename, width = 25)
        entryFilename.grid(row = 1, column = 2)

        load_file_button = tk.Button(frame5, text = 'Load File', command = self.loaddata)
        save_to_file_button = tk.Button(frame5, text = 'Save to File', command = self.save_to_file)
        quit_button = tk.Button(frame5, text = 'Quit', command = self.quit)

        load_file_button.grid(row = 1, column = 3)
        save_to_file_button.grid(row = 1, column = 4)
        quit_button.grid(row = 1, column = 5)

        #Start Event Loop
        self.window.mainloop()

    #Functions for all buttons on GUI
    #Take entries for name, street, city, state, and zip and store them in the address list.
    def add_new_address(self):
        address_info = Address(self.name.get(), self.street.get(), self.city.get(), 
                                self.state.get(), self.zip.get()) 
        self.address_list.append(address_info) 
        self.index = len(self.address_list)-1 

    #Delete the address of current index
    def delete_active_address(self):
        remove_item = self.address_list[self.index]
        self.address_list.remove(remove_item)
        self.index = 0
        self.set_address()

    #display the first address
    def display_first_address(self):
        self.index  = 0        
        self.set_address()

    #display next address in address list
    def display_next_address(self):
        if self.index<len(self.address_list)-1:
            self.index+=1
            self.set_address()

    #display previous address in address list
    def display_previous_address(self):
        if self.index > 0:
            self.index -= 1
            self.set_address()

    #display last address of address list
    def display_last_address(self):
        if len(self.address_list) > 0:
            self.index = len(self.address_list) - 1
        else:
            self.index = 0
        self.set_address()
        
    #we set all address information to whatever index we need it to be.
    #print current index whenever function is called to keep track of current index
    def set_address(self):
        print(self.index)
        if len(self.address_list) > 0:
            self.name.set(self.address_list[self.index].name)
            self.street.set(self.address_list[self.index].street)
            self.city.set(self.address_list[self.index].city)
            self.state.set(self.address_list[self.index].state)
            self.zip.set(self.address_list[self.index].zip)  

    #add all existing addresses in file to address list
    def loaddata(self):
        try:
            f=open(self.filename.get().strip())
            self.address_list = []
            lines = [x.strip() for x in f]
            i = 0
            while i < len(lines):
                a = Address(lines[i], lines[i+1], lines[i+2], lines[i+3], lines[i+4])
                self.address_list.append(a)
                i+=5
            self.set_address()
        except OSError:
            print('Invalid filename!')

    #save address list to file
    def save_to_file(self):
        f = open(self.filename.get(),'w')
        for i in range(len(self.address_list)):    
            f.write(self.address_list[i].name+'\n')
            f.write(self.address_list[i].street+'\n')
            f.write(self.address_list[i].city+'\n')
            f.write(self.address_list[i].state+'\n')
            f.write(self.address_list[i].zip+'\n')
        f.close()
    
    def quit(self):
        #terminate program
        self.window.destroy()

if __name__ == "__main__":
    #Create GUI
    AddressBook()