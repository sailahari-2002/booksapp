from utils import database
choice=input("""enter a choice
a =add a book
l=get books from list
r=making a book as read
d=deleting a book
q=quit""")
while(choice!='q'):
    if(choice=='a'):
        name=input("enter book name")
        author=input("enter author name")
        database.add_book(name,author)
    elif(choice=='l'):
         l=database.get_books()
         for i in l:
             print(i)
    elif(choice=='r'):
        name=input("enter a book name")
        database.read_book(name)
    elif(choice=='d'):
        nmae=input("enter a book name")
        database.delete_book(name)
    else:
        print("invalid key.press a new key.")
    choice=input("""enter a choice
a =add a book
l=get books from list
r=making a book as read
d=deleting a book
q=quit""")


