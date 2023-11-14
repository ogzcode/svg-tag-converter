import tkinter as tk

from src.ui.editor import SVGEditorApp


if __name__ == "__main__":
    root = tk.Tk()
    app = SVGEditorApp(root)
    root.mainloop()
