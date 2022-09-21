'''
[
 {
  'NAME' : 'USRNAME'
  'Books': {
            'book_name': time_now()
            'book_name2': time_now()
            .......
            }




 }
]
'''




import json
import time
from datetime import datetime

def timenow():
    return datetime.now().timestamp()


def get_date_from_ts(ts):
    return f"{datetime.fromtimestamp(ts)}".split(".")[0]


def create_dict(name):
    with open("usr.json","r") as f:
        l = json.load(f)

    usrdict = {"Name":name,
               "Books":{}
                 }
    l.append(usrdict)
    with open("usr.json","w") as f:
        json.dump(l,f,indent=4)
    return usrdict


def show_dict(name):
    usrdict = get_dict(name)

    inner_dict = usrdict["Books"]

    keys = list(inner_dict.keys())
    for i, key in enumerate(keys):
        bname,author = get_val(key)

        print(f"{i + 1}, {bname} - {author} ---> {get_date_from_ts(inner_dict[key])}")
    if inner_dict == {}:
        print("No book available in dictinary ")







    pass

def add_to_dict(bk,ts,username):

    usrdict = get_dict(username)
    if usrdict:
        name = usrdict["Name"]

        inner_dict = usrdict["Books"]

        inner_dict.update({bk:ts})
        ###usrdict.update
        set_dict(name,inner_dict)
    print("book borrowed from library")




def return_to_lib(username):
    bname,author = None,None
    usrdict = get_dict(username)
    if usrdict:
        name = usrdict["Name"]

        inner_dict = usrdict["Books"]
    keys = list(inner_dict.keys())
    for i, key in enumerate(keys):
        bname,author = get_val(key)
        print(f"{i + 1}, {bname} - {author} ---> {get_date_from_ts(inner_dict[key])}")
    if inner_dict == {}:
        print("No book available in dictionary ")
    else:
        b_select = int(input("choose a book : "))
        bname,author = get_val(keys[b_select - 1])
        print(f"you have selected {bname} - {author}")
        bname,author=get_val(keys[b_select - 1])
        del inner_dict[keys[b_select - 1]]
        set_dict(name,inner_dict)
        with open("books.json","r")as f:
            bd = json.load(f)
        bd[bname]=author
        with open("books.json","w") as f:
            json.dump(bd,f,indent=4)
        print("book returned to library")

def get_dict(name):
    with open("usr.json", "r") as f:
        l = json.load(f)
    for i in l:
        if name == i["Name"]:
            return i




def set_dict(name,inner_dict):
    with open("usr.json","r") as f:
        l = json.load(f)
    dupdict = get_dict(name)
    l.remove(dupdict)

    usrdict = {"Name": name,
               "Books": inner_dict
               }
    l.append(usrdict)
    with open("usr.json", "w") as f:
        json.dump(l, f,indent=4)

def get_val(st):
    return st.split("///")

def concatx(bname,author):
    return f"{bname}///{author}"
