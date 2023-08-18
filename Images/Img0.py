from PIL import Image as i

# importing image from desktop
img = i.open('C:/Users/HP/Downloads/Facebook_logo.jpeg')
with i.open('C:/Users/HP/Downloads/Facebook_logo.jpeg') as image:
    width, height = image.size
    print(width,height)
