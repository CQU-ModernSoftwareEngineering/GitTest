import tkinter as tk
import tkinter.messagebox
import re

root = tk.Tk()
root.minsize(342, 388)  # 窗口大小300*400
root.resizable(0, 0)
root.config(background='#226767')
root.title('Calculator')
pixelVirtual = tk.PhotoImage(width=1, height=1)

# 第一行
btn_sin = tkinter.Button(root,
                         text="sin",
                         font=('Arial', 12),
                         bg=('#E1E1E1'),
                         fg=('#000000'),
                         bd=0.5,
                         image=pixelVirtual,
                         width=75,
                         height=50,
                         compound="c",
                         command=lambda x='sin': buttonClick1(x)
                         )
btn_sin.place(x=9, y=87, width=75, height=50)
btn_cos = tkinter.Button(root,
                         text="cos",
                         font=('Arial', 12),
                         bg=('#E1E1E1'),
                         fg=('#000000'),
                         bd=0.5,
                         image=pixelVirtual,
                         width=75,
                         height=50,
                         compound="c",
                         command=lambda x='cos': buttonClick1(x)
                         )
btn_cos.place(x=92, y=87, width=75, height=50)
btn_arctan = tkinter.Button(root,
                            text="arctan",
                            font=('Arial', 12),
                            bg=('#E1E1E1'),
                            fg=('#000000'),
                            bd=0.5,
                            image=pixelVirtual,
                            width=75,
                            height=50,
                            compound="c",
                            command=lambda x='sin': buttonClick1(x)
                            )
btn_arctan.place(x=175, y=87, width=75, height=50)
btn_arcsin = tkinter.Button(root,
                            text="arcsin",
                            font=('Arial', 12),
                            bg=('#E1E1E1'),
                            fg=('#000000'),
                            bd=0.5,
                            image=pixelVirtual,
                            width=75,
                            height=50,
                            compound="c",
                            command=lambda x='arcsin': buttonClick1(x)
                            )
btn_arcsin.place(x=258, y=87, width=75, height=50)

# 第二行
btn_7 = tkinter.Button(root,
                       text="7",
                       font=('Arial', 12),
                       bg=('#E1E1E1'),
                       fg=('#000000'),
                       bd=0.5,
                       image=pixelVirtual,
                       width=75,
                       height=50,
                       compound="c",
                       command=lambda x='sin': buttonClick1(x)
                       )
btn_7.place(x=9, y=144, width=75, height=50)
btn_8 = tkinter.Button(root,
                       text="8",
                       font=('Arial', 12),
                       bg=('#E1E1E1'),
                       fg=('#000000'),
                       bd=0.5,
                       image=pixelVirtual,
                       width=75,
                       height=50,
                       compound="c",
                       command=lambda x='cos': buttonClick1(x)
                       )
btn_8.place(x=92, y=144, width=75, height=50)
btn_9 = tkinter.Button(root,
                       text="9",
                       font=('Arial', 12),
                       bg=('#E1E1E1'),
                       fg=('#000000'),
                       bd=0.5,
                       image=pixelVirtual,
                       width=75,
                       height=50,
                       compound="c",
                       command=lambda x='sin': buttonClick1(x)
                       )
btn_9.place(x=175, y=144, width=75, height=50)
btn_C = tkinter.Button(root,
                       text="C",
                       font=('Arial', 12),
                       bg=('#E1E1E1'),
                       fg=('#000000'),
                       bd=0.5,
                       image=pixelVirtual,
                       width=75,
                       height=50,
                       compound="c",
                       command=lambda x='arcsin': buttonClick1(x)
                       )
btn_C.place(x=258, y=144, width=75, height=50)

contentVar = tkinter.StringVar(root, '')
contentEntry = tkinter.Entry(
    root, textvariable=contentVar, state='readonly', font=("Arial", 12))
contentEntry.place(x=9, y=10, width=324, height=70)

# 第三行
btn_4 = tkinter.Button(root,
                       text="4",
                       font=('Arial', 12),
                       bg=('#E1E1E1'),
                       fg=('#000000'),
                       bd=0.5,
                       image=pixelVirtual,
                       width=75,
                       height=50,
                       compound="c",
                       command=lambda x='sin': buttonClick1(x)
                       )
