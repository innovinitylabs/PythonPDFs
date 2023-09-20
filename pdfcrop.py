from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

reader = PdfReader('ml_primer.pdf')

writer = PdfWriter()

ro = RectangleObject((120, 70, 490, 700))

for page in reader.pages:
        
    page.cropbox = ro
    
    writer.add_page(page)

writer.write("cropped.pdf")
