# Smart Auto File Organizer

A simple and intelligent desktop tool that automatically organizes files inside a folder based on their file type.  
This project is built with **Python** and **Tkinter**, providing a clean graphical interface that allows users to organize messy folders with a single click.

---

## Overview

Folders like **Downloads**, **Desktop**, or project directories often become cluttered with many different types of files.  
The **Smart File Organizer** solves this problem by automatically detecting file types and moving them into categorized folders.

For example, if a folder contains images, documents, music, videos, and programming files, the program will automatically create separate folders and move each file into its appropriate category.

This helps keep directories clean, structured, and easier to navigate.

---

## Features

• Simple graphical user interface (GUI)  
• Automatic file type detection  
• Smart folder creation  
• Organized report after completion  
• Supports multiple file categories  
• Lightweight and fast  

---

## Supported File Categories

The program currently organizes files into the following categories:

- **Images** → `.png`, `.jpg`, `.jpeg`, `.avif`, `.gif`, `.svg`  
- **Web Documents** → `.html`, `.css`, `.js`  
- **Programming Files** → `.py`, `.c`, `.cpp`, `.java`, `.go`  
- **Documents** → `.txt`, `.pdf`, `.docx`, `.xlsx`  
- **Music** → `.mp3`, `.wav`, `.flac`  
- **Videos** → `.mp4`, `.avi`, `.mkv`, `.mov`  
- **Other Files** → Any file type not listed above

---

## How the Code Works

The project is written using **Python's object‑oriented programming structure** and the **Tkinter library** for building the graphical interface.

The main logic of the program works in several steps:

### 1. User selects a folder
When the program starts, the interface displays a button called **"Select Folder & Start"**.  
When clicked, a file dialog appears allowing the user to choose a directory.


filedialog.askdirectory()


This returns the path of the selected folder which becomes the target directory for organization.

---

### 2. The program scans the folder

After selecting a folder, the program reads all files inside the directory using:


os.listdir()


It filters only actual files using:


os.path.isfile()


This ensures folders are ignored and only files are processed.

---

### 3. Detecting the file type

For every file found in the directory, the program extracts the file extension using:


os.path.splitext(file)[1].lower()


Example:


photo.jpg  -> .jpg
music.mp3  -> .mp3
code.py    -> .py


The extension is converted to lowercase to ensure consistent matching.

---

### 4. Categorizing files

The program uses a **dictionary of categories** where each category contains a tuple of supported extensions.

Example:


self.categories = {
    "Images": (".png", ".jpg", ".jpeg"),
    "Music": (".mp3", ".wav"),
    "Documents": (".pdf", ".txt")
}


For each file, the program checks whether its extension belongs to one of these categories.

If a match is found, the file is assigned to that category.

If no match exists, the file is placed into an **"Other_Files"** folder.

---

### 5. Moving files into folders

If the destination folder does not exist, the program automatically creates it:


os.mkdir(folder_name)

Then the file is moved using:

shutil.move(file, folder_name)


Example result:

Before organizing:


Downloads/
    photo.jpg
    song.mp3
    report.pdf


After organizing:

Downloads/
    Images/
        photo.jpg

    Music/
        song.mp3

    Documents/
        report.pdf

---

### 6. Generating a final report

After organizing all files, the program generates a summary using Python's **Counter** from the `collections` module.

Example output:


Organization Complete!

Images: 5 files
Music: 3 files
Documents: 2 files


This message is displayed using a Tkinter message box.

---

## Technologies Used

- **Python**
- **Tkinter** (GUI)
- **OS module** (file system interaction)
- **Shutil** (file moving operations)
- **Collections.Counter** (report generation)

---

## Installation

Clone the repository:

git clone https://github.com/yourusername/smart-file-organizer.git

Navigate to the project folder:

cd smart-file-organizer


Run the program:

python organizer.py


---

## Future Improvements

Possible future enhancements for the project:

- Drag & drop folder selection
- Dark mode interface
- Progress bar for large folders
- Automatic monitoring of folders
- Duplicate file detection
- AI-based file classification

---

## License.With My Name And Github


## Author

Developed by **[M.Sh]

که پروژه‌ات خیلی حرفه‌ای‌تر دیده شود.
