from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
screen = Tk()
screen.geometry("500x500")
screen.title("Text Editor")
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]

)
    if not filepath:
        return
    txtbx.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txtbx.insert(END, text)
        input_file.close()  
def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],

)
    if not filepath:
        return

    with open(filepath, "w") as output_file:
        text =txtbx.get(1.0, END)
        output_file.write(text)
frm = Frame(master= screen, width= 100, height= 5000, bg= "#4A564B")
frm.place(x= 0, y= 0)
btn = Button(master= frm, text= "open!", fg= "#000000", bg= "#4A564B", command= open_file)
btn.pack()
butn = Button(master= frm, text= "save as", fg= "#000000", bg= "#4A564B", command= save_file)
butn.pack()
txtbx= Text(screen)
txtbx.place(x=50, y= 0)
screen.mainloop()