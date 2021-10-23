import PyPDF2

input_pdf = PyPDF2.PdfFileReader(open("report.pdf", "rb"))
num_of_pages_per_file = 20
doc_counter = 0
counter = 0
output = PyPDF2.PdfFileWriter()

for i in range(input_pdf.numPages):
    output.addPage(input_pdf.getPage(i))
    counter = counter + 1
    if counter == num_of_pages_per_file:
        with open("report-%s.pdf" % doc_counter, "wb") as outputStream:
            output.write(outputStream)
            doc_counter = doc_counter + 1
            counter = 0
            output = PyPDF2.PdfFileWriter()
