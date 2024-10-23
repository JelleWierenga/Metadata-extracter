import os
from PIL import Image
from PIL.ExifTags import TAGS
from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["MetaTags", "Values"]

folder = "./images"
for image in os.listdir(folder):
    path = os.path.join(folder, image)

    my_image = Image.open(path)

    img_exif_data = my_image.getexif()

    for id in img_exif_data:
        tag_name = TAGS.get(id, id)
        data = img_exif_data.get(id)
        if isinstance(data, bytes):
            data = data.decode()

        table.add_row([tag_name, data])

    print(table)