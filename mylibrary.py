"""
A fixed file (json.books) is created and used for storing and editing books in 'my library'
functionaliy : It display books
               adds books
               select(remove) books
A separate fixed file (usr.json) is created to store user's name and list of books borrowed from library
syntax for usr file
[
    {
     "name" = "usr 1"
     "books" = [.....]
     }

    {
     "name" = "usr 2"
     "books" = [.....]
    }
    .....
]


"""
import json
import os
import usrtrack

def create_file():

    bookdict = {"MERCHANT OF VENICE":"BY SHAKESPEAR",
            "LOST IN WOODS":"BY ROBERT FROST"}
    with open("books.json","w") as f:
        json.dump(bookdict,f,indent=4)

def create_usrfile():
    with open("usr.json","w") as f:
        json.dump([],f,indent=4)

list_dir = os.listdir(os.getcwd())
print(list_dir)
if "books.json" not in list_dir:
    create_file()

if "usr.json" not in list_dir:
    create_usrfile()

usr_name = input("Enter your name : ")
usrdict = usrtrack.get_dict(usr_name)


if not usrdict:
    usrdict=usrtrack.create_dict(usr_name)





def select_book():
    with open("books.json","r") as f:
        bookdict= json.load(f)

    keys =list( bookdict.keys())
    for i,key in enumerate(keys):
        print(i+1,key,bookdict[key])
    if bookdict == {}:
        print("No book available in library ")
    else:
        b_select = int(input("choose a book : "))
        print(f"you have selected {keys[b_select-1]}")

        bk = usrtrack.concatx(keys[b_select-1],bookdict[keys[b_select-1]])
        del  bookdict[keys[b_select-1]]
        with open("books.json", "w") as f:
            json.dump(bookdict, f,indent=4)
        ts = usrtrack.timenow()
        usrtrack.add_to_dict(bk,ts,usr_name)



def display_book():

    with open("books.json","r") as f:
        bookdict = json.load(f)
        print(bookdict)

def add_book(key,value):
    with open("books.json", "r") as f:
        bookdict = json.load(f)
    bookdict.update({key:value})
    with open("books.json","w") as f:
        json.dump(bookdict,f,indent=4)

usrinp = int(input("choose "
                   "1:TO DISPLAY BOOKS OF LIBRARY"
                   "2:TO DONATE BOOK TO LIBRARY"
                   "3:TO SELECT BOOKS FROM LIBRARY "                   
                   "4.TO CHECK YOUR LIST OF BOOKS "
                   "5. TO RETURN BOOK TO LIBRARY "
                   "6:TO EXIT : "
                    ))

while usrinp != 6:

    if usrinp == 1:
        display_book()

    elif usrinp == 2:
        x = input("enter the name of the book : ")
        y = input("enter the name of the author : ")
        add_book(x,y)

    elif usrinp == 3:
        select_book()


    elif usrinp == 4:
        usrtrack.show_dict(usr_name)


    elif usrinp == 5:


        usrtrack.return_to_lib(usr_name)

    elif usrinp == 6:
        break



    else:
        print("you have entered wrong number")
        break

    usrinp = int(input("choose "
                       "1:TO DISPLAY BOOKS OF LIBRARY "
                       "2:TO DONATE BOOK TO LIBRARY "
                       "3:TO SELECT BOOKS FROM LIBRARY "                       
                       "4.TO CHECK YOUR LIST OF BOOKS "
                       "5. TO RETURN BOOK TO LIBRARY "
                       "6:TO EXIT : "
                       ))