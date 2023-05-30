import json

import requests


def get_all_champs_info():
    url_all_champs = requests.get('http://ddragon.leagueoflegends.com/cdn/13.8.1/data/ru_RU/champion.json').json()
    data = url_all_champs['data']

    return list(data.values())

def get_champs_count():
    url_all_champs = requests.get('http://ddragon.leagueoflegends.com/cdn/13.8.1/data/ru_RU/champion.json').json()
    data = url_all_champs['data']

    return len(data)

def get_all_champs():
    all_champs = []
    champs = get_all_champs_info()
    for champ in champs:
        all_champs.append({
            'id': champ['id'],
            'name': champ['name'],
            'image': f'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/' + champ['id'] + '_0.jpg',
        })

    return all_champs

def get_detail_champ(champ_id):
    url_champ = f'http://ddragon.leagueoflegends.com/cdn/13.8.1/data/ru_RU/champion/{champ_id}.json'
    resp = requests.get(url_champ).json()
    data = resp['data']
    return list(data.values())[0]


def get_champ_splash_from_id(champ_id):
    champion = get_all_champs_info()[champ_id]
    champ_info = {
        'name': champion['name'],
        'splash': requests.get(f'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champion["id"]}_{0}.jpg').content,
        'splash_url': f'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champion["id"]}_{0}.jpg',
    }

    return champ_info

def get_champ_info(champ_id):
    champion = get_detail_champ(champ_id)
    url_skins = f'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/'
    url_spells = f'http://ddragon.leagueoflegends.com/cdn/13.8.1/img/spell/'
    url_passive = f'http://ddragon.leagueoflegends.com/cdn/13.8.1/img/passive/'

    all_champ_info = {
        # ДЕФОЛТНАЯ ИНФА
        'id': champion['id'],
        'name': champion['name'],
        'key': champion['key'],
        'title': champion['title'],
        'blurb': champion['blurb'],
        'lore': champion['lore'],
        'partype': champion['partype'],
        # ПЕРЕХОД В info
        'attack': champion['info']['attack'],
        'defense': champion['info']['defense'],
        'magic': champion['info']['magic'],
        'difficulty': champion['info']['difficulty'],
        # ПЕРЕХОД В image
        'sprite': f'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champion["id"]}_{0}.jpg',
        # ПЕРЕХОД В skins
        'skins': [f'{url_skins}{champion["id"]}_{champion["skins"][i]["num"]}.jpg' for i in range(len(champion['skins']))],
        # ПЕРЕХОД В allytips
        'alltips': champion['allytips'],
        # ПЕРЕХОД В enemytips
        'enemytips': champion['enemytips'],
        # ПЕРЕХОД В tags
        'tags': champion['tags'],
        # ПЕРЕХОД В stats
        'min_hp': champion['stats']['hp'],
        'max_hp': 17 * champion['stats']['hpperlevel'] + champion['stats']['hp'],
        'hpregen': champion['stats']['hpregen'],
        'hpregenperlevel': champion['stats']['hpregenperlevel'],
        'hpperlevel': champion['stats']['hpperlevel'],
        'min_mp': champion['stats']['mp'],
        'max_mp': 17 * champion['stats']['mpperlevel'] + champion['stats']['mp'],
        'mpperlevel': champion['stats']['mpperlevel'],
        'mpregen': champion['stats']['mpregen'],
        'mpregenperlevel': champion['stats']['mpregenperlevel'],
        'movespeed': champion['stats']['movespeed'],
        'armor': champion['stats']['armor'],
        'armorperlevel': champion['stats']['armorperlevel'],
        'spellblock': champion['stats']['spellblock'],
        'spellblockperlevel': champion['stats']['spellblockperlevel'],
        'attackrange': champion['stats']['attackrange'],
        'crit': champion['stats']['crit'],
        'critperevel': champion['stats']['critperlevel'],
        'attackdamage': champion['stats']['attackdamage'],
        'attackspeed': champion['stats']['attackspeed'],
        'attackdamageperlevel': champion['stats']['attackdamageperlevel'],
        'attackspeedperlevel': champion['stats']['attackspeedperlevel'],
        # ПЕРЕХОД В spells
        'spells': [{
            'id': champion['spells'][i]['id'],
            'name': champion['spells'][i]['name'],
            'description': champion['spells'][i]['description'],
            'costBurn': champion['spells'][i]['costBurn'],
            #'effectBurn': champion['spells'][i]['costBurn'],
            'cooldown': champion['spells'][i]['cooldownBurn'],
            'range': champion['spells'][i]['rangeBurn'],
            'image': url_spells + champion['spells'][i]['image']['full'],
        } for i in range(4)],
        # ПЕРЕХОД В passive
        'passive': {
            'name': champion['passive']['name'],
            'description': champion['passive']['description'],
            'image': url_passive + champion['passive']['image']['full'],
        },
    }
    return all_champ_info


def get_all_items():
    url = f'http://ddragon.leagueoflegends.com/cdn/13.8.1/data/ru_RU/item.json'
    url_image_item = f'http://ddragon.leagueoflegends.com/cdn/13.8.1/img/item/'
    resp = requests.get(url).json()
    data = resp['data']

    all_items = []
    inStoreFalse = []

    items = list(data.values())
    for item in items:
        try:
            inStoreFalse.append({
                'inStore': item['inStore'],
                'name': item['name'],
                'image': f"{url_image_item}{item['image']['full']}",
                'gold': item['gold']['total'],
                'sell': item['gold']['sell'],
                'tags': item['tags'],
                'stats': item['stats'],
            }
            )
        except:
            all_items.append({
                'name': item['name'],
                'image': f"{url_image_item}{item['image']['full']}",
                'gold': item['gold']['total'],
                'sell': item['gold']['sell'],
                'tags': item['tags'],
                'stats': item['stats']
            })
    return all_items


