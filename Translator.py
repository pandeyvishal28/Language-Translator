import tkinter as tk
import ttkbootstrap as ttk
import googletrans as gt
from tkinter import messagebox
import textblob as tb


# function to translate the text


def translate():
    try:
        translator = gt.Translator()
        # global src_lang_code
        # global dest_lang_code

        for key, value in languages.items():
            if value.capitalize() == src_lang.get():
                src_lang_code = key

            if value.capitalize() == dest_lang.get():
                dest_lang_code = key
        words = tb.TextBlob(input_text.get(1.0, tk.END))

        words = words.translate(from_lang=src_lang_code, to=dest_lang_code)

        output_entry.delete(1.0, tk.END)
        output_entry.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("Error", e)


try:

    # window
    window = ttk.Window(themename="darkly")
    window.title("Translator")
    window.geometry("1020x450")

    image = tk.PhotoImage(file="icon.png")
    window.iconphoto(False, image)

    languages = gt.LANGUAGES

    # title
    title_label = ttk.Label(window, text="Translator", font=("calibri", 24))
    title_label.grid(row=0, column=1, padx=10, pady=1)

    # input_text

    input_text = tk.Text(window, width=30, height=10, font=("calibri 14"))
    input_text.grid(row=1, column=0, pady=10, padx=10, ipadx=10, ipady=10)

    # Translate button
    button = ttk.Button(window, text="Translate", command=translate)
    button.grid(row=1, column=1, padx=10, pady=10)

    # src_label

    src_lang = ttk.Combobox(window, text="from")
    src_lang['values'] = list(map(str.capitalize, languages.values()))
    src_lang_code = ''
    src_lang.grid(row=2, column=0, padx=10, pady=10)
    src_lang.current(21)

    # dest_label

    dest_lang = ttk.Combobox(window, text="to")
    dest_lang['values'] = list(map(str.capitalize, languages.values()))
    dest_lang.grid(row=2, column=2, padx=10, pady=10)
    dest_lang.current(23)

    # output_text

    output_entry = ttk.Text(window, width=30, height=10, font=("calibri 14"))
    output_entry.grid(row=1, column=2, pady=10, padx=10, ipadx=10, ipady=15)

    window.mainloop()
except Exception as ex:
    messagebox.showerror("Error", ex)
