from tkinter import *
import os
import shutil


# All the extensions that are allowed.
pic = [".jpeg", ".jpg", ".png", ".gif", ".tiff", ".raw"]
pytho = [".ipynb", ".java", ".cs", ".js"]
txt = [".txt", ".pdf", ".doc", ".pdf", ".ppt", ".pps", ".docx", ".pptx"]
music = [".mp3", ".wav", ".wma", ".mpa", ".ram", ".ra", ".aac", ".aif", ".m4a", ".tsa"]
zip = [".zip", ".rar", ".arj", ".gz", ".sit", ".sitx", ".sea", ".ace", ".bz2", ".7z"]
app = [".exe", ".msi"]
vid = [".mp4", ".webm", ".mkv", ".MPG", ".MP2", ".MPEG", ".MPE", ".MPV", ".OGG", ".M4P", ".M4V", ".WMV", ".MOV", ".QT", ".FLV", ".SWF", ".AVCHD", ".avi", ".mpg", ".mpe", ".mpeg", ".asf", ".wmv", ".mov", ".qt", ".rm"]


def run():
    root = Tk()
    root.title("File Handler")
    lable_1 = Label(root, text = "Enter address of file containing folder")
    lable_2 = Label(root, text="Enter address of destination folder")

    # These are the entry points through which paths of the files are entered.
    sorce_folder = Entry(root, width=50, borderwidth=5)
    destination_folder = Entry(root, width=50, borderwidth =5)

    # The buttton which does all the operation
    button_1 = Button(root, text="Start", padx=40, pady=10, command=lambda: runmain(sorce_folder, destination_folder))

    # These are the cordinates on which everything is placed.
    lable_1.grid(row=0, column=0)
    lable_2.grid(row=2, column=0)
    sorce_folder.grid(row=1, column=0, columnspan=3, padx=20, pady=20)
    destination_folder.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
    button_1.grid(row=4, column=0)

    root.mainloop()

def runmain(sorce_folder, destination_folder):
    start_folder = sorce_folder.get()
    sorce_folder.delete(0, END)
    end_folder = destination_folder.get()
    destination_folder.delete(0, END)
    # List of folders in which files are to be arranged.
    file_name_list = ["Pictures", "Music", "Videos", "Documents", "Compressed", "applications", "Programming"]

    # The file_cont_folder1 contains list of all the directories of end folder.
    destination_list = ["Pictures", "Music", "Videos", "Documents", "Compressed", "applications", "Programming"]

    # This loop checks if there already a required folder in the end folder and makes if not present
    for i in file_name_list:
        try:
            b = os.path.join(end_folder, i)
            os.makedirs(b)
        except OSError as error:
            continue

    # This loop will check how many files to be moved and move them.
    for filename in os.listdir(start_folder):
        for i in txt:
            if filename.endswith(i):
                ef = os.path.join(end_folder, destination_list[3])
                sf = os.path.join(start_folder,filename)
                shutil.move(sf, ef)
                break
        for i in pic:
            if filename.endswith(i):
                ef = os.path.join(end_folder, destination_list[0])
                sf = os.path.join(start_folder, filename)
                shutil.move(sf, ef)
                break
        for i in pytho:
            if filename.endswith(i):
                ef = os.path.join(end_folder, destination_list[6])
                sf = os.path.join(start_folder, filename)
                shutil.move(sf, ef)
                break
        for i in music:
            if filename.endswith(i):
                ef = os.path.join(end_folder, destination_list[1])
                sf = os.path.join(start_folder, filename)
                shutil.move(sf, ef)
                break
        for i in zip:
            if filename.endswith(i):
                ef = os.path.join(end_folder, destination_list[4])
                sf = os.path.join(start_folder, filename)
                shutil.move(sf, ef)
                break
        for i in app:
            if filename.endswith(i):
                ef = os.path.join(end_folder, destination_list[5])
                sf = os.path.join(start_folder, filename)
                shutil.move(sf, ef)
                break
        for i in vid:
            if filename.endswith(i):
                ef = os.path.join(end_folder, destination_list[2])
                sf = os.path.join(start_folder, filename)
                shutil.move(sf, ef)
                break


if __name__ == "__main__":
    run()
