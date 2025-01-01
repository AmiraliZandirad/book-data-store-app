from tkinter import*
import database

def clear_list():
    list1.delete(0,END)

def fill_list(Books):
    for book in Books:
        list1.insert(END, book)

window = Tk()
#-------------------- setting -----------------
window.geometry('400x200')
window.title('Book store')
window.resizable(width=False , height=False)
color = 'gainsboro'
window.configure(bg=color)

#-------------------- lable -----------------
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="Isbn")
l4.grid(row=1, column=2)

#-------------------- Entry -----------------
title_text = StringVar()
q1 = Entry(window, textvariable=title_text)
q1.grid(row=0, column=1)

author_text = StringVar()
q2 = Entry(window, textvariable=author_text)
q2.grid(row=0, column=3)

year_text = StringVar()
q3 = Entry(window, textvariable=year_text)
q3.grid(row=1, column=1)

isbn_text = StringVar()
q4 = Entry(window, textvariable=isbn_text)
q4.grid(row=1, column=3)

list1 = Listbox(window, width=35, height=6)
list1.grid(row=2 , column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

#-------------------- Button -----------------

def get_selected_row(event):
    global selected_book
    if len(list1.curselection())> 0:
        index= list1.curselection()[0]
        selected_book = list1.get(index)
        #tilte
        q1.delete(0, END)
        q1.insert(END, selected_book[1])
        #author
        q2.delete(0, END)
        q2.insert(END, selected_book[2])
        #year
        q3.delete(0, END)
        q3.insert(END, selected_book[3])
        #isbn
        q4.delete(0, END)
        q4.insert(END, selected_book[4])
        
list1.bind("<<ListboxSelect>>", get_selected_row)


def view_command():
    clear_list()
    books = database.view()
    fill_list(books)

d1 = Button(window, text="View all", width=12, command=lambda: view_command())
d1.grid(row=2, column=3)


def search_command():
    clear_list()
    books = database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    fill_list(books)

d2 = Button(window, text="Search Entry", width=12, command=lambda: search_command())
d2.grid(row=3, column=3)


def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

d3 = Button(window, text="Add Entry", width=12, command=lambda: add_command())
d3.grid(row=4, column=3)


def update_command():
    database.update(selected_book[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

d4 = Button(window, text="Update Entry", width=12, command=lambda: update_command())
d4.grid(row=5, column=3)


def delete_command():
    database.delete(selected_book[0])
    view_command()

d5 = Button(window, text="Delete Selected", width=12, command=lambda: delete_command())
d5.grid(row=6, column=3)

d6 = Button(window, text="Close", width=12, command=lambda: window.destroy() )
d6.grid(row=7, column=3)

window.mainloop()
