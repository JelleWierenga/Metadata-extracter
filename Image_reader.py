from PIL import Image
from PIL.ExifTags import TAGS
import os

def get_file_type(extension):
    file_types = {
        "images": [".jpg", ".jpeg", ".png", ".tiff", ".bmp", ".gif"],
        "videos": [".mp4", ".mov", ".avi", ".mkv"],
        "ms_office": [".docx", ".xlsx", ".pptx"],
        "pdfs": [".pdf"],
        "text": [".txt"],
    }

    for key, extensions in file_types.items():
        if extension in extensions:
            return key
    return None

# folder = "./images"
#
# for image in os.listdir(folder):
#     image = Image.open(f"images/{image}")
#     exif_data = image.getexif()
#     for tagid in exif_data:
#         tagname = TAGS.get(tagid, tagid)
#         value = exif_data.get(tagid)
#         print(f"{tagname}: {value}")
#     print("\n")



file_folder = "./files"
for file in os.listdir(file_folder):
    file_path = f"{file_folder}/{file}"
    extension = os.path.splitext(file)[1].lower()
    file_type = get_file_type(extension)
    if file_type:
        print(f"{file} is a {file_type} file with extension {extension}")

