from tkinter import Tk, Label, Text, Button, filedialog, ttk, Frame, messagebox
import subprocess
import threading
from os import path, listdir

def processControl(option, path):
    if(option == 'create'):
        subprocess.Popen('extract-xiso.exe -c "%s"' % path)
    elif(option == 'extract'):
        subprocess.Popen('extract-xiso.exe -x "%s"' % path)

def threadedProcess():
        threading.Thread(target=processControl).start()

def getPath(recursive=False):
    file_path = filedialog.askdirectory()
    if(path.isfile(file_path)):
        # attempt to extract file
        try:
            filename, extension = str(file_path).split('.')
            if(extension == 'iso'):
                # need to extract
                return 'extract'
            else:
                # error, file not supported
                messagebox.showerror('File type is not supported.\nMust be iso filetype.')
        except:
            # error, file has no extension
            messagebox.showerror('File object has no extension')
    elif(path.isdir(file_path)):
        if(not recursive):
            # compress directory
            file_objects = listdir()
            found = False
            for file in file_objects:
                if('.xbe' in file):
                    found = True
                    break
            
            if(found):
                return 'create'
            else:
                messagebox.showerror('Directory is not an xbe directory')
        else:
            # create from all viable sub directories
            pass
    else:
        # error, wth file object is this?
        messagebox.showerror('Completely unknown filetype.')

def createWindow():
    window = Tk()
    window.title("pyXISO")

    # Frames
    topframe = Frame(window)
    bottomframe = Frame(window)
    topframe.grid(column=0, row=0)
    bottomframe.grid(column=0, row=1)

    # File/Directory name
    text_width = 100
    file_Label = Label(topframe, text="File Selected: None")
    file_Label.grid(column=0, row=0, padx=20)

    path_btn = Button(topframe, text="Select the file or directory", command=getPath)
    path_btn.grid(column=1, row=0, padx=20)

    start_btn = Button(topframe, text="Start", command=threadedProcess)
    start_btn.grid(column=2, row=0, padx=20)

    # Progress bar
    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background='black')
    bar = ttk.Progressbar(bottomframe, length=text_width*6,
                        style='black.Horizontal.TProgressbar')
    bar.grid(column=0, row=1, padx=4, pady=4)

    # def update():
    #     bar['value'] = progress_value
    #     if(progress_value >= 100):
    #         selected_class = var.get()
    #         global media_label
    #         res = 'Finished! %s Download, %s' % (
    #             selected_class, media_label)
    #         URL_Label.configure(text=res)
    #     elif(progress_value > 0):
    #         global playlist_checked
    #         if(playlist_checked):
    #             global playlist_index
    #             global playlist_count
    #             playlist_label.configure(
    #                 text="%s/%s" % (str(playlist_index + 1), str(playlist_count)))
    #         selected_class = var.get()
    #         URL_Label.configure(
    #             text=str("Downloading...  %s %s" % (selected_class, media_label)))
    #     window.after(100, update)

    # Execute GUI
    #threading.Thread(target=update).start()
    window.mainloop()
    
createWindow()