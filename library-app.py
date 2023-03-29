class Library:
    def __init__(self,bookList,libName,lenders,donors):
        self.bookList = bookList
        self.libName = libName
        self.lenders = lenders
        self.donors = donors
    def books(self):
        return self.bookList
    def lend(self,bookName,name):
        if bookName in self.bookList:
            self.bookList.remove(bookName)
            self.lenders.update({name.lower():bookName})
            print('Book lended! Return within a week!')
        else:
            print('No such book!')
        
            
    def returnB(self,name):
        if name.lower() in self.lenders.keys():#search in keys
            self.bookList.append(self.lenders[name.lower()])#name is the key and the value is book's name
            self.lenders.pop(name.lower())
        else:
            print('This name doesn\'t exist,put a correct name')
    def donate(self,name,newBook):
        print('Thank you for donation!')
        self.bookList.append(newBook)
        self.donors.update({name.lower():newBook})        
            
lib = Library(['passion','programming','yes or no'],'Hope',{},{})


if __name__ == '__main__':
    while True:
        print('This is the',lib.libName,'library !')
        op = int(input('Enter what do you want to do:\n1: See the book list\n2: Rent a book\n3: Donate a book\n4: Return a book\n'))
        if op == 1:
            print(lib.books())
        elif op == 2:
            name = input('Enter your name: ')
            book = input('Enter the book\'s name:')
            lib.lend(book, name)
        elif op == 3:
            name = input('Enter your name: ')
            book = input('Enter the book\'s name:')
            lib.donate(name,book)
        elif op == 4:
            if len(lib.lenders) > 0:
                # print(lib.lenders.keys())
                print(lib.lenders)
                name = input('Please give me your name: ')
                lib.returnB(name)
            else:
                print('No book borrowers currently!')
        else:
            break
