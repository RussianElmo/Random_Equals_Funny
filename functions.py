import random
import urllib.request
from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup
import requests


def open_file(file_name):
    with open(file_name) as f:
        return f.readlines()


def add_to_file(file_name, new):
    with open(file_name, 'a') as f:
        f.write('\n' + new)


def get_caption():
    captions = open_file('Captions.txt')
    return random.choice(captions).upper()


def prepare_image(c):
    im = Image.open('meme.jpg')
    draw = ImageDraw.Draw(im)
    font_size = 45
    font = ImageFont.truetype("impact.ttf", font_size)
    width, height = im.size
    w, h = draw.textsize(c, font=font)

    x, y = (width - w) / 2, height - 100
    shadowcolor = 'black'

    draw.text((x - 1, y - 1), c, font=font, fill=shadowcolor)
    draw.text((x + 1, y - 1), c, font=font, fill=shadowcolor)
    draw.text((x - 1, y + 1), c, font=font, fill=shadowcolor)
    draw.text((x + 1, y + 1), c, font=font, fill=shadowcolor)
    draw.text((x, y), c, (255, 255, 255), font=font)

    im.save('meme.jpg')


def get_classes():
    image_queries = open_file('Images.txt')
    query = random.choice(image_queries)
    query = query.replace(' ', '+')
    page = urllib.request.urlopen('https://imgur.com/search?q=' + query)
    soup = BeautifulSoup(page, 'html.parser')
    classes = soup.find_all('a', {'class': 'image-list-link'})
    return classes


def get_image(classes):
    while len(classes) == 0:
        classes = get_classes()
    gallery_link = 'https://imgur.com' + random.choice(classes)['href']
    page = urllib.request.urlopen(gallery_link)
    soup = BeautifulSoup(page, 'html.parser')
    image_link = soup.find('meta', {'name': 'twitter:image'})['content']
    response = requests.get(image_link)
    file = open('meme.jpg', 'wb')
    file.write(response.content)
    file.close()
