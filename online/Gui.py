from tkinter import Tk, END, Entry, Button, Listbox
from online.auto_complete import get_best_k_completions
from online.online_data import DataFiles

DataFiles.load_sentences()
DataFiles.load_sub_sentences()

root = Tk()
root.title('Auto Complete')


def clear():
    my_list.delete(0, END)
    entry.delete(0, END)


def search():
    input_ = entry.get()
    my_list.delete(0, END)

    if input_ == "":
        suggestions = list()
    else:
        suggestions = get_best_k_completions(input_)
    my_list.insert(END, '\n\n')

    if len(suggestions) == 0 and input_ != '':
        my_list.insert(END, f' Oops, there are no suggestions.')
        return

    elif len(suggestions) > 0:
        my_list.insert(END, f' Here are {len(suggestions)} suggestions:')

    my_list.insert(END, '\n\n')

    for i in range(len(suggestions)):
        my_list.insert(END, f'{i + 1}. {suggestions[i].get_completed()} ')
        my_list.insert(END, f' source_text: {suggestions[i].get_source_text()} '
                            f' offset: {suggestions[i].get_offset()} '
                            f' score: {suggestions[i].get_score()}')
        my_list.insert(END, '\n\n')


entry = Entry(width=88, bd=5)
button_clear = Button(root, text='Clear', width=8, bd=2, command=clear)
button_search = Button(root, text='Search', width=8, bd=2, command=search)

entry.grid(row=0, column=0)
button_search.grid(row=0, column=1)
button_clear.grid(row=0, column=2)

my_list = Listbox(root, width=88, height=20, bd=4)
my_list.grid(row=1, column=0)
root.mainloop()
