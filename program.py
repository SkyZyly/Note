from tkinter import *
from PIL import ImageTk,Image
from tkinter import font
from tkinter import scrolledtext
import tkinter.messagebox
from tkinter.filedialog import *

root=Tk()
root.title("สมุดจดบันทึก")
root.iconbitmap("icon/note.ico")
root.geometry("600x600")
root.resizable(0,0)
root.config(bg="#FAEBD7")

def changeFont(e):
    if fontStyle.get()=="none":
        myfont=(fontFamily.get(),fontSize.get())
    else :
        myfont=(fontFamily.get(),fontSize.get(),fontStyle.get())

    textArea.config(font=myfont)

def newNote():
    confirm=tkinter.messagebox.askquestion("คำเตือน","ต้องการสร้างหน้าใหม่หรือไม่")
    if confirm=="yes":
        textArea.delete("1.0",END)

def closeNote():
    confirm=tkinter.messagebox.askquestion("คำเตือน","ต้องการปิดโปรแกรมหรือไม่")
    if confirm=="yes":
        root.destroy()

def saveNote():
    myFile=asksaveasfilename(initialdir="./",title="บันทึกโน๊ต",filetypes=(("Text File","*.txt"),("All File","*")))
    with open(myFile,"w",encoding="utf8") as file:
        file.write(fontFamily.get()+"\n")
        file.write(str(fontSize.get())+"\n")
        file.write(fontStyle.get()+"\n")
        file.write(textArea.get("1.0",END))

def openNote():
    myFile=askopenfilename(initialdir="./",title="เปิดโน๊ต",filetypes=(("Text File","*.txt"),("All File","*")))
    with open(myFile,"r",encoding="utf8") as file:
        textArea.delete("1.0",END)
        fontFamily.set(file.readline().strip())
        fontSize.set(file.readline().strip())
        fontStyle.set(file.readline().strip())
        content=file.read()
        textArea.insert("1.0",content)


menu_color="#FFDAB9"
text_color="white"

menuFrame=Frame(root,bg=menu_color)
textFrame = Frame(root,bg=text_color)
menuFrame.pack(padx=5,pady=5)
textFrame.pack(padx=5,pady=5)

new_img=ImageTk.PhotoImage(Image.open("icon/new.png"))
btnNew=Button(menuFrame,image=new_img,command=newNote)
btnNew.grid(row=0,column=0,padx=5,pady=5)

open_img=ImageTk.PhotoImage(Image.open("icon/open.png"))
btnOpen=Button(menuFrame,image=open_img,command=openNote)
btnOpen.grid(row=0,column=1,padx=5,pady=5)

save_img=ImageTk.PhotoImage(Image.open("icon/save.png"))
btnSave=Button(menuFrame,image=save_img,command=saveNote)
btnSave.grid(row=0,column=2,padx=5,pady=5)

quit_img = ImageTk.PhotoImage(Image.open("icon/quit.png"))
btnQuit=Button(menuFrame,image=quit_img,command=closeNote)
btnQuit.grid(row=0,column=3,padx=5,pady=5)

allFonts=font.families()
fontFamily=StringVar()
fontOption=OptionMenu(menuFrame,fontFamily,*allFonts,command=changeFont)
fontFamily.set("Arial")
fontOption.config(width=22)
fontOption.grid(row=0,column=4,padx=5,pady=5)

sizes=[8,12,16,18,24,36,42,50]
fontSize=IntVar()
sizeOption=OptionMenu(menuFrame,fontSize,*sizes,command=changeFont)
fontSize.set(12)
sizeOption.config(width=5)
sizeOption.grid(row=0,column=5,padx=5,pady=5)

styles=["none","bold","italic"]
fontStyle=StringVar()
styleOption=OptionMenu(menuFrame,fontStyle,*styles,command=changeFont)
fontStyle.set("none")
styleOption.config(width=10)
styleOption.grid(row=0,column=6,padx=5,pady=5)

myfont=(fontFamily.get(),fontSize.get())
textArea=scrolledtext.ScrolledText(textFrame,bg=text_color,font=myfont,width=1000,height=1000)
textArea.pack()


root.mainloop()