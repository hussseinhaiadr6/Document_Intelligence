from pdf2image import convert_from_path
import os
from variables import get_path,get_poppler
path=get_path()
poppler_path = get_poppler()
def pdftoImages(Source_dir, Save_folder=""):
    os.makedirs(f"{path}/Task1/images", exist_ok=True)  # Create directory if it doesn't exist
    try:
        for root, dirs, files in os.walk(Source_dir):
            for filename in files:
                if filename.endswith(".pdf"):
                    os.mkdir(Save_folder + "/" + filename.split('.')[0])
                    print(filename)
                    images = convert_from_path(root+"/"+filename, poppler_path=poppler_path)
                    for i in range(len(images)):

                        images[i].save(Save_folder+'/'+filename.split('.')[0]+'/page' + str(i + 1) + '.jpg', 'JPEG')

    except FileNotFoundError:
        print("ERROR: Create a folder Called Images to continue in Task 1 Directory")

