from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()

root.title("TarNote 0.0.1")

root.geometry('500x600+465+135')


main_menu = Menu(root)
root.config(menu=main_menu)


def about_program():
    messagebox.showerror(title='About TarNote',
                         message='Program TarNote version 0.0.1\nDesignet by tarp20')


def change_theme(theme):
    t['bg'] = theme_colors[theme]['text_bg']
    t['fg'] = theme_colors[theme]['text_fg']
    t['insertbackground'] = theme_colors[theme]['cursor']
    t['selectbackground'] = theme_colors[theme]['select_bg']


def quit_program():
    answer = messagebox.askokcancel(title="Quit", message="Quit TarNote?")
    if answer:
        root.destroy()


def open_file():
    file_path = filedialog.askopenfilename(title="choose a file", filetypes=(
        ("text documents (*.txt)", "*.txt"), ("allfiles", "*.*")))
    if file_path:
        t.delete('1.0', END)
        t.insert('1.0', open(file_path, encoding='utf-8').read())


def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(("text documents (*.txt)", "*.txt"), ("all files", "*.*")))
    f = open(file_path, 'w', encoding='utf-8')
    text = t.get('1.0', END)
    f.write(text)
    f.close()


file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit_program)
main_menu.add_cascade(label="File", menu=file_menu)

# Theme menu
theme_menu = Menu(main_menu, tearoff=0)
theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(label="Light", command=lambda: change_theme('light'))
theme_menu_sub.add_command(label="Dark", command=lambda: change_theme('dark'))
theme_menu.add_cascade(label="Desigh", menu=theme_menu_sub)
theme_menu.add_command(label="About", command=about_program)
main_menu.add_cascade(label="Extra", menu=theme_menu)


f_text = Frame(root, bg="#343D46")
f_text.pack(fill=BOTH, expand=1)

theme_colors = {
    "light": {
        "text_bg": "#fff",
        "text_fg": "#000",
        "cursor": "#8000FF",
        "select_bg": "#777"

    },
    "dark": {
        "text_bg": "#343D46",
        "text_fg": "#C6DEC1",
        "cursor": "#EDA756",
        "select_bg": "#4E5A65"

    }
}


t = Text(f_text, bg=theme_colors['dark']['text_bg'],
         fg=theme_colors['dark']['text_fg'], padx=10,
         pady=10, wrap=WORD, insertbackground=theme_colors['dark']['cursor'],
         selectbackground=theme_colors['dark']['select_bg'],
         width=30, spacing3=10, font=("Courier New", 15))
t.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)

t.config(yscrollcommand=scroll.set)


root.mainloop()
