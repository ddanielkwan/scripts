from PIL import Image

filename = input("Enter file: ")

image1 = Image.open(f'{filename}.png')
im1 = image1.convert('RGB')
im1.save(f'{filename}.pdf')