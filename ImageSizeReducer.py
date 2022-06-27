import os
from PIL import Image
from zipfile import ZipFile  # If you also want to zip the folder

lookPath = 'Input_Images'  # Enter the folder path
outputPath = 'Output_Images'  # Enter the output folder path


def imageReducer(h, v):
    for folder, sub_folders, files in os.walk(lookPath):
        if (len(files) == 0):
            print(f"No files in the {lookPath} folder!")
            return
        for f in files:
            # print(f'{f}\n')
            img = Image.open(f'{lookPath}/{f}')
            img = img.resize((h, v))
            img.save(f'{outputPath}/{f}')
    print('Image Sizes Reduced!!!')


def zip():
    filePaths = []
    for folder, sub_folders, files in os.walk(outputPath):
        for f in files:
            # print(f'{f}\n')
            # filePath = f'{os.getcwd()}\{outputPath}\{f}'
            filePath = f'{outputPath}\{f}'
            filePaths.append(filePath)
    # print(os.getcwd())
    # print(filePaths)
    folder = f'{outputPath}.zip'
    with ZipFile(folder, 'w') as zip:
        for file in filePaths:
            zip.write(file)

    print('All files zipped successfully!')


def main():
    # First the image sizes will be reduced
    # e.g: 1240 x 720
    print("Image Resolution: ")
    width = int(input("Enter width: ")) # horizontal = 1240
    height = int(input("Enter height: ")) # vertical = 720
    imageReducer(width, height)

    # Secondly the images that are being reduced will be zipped
    zip() # comment it, if you don't want the program to zip the folder


if __name__ == "__main__":
    main()
