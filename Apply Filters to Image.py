from PIL import Image, ImageFilter

def apply_filter("C:\xampp\htdocs\html\img\WhatsApp Image 2024-08-01 at 22.03.50_30342575.jpg", filter_typ):
    image = Image.open(image_path)
    if filter_type == 'BLUR':
        filtered_image = image.filter(ImageFilter.BLUR)
    elif filter_type == 'CONTOUR':
        filtered_image = image.filter(ImageFilter.CONTOUR)
    else:
        filtered_image = image
    filtered_image.show()