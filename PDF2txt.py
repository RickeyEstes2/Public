from PyPDF2 import PdfReader

textFile = open('example.txt', 'w')
reader = PdfReader("example.pdf")
number_of_pages = len(reader.pages)

for x in range(number_of_pages):
    page = reader.pages[x]
    text = page.extract_text()
    print(text)
    print()
    textFile.write(text)
textFile.close()
