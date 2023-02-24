from Maze import *
import tkinter, os

def main():
    # Making Root
    root = tkinter.Tk()
    root.geometry("400x400")
    root.minsize(400, 400)
    root.maxsize(400, 400)
    root.title("Maze Generator by 321nomyzS")

    # Making icon
    icon = tkinter.PhotoImage(file=r"structures\icon.png")
    root.iconphoto(False, icon)

    # Title
    title_img = tkinter.PhotoImage(file=r"structures\title.png")
    tkinter.Label(root, image=title_img).place(x=32,y=0)

    # Size of maze
    tkinter.Label(root, text='Size of maze:', font=('Cambria', 18)).place(x=20,y=170)
    maze_size = tkinter.Entry(root, font=('default', 18), width=12)
    maze_size.place(x=180,y=175)

    # File extension
    tkinter.Label(root, text='File extension:', font=('Cambria', 18)).place(x=20,y=210)
    png_file = tkinter.IntVar()
    gif_file = tkinter.IntVar()

    chkbutton1 = tkinter.Checkbutton(root, text = '.png', variable = png_file, onvalue=True, offvalue=False, font=('Cambria', 18))
    chkbutton1.place(x=180,y=210)

    chkbutton2 = tkinter.Checkbutton(root, text = '.gif', variable = gif_file, onvalue=True, offvalue=False, font=('Cambria', 18))
    chkbutton2.place(x=280,y=210)


    # Button
    def maze_generator():
        size = maze_size.get()
        png = png_file.get()
        gif = gif_file.get()

        lab = Maze(int(size))
        if png and gif:
            lab.generating_gif_and_file()
            tkinter.Label(root, text='The .gif and .png files have just been generated!').place(x=10, y=320)
            os.system("start maze.png")
            os.system("start maze.gif")
        elif png:
            lab.generating_file()
            tkinter.Label(root, text='The .png file has just been generated!').place(y=320, x=10)
            os.system("start maze.png")
        elif gif:
            lab.generating_gif()
            tkinter.Label(root, text='The .gif file has just been generated!').place(x=10, y=320)
            os.system("start maze.gif")


    virtual_pixel = tkinter.PhotoImage(r"structures\pixel.png")
    tkinter.Button(root, text='Generate maze!', image=virtual_pixel, command=maze_generator, font=('Cambria', 14), width=150, compound="c").place(x=125, y=260)
    root.mainloop()


if __name__ == "__main__":
    main()
