import tkinter as tk


def open_window():
    list_of_tops.append(tk.Toplevel(root))
    list_of_tops[-1].geometry("100x100")


def destroy_all():
    for top_window in list_of_tops:
        top_window.destroy()

root = tk.Tk()
root.geometry("500x500")
list_of_tops = [] # list to store any toplevel window.
tk.Button(root, text="open", command=open_window).pack(side=tk.TOP)
tk.Button(root, text="destroy all", command=destroy_all).pack(side=tk.BOTTOM)
root.mainloop()