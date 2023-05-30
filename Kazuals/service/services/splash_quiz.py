import random
from io import BytesIO

from PIL import Image

from champs.service.items_on_db import get_champ_splash_from_id, get_champs_count


def hard_level():
    champ_id = random.randint(0, get_champs_count() - 1)
    champ = get_champ_splash_from_id(champ_id)
    img = Image.open(BytesIO(champ['splash']))

    width, height = img.size

    square_size = 150

    sides = [(1, random.randint(1, height - square_size)),  # Левая сторона
             (random.randint(1, width - square_size), 1),  # Верхняя сторона
             (width - square_size, random.randint(1, height - square_size)),  # Правая сторона
             (random.randint(1, width - square_size), height - square_size)  # Нижняя сторона
             ]

    left, top = sides[random.randint(0, 3)]

    right = left + square_size
    bottom = top + square_size

    crop_img = img.crop((left, top, right, bottom))
    img_name = 'crop'
    crop_img.save(f'static/crop_img/{img_name}.jpg')

    return {'answer': champ['name'], 'splash': champ['splash_url'], 'img_name': img_name}


def easy_level():
    champ_id = random.randint(0, get_champs_count() - 1)
    champ = get_champ_splash_from_id(champ_id)
    img = Image.open(BytesIO(champ['splash']))

    width, height = img.size

    square_size = 150

    left = random.randint(square_size, width - square_size)
    top = random.randint(square_size, height - square_size)

    right = left + square_size
    bottom = top + square_size

    crop_img = img.crop((left, top, right, bottom))
    img_name = 'crop'
    crop_img.save(f'static/crop_img/{img_name}.jpg')

    return {'answer': champ['name'], 'splash': champ['splash_url'], 'img_name': img_name}
