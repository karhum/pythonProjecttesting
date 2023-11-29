from PIL import Image, ImageDraw, ImageFont
# all colors collected
# shapes collected, practise shapes
# how to use pillow: import, PIL or pillow?

img = Image.new(mode="RGB", size=(500, 300),
                   color = (120, 0, 225))



# text from user
# text = input("Please type something: \n")

fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 16)
d = ImageDraw.Draw(img)
d.text((50, 220), "text", font = fnt, fill = (255, 150, 0))

# white triangle
d.polygon([(400, 100), (200, 100), (300, 240)], fill = (255, 255, 255))

# blue circle
d.ellipse((250, 103, 350, 203), fill =(0, 75, 255))

img.save('pil_img.png')
