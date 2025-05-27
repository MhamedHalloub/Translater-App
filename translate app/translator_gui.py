import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Reverse LANGUAGES dict to get full name to short code mapping
LANGUAGE_NAMES = {name.capitalize(): code for code, name in LANGUAGES.items()}
LANGUAGE_LIST = sorted(LANGUAGE_NAMES.keys())

# Initialize the translator
translator = Translator()

# Translation function
def translate():
    text = input_text.get("1.0", tk.END).strip()
    selected_lang_name = target_lang_var.get()

    if not text:
        messagebox.showwarning("Warning", "Please enter text to translate.")
        return

    if selected_lang_name not in LANGUAGE_NAMES:
        messagebox.showerror("Error", "Please select a valid language.")
        return

    target_code = LANGUAGE_NAMES[selected_lang_name]

    try:
        translation = translator.translate(text, dest=target_code)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translation.text)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed:\n{e}")

# --- GUI Setup ---

# Main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("600x500")
root.configure(bg="#f7f9fb")
root.resizable(False, False)

# Title
tk.Label(root, text="Language Translator", font=("Segoe UI", 18, "bold"), bg="#f7f9fb").pack(pady=10)

# Input text
tk.Label(root, text="Enter text:", font=("Segoe UI", 12), bg="#f7f9fb").pack(anchor="w", padx=20)
input_text = tk.Text(root, height=6, font=("Segoe UI", 11))
input_text.pack(padx=20, fill="x")

# Language selection
tk.Label(root, text="Translate to:", font=("Segoe UI", 12), bg="#f7f9fb").pack(anchor="w", padx=20, pady=(10, 0))
target_lang_var = tk.StringVar()
lang_combobox = ttk.Combobox(root, textvariable=target_lang_var, values=LANGUAGE_LIST, state="readonly", font=("Segoe UI", 11))
lang_combobox.set("French")  # default selection
lang_combobox.pack(padx=20, pady=5, fill="x")

# Translate button
translate_btn = ttk.Button(root, text="Translate", command=translate)
translate_btn.pack(pady=10)

# Output text
tk.Label(root, text="Translated text:", font=("Segoe UI", 12), bg="#f7f9fb").pack(anchor="w", padx=20)
output_text = tk.Text(root, height=6, font=("Segoe UI", 11), bg="#e8f0fe")
output_text.pack(padx=20, fill="x", pady=(0, 20))

# Run app
root.mainloop()
