from PIL import Image
from PIL.ExifTags import TAGS
from prettytable import PrettyTable

image_filename = "image.jpg"

table = PrettyTable()

table.field_names = ["MetaTags", "Values"]

my_image = Image.open(image_filename)

img_exif_data = my_image.getexif()

for id in img_exif_data:
    tag_name = TAGS.get(id, id)
    data = img_exif_data.get(id)
    if isinstance(data, bytes):
        data = data.decode()

    table.add_row([tag_name, data])

print(table)