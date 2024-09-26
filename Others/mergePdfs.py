from PIL import Image
import glob
import os
os.chdir(r'F:\My Personal\Bhaskar Saripella Appl\CA appl\Work History\HCL\New_folder')
os.getcwd()
from PyPDF4 import PdfFileMerger


def mergePdfs():
    currentDir = r'F:\My Personal\Bhaskar Saripella Appl\CA appl\Work History\HCL\New_folder'
    pdfs = os.listdir(currentDir)

    merger = PdfFileMerger()
    pdf_files = ["1HCLEmploymentProofLetter.pdf", "2HCL Payments initial application emails with JD.pdf" ]
    # [merger.append(open(pdf, 'rb')) for pdf in pdf_files]
    for pdf in pdf_files:
        merger.append(r'F:\My Personal\Bhaskar Saripella Appl\CA appl\Work History\HCL\New_folder\\'+pdf)
    merger.write("new_file.pdf")

    # with open(os.path.join(exportDir+".pdf"),"wb") as fout:
    #     merger.write(fout)


# export_dir = r"F:\My Personal\Bhaskar Saripella Appl\CA appl\Work History\HCL\New Folder"
# input_dir = r"F:\My Personal\Bhaskar Saripella Appl\CA appl\Work History\HCL\New Folder"
# folders = os.listdir(input_dir)
# [mergePdfs(export_dir, input_dir,folder) for folder in folders]

if __name__ == "__main__":
    mergePdfs()



