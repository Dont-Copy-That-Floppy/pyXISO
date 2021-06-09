from tkinter import Tk, Label, Button, filedialog, ttk, Frame, messagebox
import subprocess
import threading
import sys
import os

# TO-DO
# output directory same or different
# Progress bar
# Display filename of selected file object


class GUI:
    option = ''
    file_path = ''
    filename_label = None
    process_label = None
    filename_text = 'File Selected: '
    process_text = 'Process: '
    output_directory = './'

    def __init__(self):
        self.exe_directory = os.path.join("%s/exe/" % os.getcwd())
        self.createWindow()

    def processControl(self):
        if(self.option == 'create'):
            subprocess.Popen('%s/extract-xiso.exe -c "%s" "%s.iso"' % (self.exe_directory, os.path.join(
                os.path.dirname(self.file_path)), os.path.join(self.output_directory, self.file_object_name)))
        elif(self.option == 'extract'):
            subprocess.Popen('%s/extract-xiso.exe -x "%s"' %
                             (self.exe_directory, os.path.join(self.file_path)))
        else:
            messagebox.showerror('No File selected')

    def threadedProcess(self):
        threading.Thread(target=self.processControl).start()

    def getPath(self, recursive=False):
        # get selection from user
        self.file_path = filedialog.askopenfilename()
        try:
            temp, extension = str(self.file_path).split('.')
        except:
            messagebox.showerror('Error', 'File has no extension')

        if(extension == 'xbe'):
            self.option = 'create'
            self.file_object_name = str(
                os.path.dirname(self.file_path)).split('/')[-1]
            print(self.file_object_name)
        elif(extension == 'iso'):
            self.option = 'extract'
            self.file_object_name = str(self.file_path).split('/')[-1]
        else:
            messagebox.showerror('Error', 'Incomaptible file type')

        try:
            self.filename_label.configure(text="%s%s" % (
                self.filename_text, self.file_object_name))
            self.process_label.configure(text="%s%s" % (
                self.process_text, str(self.option).upper()))
        except:
            messagebox.showerror("Error", "Don't do that...")

    def setOutputDirectory(self):
        self.output_directory = filedialog.askdirectory()

    def createWindow(self):
        window = Tk()
        window.title("pyXISO")

        # Frames
        topframe = Frame(window)
        middleframe = Frame(window)
        bottomframe = Frame(window)
        topframe.grid(column=0, row=0)
        middleframe.grid(column=0, row=1)
        bottomframe.grid(column=0, row=2)

        # File/Directory name
        text_width = 100
        self.filename_label = Label(
            topframe, text="%sNone" % self.filename_text)
        self.filename_label.grid(column=0, row=0, padx=20)

        # Process detected
        text_width = 100
        self.process_label = Label(topframe, text="%sNone" % self.process_text)
        self.process_label.grid(column=2, row=0, padx=6)

        # Begin selected process
        start_btn = Button(topframe, text="Start",
                           command=self.threadedProcess)
        start_btn.grid(column=4, row=0, padx=[4, 4])

        # Select output directory
        output_btn = Button(
            middleframe, text="Select output directory", command=self.setOutputDirectory)
        output_btn.grid(column=3, row=0, padx=[20, 0])

        # Get working directory
        path_btn = Button(
            middleframe, text="Select the file or directory", command=self.getPath)
        path_btn.grid(column=1, row=0, padx=[20, 0])

        # Progress bar
        style = ttk.Style()
        style.theme_use('default')
        style.configure("black.Horizontal.TProgressbar", background='black')
        bar = ttk.Progressbar(bottomframe, length=text_width*6,
                              style='black.Horizontal.TProgressbar')
        bar.grid(column=0, row=1, padx=4, pady=4)

        # Execute GUI
        # threading.Thread(target=update).start()
        window.mainloop()


if __name__ == "__main__":
    GUI()
