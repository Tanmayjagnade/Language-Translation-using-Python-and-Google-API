from tkinter import *
from googletrans import Translator

root = Tk()
root.title("Language Translator")
root.geometry("700x500")


# Customize colors
label_color = "#fff"
button_color = "#ccc"
textbox_color = "#f1f1f1"

# Function to translate the text
def translate_text():
    translator = Translator()
    source_lang = source_language.get()
    dest_lang = destination_language.get()
    source_text = source_text_box.get(1.0, END)
    translated_text = translator.translate(source_text, src=source_lang, dest=dest_lang)
    destination_text_box.delete(1.0, END)
    destination_text_box.insert(END, translated_text.text)

# Source Language Label
source_language_label = Label(root, text="Source Language", bg=label_color)
source_language_label.grid(row=0, column=0, padx=10, pady=10)

# Source Language Dropdown
source_language = StringVar(root)
source_language.set("en") # default value
source_language_dropdown = OptionMenu(root, source_language, "en", "es", "fr", "de", "ru")
source_language_dropdown.config(bg=button_color)
source_language_dropdown.grid(row=0, column=1, padx=10, pady=10)

# Destination Language Label
destination_language_label = Label(root, text="Destination Language", bg=label_color)
destination_language_label.grid(row=1, column=0, padx=10, pady=10)

# Destination Language Dropdown
destination_language = StringVar(root)
destination_language.set("es") # default value
destination_language_dropdown = OptionMenu(root, destination_language, "en", "es", "fr", "de", "ru")
destination_language_dropdown.config(bg=button_color)
destination_language_dropdown.grid(row=1, column=1, padx=10, pady=10)

# Source Text Label
source_text_label = Label(root, text="Enter Text to Translate", bg=label_color)
source_text_label.grid(row=2, column=0, padx=10, pady=10)

# Source Text Box
source_text_box = Text(root, height=10, width=40, bg=textbox_color)
source_text_box.grid(row=3, column=0, padx=10, pady=10)

# Destination Text Label
destination_text_label = Label(root, text="Translated Text", bg=label_color)
destination_text_label.grid(row=2, column=1, padx=10, pady=10)

# Destination Text Box
destination_text_box = Text(root, height=10, width=40, bg=textbox_color)
destination_text_box.grid(row=3, column=1, padx=10, pady=10)

# Translate Button
translate_button = Button(root, text="Translate", command=translate_text, bg=button_color)
translate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
