import os
import shutil
from collections import Counter
import tkinter as tk
from tkinter import filedialog, messagebox


# ---------------------------------------------------------
# Developed by: [M.Sh]
# Project: Smart File Organizer (Pro Version) # Tkinter GUI
# ---------------------------------------------------------

class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart File Organizer - Version 2.04")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        # دیکشنری دسته‌بندی‌ها
        self.categories = {
            "Images": (".png", ".jpg", ".jpeg", ".avif", ".gif", ".svg"),
            "Web_Docs": (".html", ".css", ".js"),
            "Programming": (".py", ".c", ".cpp", ".java", ".go"),
            "Documents": (".txt", ".pdf", ".docx", ".xlsx"),
            "Music": (".mp3", ".wav", ".flac"),
            "Videos": (".mp4", ".avi", ".mkv", ".mov"),
        }

        self.setup_ui()

    def setup_ui(self):
        """ساختار ظاهری برنامه"""
        tk.Label(self.root, text="Smart File Organizer", font=("Arial", 18, "bold")).pack(pady=10)
        tk.Label(self.root, text="Select a folder to organize your files automatically", wraplength=300).pack(pady=5)

        self.select_btn = tk.Button(self.root, text="Select Folder & Start",
                                    command=self.start_organizing,
                                    bg="#2ecc71", fg="white", font=("Arial", 10, "bold"), padx=20, pady=10)
        self.select_btn.pack(pady=20)

        tk.Label(self.root, text="© 2025 | Powered by [M.Sh]", fg="gray").pack(side="bottom", pady=5)

    def start_organizing(self):
        # انتخاب پوشه توسط کاربر
        target_dir = filedialog.askdirectory()

        if not target_dir:
            return

        moved_counts = []
        original_address = os.getcwd()

        try:
            os.chdir(target_dir)
            files = [f for f in os.listdir(target_dir) if os.path.isfile(f)]

            for file in files:
                found_category = False
                file_ext = os.path.splitext(file)[1].lower()  # گرفتن پسوند و تبدیل به حروف کوچک

                for category, extensions in self.categories.items():
                    if file_ext in extensions:
                        self.move_file(file, category)
                        moved_counts.append(category)
                        found_category = True
                        break

                # اگر در دسته‌بندی‌ها نبود
                if not found_category:
                    self.move_file(file, "Other_Files")
                    moved_counts.append("Other_Files")

            # نمایش گزارش نهایی
            report = Counter(moved_counts)
            result_msg = "Organization Complete!\n\n"
            for cat, count in report.items():
                result_msg += f"• {cat}: {count} files\n"

            messagebox.showinfo("Success", result_msg if moved_counts else "No files found to organize!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            os.chdir(original_address)

    def move_file(self, file, folder_name):
        """ساخت پوشه و انتقال فایل"""
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        try:
            shutil.move(file, folder_name)
        except:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()