btn_4.place(x=9, y=201, width=75, height=50)
btn_5 = tkinter.Button(root,
                       text="5",
                       font=('Arial', 12),
                       bg=('#E1E1E1'),
                       fg=('#000000'),
                       bd=0.5,
                       image=pixelVirtual,
                       width=75,
                       height=50,
                       compound="c",
                       command=lambda x='cos': buttonClick1(x)
                       )
btn_5.place(x=92, y=201, width=75, height=50)
btn_6 = tkinter.Button(root,
                       text="6",
                       font=('Arial', 12),
                       bg=('#E1E1E1'),
                       fg=('#000000'),
                       bd=0.5,
                       image=pixelVirtual,
                       width=75,
                       height=50,
                       compound="c",
                       command=lambda x='sin': buttonClick1(x)
                       )
btn_6.place(x=175, y=201, width=75, height=50)
btn_rad = tkinter.Button(root,
                         text="R/°",
                         font=('Arial', 12),
                         bg=('#E1E1E1'),
                         fg=('#000000'),
                         bd=0.5,
                         image=pixelVirtual,
                         width=75,
                         height=50,
                         compound="c",
                         command=lambda x='arcsin': buttonClick1(x)
                         )
btn_rad.place(x=258, y=201, width=75, height=50)

# 第四行
btn_1= tkinter.Button(root,
                         text="1",
                         font=('Arial', 12),
                         bg=('#E1E1E1'),
                         fg=('#000000'),
                         bd=0.5,
                         image=pixelVirtual,
                         width=75,
                         height=50,
                         compound="c",
                         command=lambda x='sin': buttonClick1(x)
                         )
btn_1.place(x=9, y=258, width=75, height=50)
btn_2 = tkinter.Button(root,
                         text="2",
                         font=('Arial', 12),
                         bg=('#E1E1E1'),
                         fg=('#000000'),
                         bd=0.5,
                         image=pixelVirtual,
                         width=75,
                         height=50,
                         compound="c",
                         command=lambda x='cos': buttonClick1(x)
                         )
btn_2.place(x=92, y=258, width=75, height=50)
btn_3= tkinter.Button(root,
                            text="3",
                            font=('Arial', 12),
                            bg=('#E1E1E1'),
                            fg=('#000000'),
                            bd=0.5,
                            image=pixelVirtual,
                            width=75,
                            height=50,
                            compound="c",
                            command=lambda x='sin': buttonClick1(x)
                            )
btn_3.place(x=175, y=258, width=75, height=50)
btn_del = tkinter.Button(root,
                            text="del",
                            font=('Arial', 12),
                            bg=('#E1E1E1'),
                            fg=('#000000'),
                            bd=0.5,
                            image=pixelVirtual,
                            width=75,
                            height=110,
                            compound="c",
                            command=lambda x='arcsin': buttonClick1(x)
                            )
btn_del.place(x=258, y=258, width=75, height=107)

# 第五行
btn_sign= tkinter.Button(root,
                         text="+/-",
                         font=('Arial', 12),
                         bg=('#E1E1E1'),
                         fg=('#000000'),
                         bd=0.5,
                         image=pixelVirtual,
                         width=75,
                         height=50,
                         compound="c",
                         command=lambda x='sin': buttonClick1(x)
                         )
btn_sign.place(x=9, y=315, width=75, height=50)
btn_0 = tkinter.Button(root,
                         text="0",
                         font=('Arial', 12),
                         bg=('#E1E1E1'),
                         fg=('#000000'),
                         bd=0.5,
                         image=pixelVirtual,
                         width=75,
                         height=50,
                         compound="c",
                         command=lambda x='cos': buttonClick1(x)
                         )
btn_0.place(x=92, y=315, width=75, height=50)
btn_dot= tkinter.Button(root,
                            text=".",
                            font=('Arial', 12),
                            bg=('#E1E1E1'),
                            fg=('#000000'),
                            bd=0.5,
                            image=pixelVirtual,
                            width=75,
                            height=50,
                            compound="c",
                            command=lambda x='sin': buttonClick1(x)
                            )
btn_dot.place(x=175, y=315, width=75, height=50)

def buttonClick1(btn):
    pass


root.mainloop()

'''
text='sin',
                         font=('Arial', 12),
                         bg=('#E1E1E1'),
                         fg=('#000000'),
                         bd=0.5,
'''
