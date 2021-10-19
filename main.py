import tkinter as tk
from tkinter import scrolledtext


main = tk.Tk()
main.resizable(False,False)
main.title('TransLang')
main.geometry('700x620')
main.iconbitmap(r"D:\Translang\icon-modified.ico")

tv = tk.StringVar()
tv1 = tk.StringVar()
tv2 = tk.StringVar()

lab = tk.Label(main,text='From:',font=("Arial",20))
lab.place(x=15,y=300)


txt = scrolledtext.ScrolledText(main,font=('Arial',15),height=10,width=50,padx=6,pady=5)
txt.place(x=60,y=23)

txt.insert(1.8,'Enter text you want to translate')
ent = tk.Entry(main,font=('Arial',12),textvariable=tv)
ent.place(x=130,y=310,height=25)

lab1 = tk.Label(main,text='TO:',font=('Arial',20))
lab1.place(x=390,y=300)

ent1 = tk.Entry(main,font=('Arial',12),textvariable=tv1)
ent1.place(x=480,y=310,height=25)

file = None

def trans():
    import googletrans

    t = googletrans.Translator()
    d = str(txt.get('1.0','end-1c'))
    s = t.translate(d,src=ent.get(),dest=ent1.get())
    txt1['state'] = 'normal'
    txt1.delete(1.0, tk.END)
    txt1.insert(1.0,s.text)
    txt1['state'] = 'disabled'

def save():
    import tkinter.filedialog as fd
    global file

    if file == None:
        file = fd.asksaveasfilename(initialfile='transcript.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:

            # Save as a new file
            f = open(file, "w")
            f.write(txt1.get(1.0, tk.END))
            f.close()

    else:
        # Save the file
        f = open(file, "w")
        f.write(txt1.get(1.0, tk.END))
        f.close()

b1 = tk.Button(main, text='Translate', command=trans, font=('Arial', 15),padx=4,pady=5)
b1.place(x=250, y=350, height=50, width=200)

b2 = tk.Button(main,text='Export',command=save,font=('Arial',10),padx=6,pady=7)
b2.place(x=610,y=350)

txt1 = scrolledtext.ScrolledText(main,font=('Arial',15),height=7,width=50,padx=6,pady=5)
txt1.place(x=60,y=410)
txt1.insert(1.0,'Result shown here')

txt1['state'] = 'disabled'

main.mainloop()
