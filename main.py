import tkinter as tk
import tkinter.font as tkFont
import tkinter.filedialog as fd
import os
import shutil
from PIL import Image
from pathlib import Path


class App:
    def __init__(self, root):
        self.images = []
        self.extentions = ['png', 'jpeg', 'webp', 'jpg']
        self.exportPath = ''

        #setting title
        root.title("Image Converter")
        root.configure(bg="white")

        #setting window size
        width = 600
        height = 300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        webpBtn = tk.Button(root)
        webpBtn["borderwidth"] = "0px"
        ft = tkFont.Font(family='Blinker ', size=13)
        webpBtn["highlightbackground"] = "#ff5722"
        webpBtn["font"] = ft
        webpBtn["fg"] = "#1b1b1b"
        webpBtn["justify"] = "center"
        webpBtn["text"] = "CONVERT TO WEBP"
        webpBtn["command"] = self.webpBtn_command
        webpBtn.place(x=390, y=120, width=180, height=45)

        GLabel_942 = tk.Label(root)
        GLabel_942["anchor"] = "center"
        ft = tkFont.Font(family='Blinker ', size=20)
        GLabel_942['highlightbackground']= "white"
        GLabel_942["font"] = ft
        GLabel_942["fg"] = "#1b1b1b"
        GLabel_942["justify"] = "center"
        GLabel_942["text"] = "Image Converter"
        GLabel_942.place(x=210, y=0, width=180, height=50)
        GLabel_942.config(background="white")

        GLabel_658 = tk.Label(root)
        ft = tkFont.Font(family='Blinker ', size=10)
        GLabel_658['highlightbackground']= "white"
        GLabel_658["font"] = ft
        GLabel_658["fg"] = "#1b1b1b"
        GLabel_658["justify"] = "center"
        GLabel_658["text"] = "BY MRCHOCOLAT3"
        GLabel_658.place(x=240, y=40, width=121, height=30)
        GLabel_658.config(background="white")

        self.heightEntry = tk.Entry(root)
        self.heightEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Blinker ', size=10)
        self.heightEntry["font"] = ft
        self.heightEntry["fg"] = "#1b1b1b"
        self.heightEntry["justify"] = "center"
        self.heightEntry["text"] = "Height"
        self.heightEntry.place(x=210, y=150, width=72, height=25)
        self.heightEntry.config(background='grey', borderwidth=1, border=0)

        self.widthEntry = tk.Entry(root)
        self.widthEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Blinker ', size=10)
        self.widthEntry["font"] = ft
        self.widthEntry["fg"] = "#1b1b1b"
        self.widthEntry["justify"] = "center"
        self.widthEntry["text"] = "Width"
        self.widthEntry.place(x=110, y=150, width=70, height=25)
        self.widthEntry.config(background='grey', borderwidth=1, border=0)

        GLabel_402 = tk.Label(root)
        ft = tkFont.Font(family='Blinker ', size=10)
        GLabel_402['highlightbackground'] = "white"
        GLabel_402["font"] = ft
        GLabel_402["fg"] = "#1b1b1b"
        GLabel_402["justify"] = "center"
        GLabel_402["text"] = "x"
        GLabel_402.place(x=180, y=148, width=30, height=30)
        GLabel_402.config(background="white")

        GLabel_930 = tk.Label(root)
        ft = tkFont.Font(family='Blinker ', size=10)
        GLabel_930['highlightbackground'] = "white"
        GLabel_930["font"] = ft
        GLabel_930["fg"] = "#1b1b1b"
        GLabel_930["justify"] = "left"
        GLabel_930["text"] = "Resolution :"
        GLabel_930.place(x=30, y=148, width=80, height=30)
        GLabel_930.config(background="white")

        GLabel_541 = tk.Label(root)
        ft = tkFont.Font(family='Blinker ', size=16)
        GLabel_541['highlightbackground'] = "white"
        GLabel_541["font"] = ft
        GLabel_541["fg"] = "#1b1b1b"
        GLabel_541["justify"] = "left"
        GLabel_541["text"] = "Set Custom Resolution  (Optional)"
        GLabel_541.place(x=25, y=110, width=282, height=30)
        GLabel_541.config(background="white")

        pngBtn = tk.Button(root)
        pngBtn["highlightbackground"] = "#5fb878"
        pngBtn["borderwidth"] = "0px"
        ft = tkFont.Font(family='Blinker ', size=13)
        pngBtn["font"] = ft
        pngBtn["fg"] = "#5fb878"
        pngBtn["justify"] = "center"
        pngBtn["text"] = "CONVERT TO PNG"
        pngBtn.place(x=390, y=170, width=180, height=45)
        pngBtn["command"] = self.pngBtn_command

        jpgBtn = tk.Button(root)
        jpgBtn["highlightbackground"] = "#c71585"
        jpgBtn["borderwidth"] = "0px"
        ft = tkFont.Font(family='Blinker ', size=13)
        jpgBtn["font"] = ft
        jpgBtn["fg"] = "#1b1b1b"
        jpgBtn["justify"] = "center"
        jpgBtn["text"] = "CONVERT TO JPEG"
        jpgBtn.place(x=390, y=220, width=180, height=45)
        jpgBtn["command"] = self.jpgBtn_command

        imgBtn = tk.Button(root)
        imgBtn["highlightbackground"] = "#01aaed"
        imgBtn["borderwidth"] = "0px"
        ft = tkFont.Font(family='Blinker ', size=13)
        imgBtn["font"] = ft
        imgBtn["fg"] = "#1b1b1b"
        imgBtn["justify"] = "center"
        imgBtn["text"] = "SELECT IMAGES"
        imgBtn.place(x=40, y=230, width=240, height=40)
        imgBtn["command"] = self.imgBtn_command

        GLabel_28 = tk.Label(root)
        ft = tkFont.Font(family='Blinker ', size=16)
        GLabel_28['highlightbackground'] = "white"
        GLabel_28["font"] = ft
        GLabel_28["fg"] = "#1b1b1b"
        GLabel_28["justify"] = "left"
        GLabel_28["text"] = "Browse Images to Convert"
        GLabel_28.place(x=40, y=190, width=194, height=34)
        GLabel_28.config(background="white")

        self.infoL = tk.Label(root)
        ft = tkFont.Font(family='monospace', size=16)
        self.infoL["font"] = ft
        self.infoL["fg"] = "#1e005f"
        self.infoL["justify"] = "left"
        self.infoL["text"] = ""
        self.infoL.place(x=40, y=80, width=530, height=30)
        self.infoL.config(background="white")

    def get_values(self):
        width = self.widthEntry.get()
        height = self.widthEntry.get()
        if width == "" or height == "":
            return None 
        else: return (int(width), int(height))

    def _clear_cache(self):
        imgPath = Path(self.images[0])
        exportPath = os.path.join(imgPath.parent, 'Converted Images')
        if os.path.exists(exportPath):
            shutil.rmtree(exportPath)
            os.mkdir(exportPath)
        else:
            os.mkdir(exportPath)

    def convert(
        self,
        ext: str,
        res: tuple = None
    ):
        # clear cache
        self._clear_cache()

        converted = 0
        for extns in self.extentions:
            for image in self.images:
                if extns in image:
                    img = Image.open(image).convert('RGB')
                    if res:
                        img.resize(res)
                    img.save(
                        image.replace(extns, ext), ext)
                    converted += 1

                    self.infoL['text'] = f"Converted {converted} / {len(self.images)} images"

    def webpBtn_command(self):
        self.infoL['text'] = "Converting to WEBP..."
        if len(self.images) > 0:
            try:
                self.convert('webp', self.get_values())
                self.infoL['text'] = "Converted!"
            except Exception as e:
                self.infoL['text'] = e

    def pngBtn_command(self):
        self.infoL['text'] = "Converting to PNG..."
        if len(self.images) > 0:
            try:
                self.convert('png', self.get_values())
                self.infoL['text'] = "Converted!"
            except Exception as e:
                self.infoL['text'] = e

    def jpgBtn_command(self):
        if len(self.images) > 0:
            self.infoL['text'] = "Converting to JPEG..."
            try:
                self.convert('jpeg', self.get_values())
                self.infoL['text'] = "Converted!"
            except Exception as e:
                self.infoL['text'] = e

    def imgBtn_command(self):
        self.images = fd.askopenfilenames(parent=root, title='Choose images to convert')
        self.infoL['text'] = f"Imported {len(self.images)} images"


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
