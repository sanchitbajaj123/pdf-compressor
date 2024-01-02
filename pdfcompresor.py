import tkinter as tk
from tkinter import filedialog
from tkinter import font as tkFont
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import webbrowser
import PyPDF2
import time

def compress(input_path,output_path):
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page.compress_content_streams()  
            pdf_writer.add_page(page)

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)
    for i in range(101):
        progress['value'] = i
        root.update()
        time.sleep(0.05)      
    webbrowser.open(output_path)


def browse():
    file_path = filedialog.askopenfilename(title="Select a PDF file", filetypes=[("PDF files", "*.pdf")])
    result = messagebox.askquestion("Confirmation", "Do you want to compress the PDF?")
    if result == 'yes':
        output_pdf = "output_compressed.pdf"
        compress(file_path,output_pdf)
def git():
    webbrowser.open('https://github.com/sanchitbajaj123')
root = tk.Tk()
root.title("PDF COMPRESSOR")
root.geometry("300x200")
root.configure(bg='grey')

lbl = tk.Label(root, text="SELECT PDF", bg="grey",fg='white',  height=2,font=('Times New Roman', 15, 'bold'))
lbl.pack()

button = tk.Button(root, text="BROWSE",bg="grey",fg='white', font=('Times New Roman', 12, 'bold'),command=browse)
button.pack()

progress = ttk.Progressbar(root, orient = HORIZONTAL,length = 250, mode = 'determinate')
progress.pack()

button2 = tk.Button(root, text="!MY GITHUB LINK!",bg="grey",fg='black', font=('Times New Roman', 15, 'bold'),bd=0, relief=tk.FLAT,command=git)
button2.pack()

root.mainloop()