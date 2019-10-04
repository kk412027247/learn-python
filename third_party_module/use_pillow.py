from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

im = Image.open('./test.jpeg')

w, h = im.size

print('Original image size: %sx%s' % (w, h))

im.thumbnail((w // 2, h // 2))
print('Resize image to: %sx%s' % (w // 2, h // 2))

im.save('./thumbnail.jpg', 'jpeg')


def rnd_char():
    return chr(random.randint(65, 90))


def rnd_color():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


def rnd_color_2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


width = 60 * 4

height = 60

image = Image.new('RGB', (width, height), (255, 255, 255))

font = ImageFont.truetype('/Library/Fonts/Arial Unicode.ttf', 36)

draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rnd_color())

for t in range(4):
    draw.text((60 * t + 10, 10), rnd_char(), font=font, fill=rnd_color_2())

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
