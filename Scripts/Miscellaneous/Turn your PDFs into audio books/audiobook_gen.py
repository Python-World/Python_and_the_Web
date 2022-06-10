import PyPDF2
import pyttsx3


def main(book, pg_no):
    pdf_Reader = PyPDF2.PdfFileReader(book)
    pages = pdf_Reader.numPages

    speaker = pyttsx3.init()

    for num in range((pg_no - 1), pages):
        page = pdf_Reader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()


if __name__ == "__main__":
    book = open(input("Enter the book name: "), "rb")
    pg_no = int(
        input(
            "Enter the page number from which you want the system to start reading text: "
        )
    )
    main(book, pg_no)
