import PyPDF2

input_pdf = PyPDF2.PdfFileReader(open("report.pdf", "rb"))
num_of_pages_per_file = 10000
doc_counter = 1
counter = 0
output = PyPDF2.PdfFileWriter()

for split_range in [range(input_pdf.numPages)[x:x + num_of_pages_per_file] for x in
                    range(0, input_pdf.numPages, num_of_pages_per_file)]:
    for _ in split_range:
        output.addPage(input_pdf.getPage(counter))
        counter = counter + 1
    print("Saving page %s / %s " % (counter, input_pdf.numPages))
    with open("report-%s.pdf" % doc_counter, "wb") as outputStream:
        output.write(outputStream)
        doc_counter = doc_counter + 1
        output = PyPDF2.PdfFileWriter()
