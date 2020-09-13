import PyPDF2
import sys


def put_watermark(watermark_file, pdfs):
    """This function recieves file with watrmark and list of pdfs. Create new files with watermarked pages. 
    There is ability to get arguments from command line. First file is the watermakrk, 
    all following files are pdfs to be watermarked"""

    wm_reader = PyPDF2.PdfFileReader(open(watermark_file,'rb'))
    watermark_page = wm_reader.getPage(0)
    

    for pdf in pdfs:
        reader = PyPDF2.PdfFileReader(open(pdf, 'rb'))
        number_of_pages = reader.numPages
        writer = PyPDF2.PdfFileWriter()
        
        for page in range(number_of_pages):
            file_page = reader.getPage(page)
            file_page.mergePage(watermark_page)

            writer.insertPage(file_page, index=page)

            with open (f"watermarked_{pdf}", "wb") as new_wm_file:
                writer.write(new_wm_file)
    


if __name__ == "__main__":
    watermark = sys.argv[1]
    input_pdfs = sys.argv[2:]

    put_watermark(watermark, input_pdfs)
