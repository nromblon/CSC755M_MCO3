from tkinter import *
from tkinter import filedialog
from CSC755M_MCO3.com.imgcompress.image_compression import *
from PIL import Image, ImageTk

class Global:
    img = Image.open("test.jpg")
    qtree = quadtree(img)

class GUI:

    def __init__(self):

        root = Tk()

        main_frame = Frame(root)
        main_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # img frame init
        img_frame = Frame(main_frame)
        img_frame.pack(side=LEFT, fill=BOTH, anchor=CENTER, expand=True)
        img_frame.config(width=300,height=300,padx=20,pady=20)
        # img frame components
        img_label = Label(img_frame)
        img_label.pack(side=TOP)

        #ctrl frame init
        ctrl_frame = Frame(main_frame)
        ctrl_frame.pack(side=RIGHT, fill=BOTH, anchor=CENTER, expand=True)
        ctrl_frame.config(bd=5,relief=RIDGE,width=150,height=256,padx=20,pady=15)
        #ctrl frame components
        file_label = Label(ctrl_frame, text="Choose image to open: ")
        file_label.pack(side=TOP, fill=X)
        open_btn = Button(ctrl_frame, text="Browse")
        open_btn.pack(side=TOP)
        selfile_label = Label(ctrl_frame)
        selfile_label.pack(side=TOP)

        depth_label = Label(ctrl_frame, text="Depth: ")
        depth_label.pack(side=TOP,fill=X)
        depth_scale = Scale(ctrl_frame, from_=0, to=0, orient=HORIZONTAL)
        depth_scale.pack(side=TOP)
        open_btn.bind("<Button-1>",lambda b: open_file(img_label,selfile_label,depth_scale))
        compress_btn = Button(ctrl_frame,text="Compress")
        compress_btn.pack(side=TOP)
        compress_btn.bind("<Button-1>",lambda a: compress(depth_scale))

        root.mainloop()


#util functions
def open_file(ilabel,label,scale):
    file_path = filedialog.askopenfilename(initialdir="\Python\CSC755M_MCO3\com\imgcompress",filetypes=[("Image Files (*.jpg,*.jpeg,*.bmp)", "*.jpg;*.jpeg;*.bmp")])
    label.config(text=file_path)
    img = Image.open(file_path)

    photo = ImageTk.PhotoImage(img)
    ilabel.config(image = photo, width = 256, height = 256)
    ilabel.photo = photo


    Global.qtree = quadtree(img)
    scale.config(to=Global.qtree.depth)

def compress(scale):
    level = scale.get()
    Global.qtree.disp(level)

gui = GUI()