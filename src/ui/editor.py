import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
from tkinter import messagebox


class SVGEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SVG Editor")
        self.root.resizable(False, False)

        window_width = 700
        window_height = 500

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.ui_screen()

    def ui_screen(self):
        # Ana Frame'i oluştur ve tüm pencereyi kaplasın
        self.main_frame = tk.Frame(self.root, padx=10, pady=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Sol taraftaki Frame
        self.left_frame = tk.Frame(self.main_frame, borderwidth=2,
                                   relief="groove", padx=10, pady=10)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Label(self.left_frame, text="İşlemler", bg="white", padx=8, pady=8).pack()

        self.buton1 = tk.Button(
            self.left_frame, text="Yükle", command=self.upload_file)
        self.buton2 = tk.Button(self.left_frame, text="Temizle", command=self.clear_content)
        self.buton3 = tk.Button(self.left_frame, text="İndir", command=self.dowload_svg)

        self.buton1.pack(pady=10, fill=tk.X)
        self.buton2.pack(pady=10, fill=tk.X)
        self.buton3.pack(pady=10, fill=tk.X)

        # Sağ taraftaki Frame
        self.right_frame = tk.Frame(self.main_frame, borderwidth=2,
                                    relief="groove", padx=10, pady=10)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        tk.Label(self.right_frame, text="Düzenlenmiş SVG", anchor="w",
                 bg="white", padx=8, pady=8).pack(padx=10, fill=tk.X)

        self.text_input = tk.Text(self.right_frame, bd=2, relief="groove", padx=10, pady=10)
        self.text_input.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

    def upload_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("SVG Files", "*.svg")])

        if file_path:
            with open(file_path, "r") as f:
                content = f.read()

            content = self.format_svg(content)

            self.text_input.delete("1.0", tk.END)
            self.text_input.insert(tk.END, content)

    def format_svg(self, svg_text):
        try:
            root = ET.fromstring(svg_text)

            for elem in root.iter():
                if "}" in elem.tag:
                    elem.tag = elem.tag.split("}")[1]
                    elem.tag = elem.tag.capitalize()

            formatted_svg = ET.tostring(root, encoding="unicode")
            return formatted_svg

        except ET.ParseError:
            messagebox.showerror("Hata", "SVG dosyası geçersiz!")
            return "SVG dosyası geçersiz!"

    def dowload_svg(self):
        svg_content = self.text_input.get("1.0", tk.END)

        if svg_content.strip():
            file_path = filedialog.asksaveasfilename(defaultextension=".svg", filetypes=[("SVG Files", "*.svg")])
            if file_path:
                with open(file_path, "w") as f:
                    f.write(svg_content)
                
                messagebox.showinfo("İndirme Başarılı", "İndirme işlemi başarıyla gerçekleştirildi.")
        else:
            messagebox.showwarning("Uyarı", "SVG içeriği boş, indirme işlemi gerçekleştirilemedi.")
            print("SVG içeriği boş, indirme işlemi gerçekleştirilemedi.")

    def clear_content(self):
        self.text_input.delete("1.0", tk.END)
