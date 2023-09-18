from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

reader = PdfReader('ml_primer.pdf')

writer = PdfWriter()


for page in reader.pages:
    mb = page.mediabox
    mb.left, mb.bottom = (120, 70)
    mb.right, mb.top = (490, 700)
    page.cropbox = RectangleObject((mb.left, mb.bottom, mb.right, mb.top))
    page.scale_by(1.5)
    writer.add_page(page)

writer.write("cropped.pdf")
