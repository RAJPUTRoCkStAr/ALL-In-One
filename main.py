# import subprocess #to make exe file work with this project
# subprocess.run("install_dependencies.bat", shell=True)

import webbrowser
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from pdf2docx.main import Converter
from docx2pdf import convert
import sounddevice
from scipy.io.wavfile import write
from PIL import Image
import rembg
import easyocr
from gtts import gTTS
import PyPDF2
import pyttsx3
# above are the module of differnt functions
def pdf2d():
    def pdf_to_docx():
        input_path = filedialog.askopenfilename(title='Open PDF file', filetypes=[("PDF File", "*.pdf")])
        if not input_path:
            return

        output_path = filedialog.asksaveasfilename(defaultextension='.docx', filetypes=[("Microsoft Word", "*.docx")])
        if not output_path:
            return

        cv = Converter(input_path)
        cv.convert(output_path)
        cv.close()
        status_label.config(text="Conversion successful!")

    pdfwindow = Tk()
    pdfwindow.title('PDF to DOCX Converter')
    pdfwindow.geometry('400x200')



    convert_button = Button(pdfwindow, text='Convert PDF to DOCX', command=pdf_to_docx)
    convert_button.pack(pady=20)

    status_label = Label(pdfwindow, text='', fg='green')
    status_label.pack(pady=10)

    pdfwindow.mainloop()



def backgroundremover():
    def rembimg():
        filepath = filedialog.askopenfilename(filetypes=[("image files","*.png *.jpg")])
        print(filepath)
        global bgimageremover
        bgimageremover = Image.open(filepath)

    def remimg():
        
        global image_without_bg 
        image_without_bg = rembg.remove(bgimageremover)

    def saveremimg():
        if image_without_bg is not None:
            filename = entry_filename.get() + '.png'
            image_without_bg.save(filename)
        else:
            print("Please remove the background first.")
    
    rembgwindow = Tk()
    rembgwindow.title('background image remover')
    rembgwindow.geometry('400x300')
    
    rembg_button = Button(rembgwindow, text='open image', command=rembimg)
    rembg_button.pack()
    
    rembg_button = Button(rembgwindow, text='remove bg', command=remimg)
    rembg_button.pack()

    entry_filename = Entry(rembgwindow, width=30)
    entry_filename.insert(0, "bgremove")
    entry_filename.pack()

    rembg_button = Button(rembgwindow, text='save', command=saveremimg)
    rembg_button.pack()
    
    rembgwindow.mainloop()


def image2text():
    def extract_text():
        filepath = filedialog.askopenfilename(title='Open Image File', filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if not filepath:
            return

        reader = easyocr.Reader(['en'])
        result = reader.readtext(filepath)

        extracted_text = ''
        for res in result:
            extracted_text += res[1] + ' '

        text_display.delete(1.0, END)  
        text_display.insert(END, extracted_text)


    ocrwindow = Tk()
    ocrwindow.title('Image Text Extractor')
    ocrwindow.geometry('500x300')


    extract_button = Button(ocrwindow, text='Extract Text', command=extract_text)
    extract_button.pack(pady=20)

    text_display = Text(ocrwindow, height=10, width=50)
    text_display.pack(pady=10)

    ocrwindow.mainloop()

def doc2f():
    def docx_to_pdf():
        input_path = filedialog.askopenfilename(title='Open DOCX file', filetypes=[("Microsoft Word", "*.docx")])
        if not input_path:
            return

        output_path = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=[("PDF File", "*.pdf")])
        if not output_path:
            return

        convert(input_path, output_path)
        status_label.config(text="Conversion successful!")


    docxwindow = Tk()
    docxwindow.title('DOCX to PDF Converter')
    docxwindow.geometry('400x200')


    convert_button = Button(docxwindow, text='Convert DOCX to PDF', command=docx_to_pdf)
    convert_button.pack(pady=20)

    status_label = Label(docxwindow, text='', fg='green')
    status_label.pack(pady=10)


    docxwindow.mainloop()


