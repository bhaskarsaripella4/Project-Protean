from PIL import Image
import glob
import os
os.chdir(r'F:')
os.getcwd()
import PyPDF4


# pdf1File = open(r'F:\My Personal\Office Claims\Haripriya Maternity Claim\RampBackForm\U4668439 first page.pdf','rb')
# pdf2File = open(r'F:\My Personal\Office Claims\Haripriya Maternity Claim\RampBackForm\U4668439 last page.pdf','rb')
#
# pdfWriter = PyPDF4.PdfFileWriter()
#
# pdfWriter.addPage(PyPDF4.PdfFileReader(pdf1File).getPage(0))
# pdfWriter.addPage(PyPDF4.PdfFileReader(pdf2File).getPage(0))
# pdfOutputFile = open(r'F:\My Personal\Office Claims\Haripriya Maternity Claim\RampBackForm\MergedFiles.pdf', 'wb')
# pdfWriter.write(pdfOutputFile)


# images = sorted(glob.glob(r'F:\My Personal\Bhaskar Saripella Appl\2_Offer Letters\3Frames\*.jpg'), key=os.path.getmtime)
images = glob.glob(r'F:\My Personal\Bhaskar Saripella Appl\2_Offer Letters\3Frames\*.jpg')
# images = glob.glob(r'F:\My Personal\Office Claims\Haripriya Maternity Claim\RampBackForm\blah\*.jpeg')
# images = glob.glob(r'C:\Users\HP\Downloads\10thPass.jpeg')
# images = glob.glob(r'F:\My Personal\Bank Statements Yes\Bhaskar 2022-23 tax\Nana\PPF\*.jpeg')
# images = sorted(images)
imgs = []
c = 0
for image in images:
    with open(image,'rb') as file:
        img = Image.open(file)
        if c == 0:
            first = img
            # first = first.rotate(180,expand=True)
            first = first.reduce(2)
        # if c>0 and c < 4:
        #     img = img.rotate(180,expand=True)
        img = img.convert('RGB')
        # if c==2:
        #     img = img.rotate(270, expand=True)
        # if c==7 or c==8:
        #     img = img.rotate(90,expand=True)
        img = img.reduce(2)
        imgs.append(img)
        c+=1

first.save(r'F:\My Personal\Bhaskar Saripella Appl\2_Offer Letters\3Frames\12112_Interest_Certificate_2023.pdf',save_all=True, append_images=imgs[1:])

# images.save(r'D:\My Personal\Office Claims\Haripriya Maternity Claim\ID Cards\UHCP_HP_ID.pdf'
#          ,save_all=True, append_images=[images])
#
# print(imgs)
# images = Image.open(r'D:\My Personal\Office Claims\Haripriya Maternity Claim\ID Cards\UHCP Peri Haripriya ID '
#                     r'Card.png').convert('RGB')
# # images.show()
#






# image1 = Image.open(r'D:\My Personal\Bank Statements Yes\Bhaskar 2021-22 tax\Nana\20210906_220215.jpg')
# image2 = Image.open(r'D:\My Personal\Bank Statements Yes\Bhaskar 2021-22 tax\Nana\20210906_220149.jpg')
# image1 =  image1.convert('RGB')
# image2 = image2.convert('RGB')
# # image2 = image2.rotate(-90)
# #
# # image = [image1,image2]
# #
# # image1.save(r'D:\My Personal\Bank Statements Yes\Bhaskar 2021-22 tax\Nana\PPF_Bhanumathi.pdf'
# #            , save_all = True, append_images=image)
