# 1] install PyMuPDF
# 2] open file using fitz
import fitz
file = fitz.open('input.pdf')

# 3] extract text
for pagenumber, page in enumerate(file.pages(), start=1):
    text = page.getText()
    txt = open(f'openFile{pagenumber}.txt','a')

    txt.writelines(text)
    txt.close()

# 4] extract images
for pagenumber,page in enumerate(file.pages(), start=1):
    for imgNumber, img in enumerate(page.getImageList(), start=1):
        # address of where the image is present in the pdf
        xref = img[0]

        pix = fitz.Pixmap(file,xref)

        # pix.n = bytes per pixel
        # if pix.n value is greater than 4 then it is not an grey or rgb image -> So convert it into rgb
        if pix.n > 4:
            pix = fitz.Pixmap(fitz.csRGB,pix)

        pix.writePNG(f'image_page{pagenumber}_{imgNumber}.png')