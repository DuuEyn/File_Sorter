import os
import shutil


class sortDownloads():
  def __init__(self, file_list, sourcePath):
    self.file_list = file_list
    self.sourcePath = sourcePath

  def sortImgs(self, path):
    self.imgPath = path
    #If the destination directory does not exist, the function will create one.
    if not os.path.exists(self.imgPath):
      os.mkdir(self.imgPath) 
    for image in self.file_list:
      if not os.path.exists(f'{self.imgPath}/{image}'):
        shutil.move(f'{self.sourcePath}/{image}', self.imgPath)

  def sortPDFs(self, path):
    self.pdfPath = path
    #If the destination directory does not exist, the function will create one.
    if not os.path.exists(self.pdfPath):
      os.mkdir(self.pdfPath) 
    for pdfFile in self.file_list:
      if not os.path.exists(f'{self.pdfPath}/{pdfFile}'):
        shutil.move(f'{self.sourcePath}/{pdfFile}', self.pdfPath)

def sortFiles():
  #Source and destination directories. Change this if and when needed.
  sourcePath = 'Downloads'
  imgPath = 'Images'
  pdfPath = 'PDFs'
  
  file_list = os.listdir(sourcePath)
  imgs = []
  pdfs = []
  
  for file in file_list:
    #If statements below ensures that a file will not be moved
    #if a file with the same name already exists in the destination directory
    if file.endswith('.jpg') and not os.path.exists(f'{imgPath}/{file}'):
      imgs.append(file)
    elif file.endswith('.pdf') and not os.path.exists(f'{pdfPath}/{file}'):
      pdfs.append(file)
  if len(imgs) == 0 and len(pdfs) == 0:
    return "No new images and PDF files to sort"
  else: 
    #Creates a sortDownloads object then calls the relevant function to sort the files.
    imgSorter = sortDownloads(imgs, sourcePath)
    imgSorter.sortImgs(imgPath)
    pdfSorter = sortDownloads(pdfs, sourcePath)
    pdfSorter.sortPDFs(pdfPath)
  
    return 'All new images and PDFs in the Downloads folder have been sorted!'

print(sortFiles())
