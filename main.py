import pyttsx3
import PyPDF2

# choose the pdf file 
book = open('book.pdf', 'rb')

# read the pdf file binary mode
pdfReader = PyPDF2.PdfFileReader(book)

# find number of pages in the pdf
pages = pdfReader.numPages

speaker = pyttsx3.init()
# set audio speed
speaker.setProperty('rate', 160)

#set audio volume
speaker.setProperty('volume', 180)

for num in range(15, pages-5):
    # read the pdf page
    page = pdfReader.getPage(num)

    # extract the texts of the pdf page
    text = page.extractText()

    # say method on the speaker that passing input text to be spoken
    speaker.say(text)
    # run and wait method to processes the voice commands
    speaker.runAndWait()