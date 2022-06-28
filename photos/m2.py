#підключаєм необхідні бібліотеки
import os
#os.chdir("D:\DEL")

import tkinter as tk
from tkinter import Canvas, filedialog as fd

from PIL import Image, ImageTk
from PIL.ImageFilter import CONTOUR, EDGE_ENHANCE, DETAIL
import m1

#Створюємо функцію для зміни зображення
def change_img(new_image):
    
    global img_label

    print('change_img ', new_image)

    img = Image.open(new_image)
    img = img.convert('RGB')
    img.thumbnail([512, 256])
    img2 = ImageTk.PhotoImage(image=img)
    img_label.configure(image = img2)
    img_label.image = img2

#Створюємо функцію для збереження зображення з новим типом
def save_image_with_another_extension(image_name: str, new_extension: str) -> str:

    im = Image.open(image_name)
    image_name_without_extension = ''.join(''.join(image_name.split('.')[:-1]).split('/')[-1])
    im.save(f'{image_name_without_extension}.{new_extension}')

    global current_file, img_name
    current_file = f'{image_name_without_extension}.{new_extension}'
    img_name.config(text = f'Opened file: {current_file}')
    change_img(current_file)
    print(current_file)

    return f'{image_name_without_extension}.{new_extension}'

#Створюємо функцію для зміни розмірів зображення
def change_resolution(x: int, y: int, current_file) -> Image:

    image = Image.open(current_file)
    image = image.resize((x, y), Image.ANTIALIAS)
    image.save(current_file, optimize = True, quality = 95)
    change_img(current_file)
    return image

#Створюємо функцію для застосування фільтру
def apply_contour_filter(image_name: str) -> None:

    image = Image.open(image_name)
    image = image.convert('RGB')
    image = image.filter(DETAIL)
    image.save(image_name)
    change_img(current_file)

    return image

#Створюємо функцію для вибору файла
def choose_file():

    global current_file

    current_file = "photo.jpeg"

    change_img(current_file)

    return current_file

#Створюємо юай, де розміщуєм текстові поля, кнопки і тд
if __name__ == "__main__":

    app = tk.Tk()
    app.config(bg = 'gray80')
    new_file_extension = tk.StringVar()
    current_file = tk.StringVar()
    x = tk.StringVar()
    y = tk.StringVar()

    button = tk.Button(app, command = lambda: choose_file(),
                       text = 'CHOOSE FILE', width = 16,
                       height = 3,
                       bg = "MediumOrchid1",
                       fg = "white", font = ('Arial', 15 ), relief = "flat")
    button.grid(row = 6, column = 7, sticky = 'ew', padx = 5, pady = 10)

    img_name = tk.Label(app,bg = "gray70", fg = "white", font = ('Arial', 12 ), text = 'Opened file: None')
    img_name.grid(row = 9, column = 7, sticky = 'ew', pady = 8)

    extension_entry = tk.Entry(textvariable=new_file_extension)
    extension_entry.grid(row = 12, column = 4, sticky = 'e', pady = 10)

    img_ext = tk.Label(app, bg = "gray70", fg = "white", font = ('Arial', 12 ), text = 'New type')
    img_ext.grid(row = 12, column = 3,  sticky = 'e', padx = 3, pady = 4)

    button_ext = tk.Button(app, command = lambda:
    save_image_with_another_extension(current_file,
    new_file_extension.get()),
    text = 'CHANGE FILE TYPE', bg = "MediumOrchid1", fg = "white", font = ('Arial', 13 ), relief = "flat")
    button_ext.grid(row = 15, column = 4, sticky = 'e', pady = 6)

    img_x = tk.Label(app, bg = "gray70", fg = "white", font = ('Arial', 12 ), text = 'Width')
    img_x.grid(row = 20, column = 3, sticky = 'e', padx = 6, pady = 6)
    extension_entry = tk.Entry(textvariable = x)
    extension_entry.grid(row = 20, column = 4, sticky = 'e', padx = 5, pady = 6)

    img_y = tk.Label(app, bg = "gray70", fg = "white", font = ('Arial', 12 ), text = 'Height')
    img_y.grid(row = 25, column = 3, sticky = 'e', padx = 6, pady = 6)
    extension_entry = tk.Entry(textvariable = y)
    extension_entry.grid(row = 25, column = 4, sticky = 'e', padx = 6, pady = 6)
    button_res = tk.Button(app, command = lambda:
                           change_resolution(int(x.get()), int(y.get()), current_file),
                           text = 'CHANGE SIZE', bg = "MediumOrchid1",
                           fg = "white", font = ('Arial', 13 ), relief = "flat")
    button_res.grid(row = 28, column = 4, sticky = 'e', pady = 6)

    button_filter = tk.Button(app, command = lambda:
                              apply_contour_filter(current_file),
                              text = 'ON FILTER', bg = "MediumOrchid1",
                              fg = "white", font = ('Arial', 13 ), relief = "flat")
    button_filter.grid(row = 34, column = 4, sticky = 'e', pady = 6)

    button_filter = tk.Button(app, command=lambda:
                              m1.main("photo.jpeg"),
                              text='СUT', bg="MediumOrchid1",
                              fg="white", font=('Arial', 13), relief="flat")
    button_filter.grid(row=38, column=4, sticky='e', pady=6)

    img_label = tk.Label(app)
    img_label.grid(row = 42, column = 4, columnspan = 4, sticky = 'e')

    app.bind("<Return>", change_img)
    app.title("Image")
    app.geometry("800x800")
    app.mainloop()

    app.mainloop()