def soundda():
    def record_audio():
        seconds = int(entry_duration.get())
        sr = int(entry_samplerate.get())
        record_voice = sounddevice.rec(sr*seconds, samplerate=sr, channels=2)
        sounddevice.wait()
    
        filepath = filedialog.asksaveasfilename(defaultextension='.wav', filetypes=[("WAV File", "*.wav")])
        if filepath:
            write(filepath, sr, record_voice)
        status_label.config(text="Recording saved as WAV.")


    soundwindow = Tk()
    soundwindow.title('Audio Recorder')
    soundwindow.geometry('400x200')


    label_duration = Label(soundwindow, text='Recording Duration (seconds):')
    label_duration.pack(pady=5)
    entry_duration = Entry(soundwindow)
    entry_duration.pack(pady=5)
    entry_duration.insert(0, "5")  

    label_samplerate = Label(soundwindow, text='Sample Rate (Hz):')
    label_samplerate.pack(pady=5)
    entry_samplerate = Entry(soundwindow)
    entry_samplerate.pack(pady=5)
    entry_samplerate.insert(0, "44100")  

    record_button = Button(soundwindow, text='Record Audio', command=record_audio)
    record_button.pack(pady=20)

    status_label = Label(soundwindow, text='', fg='green')
    status_label.pack(pady=10)


    soundwindow.mainloop()



def texts():
    def create_audio():
        mytext = entry_text.get()
        language = entry_language.get()
        slow_speed = slow_var.get()

        myobj = gTTS(text=mytext, lang=language, slow=slow_speed)
    
        filepath = filedialog.asksaveasfilename(defaultextension='.mp3', filetypes=[("MP3 File", "*.mp3")])
        if filepath:
            myobj.save(filepath)
            status_label.config(text="Audio saved as MP3.")


    gttswindow = Tk()
    gttswindow.title('Text-to-Speech Audio Creator')
    gttswindow.geometry('500x300')


    label_text = Label(gttswindow, text='Enter Text:')
    label_text.pack(pady=5)
    entry_text = Entry(gttswindow, width=50)
    entry_text.pack(pady=5)

    label_language = Label(gttswindow, text='Language Code:')
    label_language.pack(pady=5)
    entry_language = Entry(gttswindow)
    entry_language.pack(pady=5)
    entry_language.insert(0, "en")  

    slow_var = BooleanVar()
    slow_check = Checkbutton(gttswindow, text='Slow Speed', variable=slow_var)
    slow_check.pack(pady=5)

    create_button = Button(gttswindow, text='Create Audio', command=create_audio)
    create_button.pack(pady=20)

    status_label = Label(gttswindow, text='', fg='green')
    status_label.pack(pady=10)

   
    gttswindow.mainloop()

def readers():

    def read_pdf_and_speak():
        filepath = filedialog.askopenfilename(title='Open PDF file', filetypes=[("PDF File", "*.pdf")])
        if not filepath:
            return

   
        with open(filepath, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)

            text = ''
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

   
            speak = pyttsx3.init()
   
            speak.say(text)
            speak.runAndWait()

    readerwindow = Tk()
    readerwindow.title('PDF Text-to-Speech Converter')
    readerwindow.geometry('400x200')



    convert_button =Button(readerwindow, text='Read PDF and Speak', command=read_pdf_and_speak)
    convert_button.pack(pady=20)


    readerwindow.mainloop()

def conta(event):
    webbrowser.open("https://github.com/RAJPUTRoCkStAr")

#above all are functions for the button below

window = Tk()
window.title('All in One')
window.geometry('500x500')

heading_label = ttk.Label(window, text='Find everything you want', font=('Helvetica', 20),foreground='lightgrey',background='purple')
heading_label.pack(pady=20)


a_button = ttk.Button(window, text='Pdf2docx', command=pdf2d, width=20)
a_button.pack(pady=10)

b_button = ttk.Button(window, text='Image_bgremover', command=backgroundremover, width=20)
b_button.pack(pady=10)

c_button = ttk.Button(window, text='Image2text', command=image2text, width=20)
c_button.pack(pady=10)

d_button = ttk.Button(window, text='Docx2pdf', command=doc2f, width=20)
d_button.pack(pady=10)

e_button = ttk.Button(window, text='Recording', command=soundda, width=20)
e_button.pack(pady=10)

f_button = ttk.Button(window, text='Textreader', command=texts, width=20)
f_button.pack(pady=10)

g_button = ttk.Button(window, text='Pdfreader', command=readers, width=20)
g_button.pack(pady=10)

contact_us_button = ttk.Button(window, text='Contact us',width=25)
contact_us_button.bind("<Button-1>", conta)
contact_us_button.pack(pady=10)

exit_button = ttk.Button(window, text='Exit', command=quit, width=25)
exit_button.pack(pady=10)


window.configure(bg='gray')


window.eval('tk::PlaceWindow . center')


window.mainloop()