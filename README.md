
# Language Translator App

A simple and user-friendly desktop application for translating text between over 100 languages, developed during my internship at **CodeAlpha**.

## About the Project

This application allows users to input text, select a target language by its full name (e.g., *Arabic*, *French*), and instantly get a translation using the Google Translate API. It features a clean graphical interface built with **Tkinter** and is packaged as a standalone `.exe` for Windows using **PyInstaller**.

## Features

- Translate text between 100+ languages
- Full language names (no confusing language codes)
- Modern, minimal desktop interface
- Built with Python and Tkinter
- Distributed as a standalone Windows executable

## Tech Stack

- Python 3.x
- Tkinter (GUI)
- `googletrans` (Google Translate API wrapper)
- PyInstaller (for `.exe` generation)


## How to Run

### Option 1: Use the Pre-built Executable

You can run the application directly using the `.exe` file included in the repository:

```
dist/language-translator-app.exe
```

No installation required — just double-click to launch.

### Option 2: Run from Source

#### 1. Clone the Repository

```bash
git clone https://github.com/MhamedHalloub/Translater-App.git
cd Translator-app
```

#### 2. Install Dependencies

```bash
pip install googletrans==4.0.0-rc1
```

#### 3. Run the App

```bash
python translator_gui.py
```


## Credits

Developed as part of my **internship at CodeAlpha**.

## License

This project is licensed under the [MIT License](LICENSE).
