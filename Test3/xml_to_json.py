import xml.dom.minidom
import json

dict = {} #Словарь, из которого впоследствии сделаем json-файл

markup = xml.dom.minidom.parse('annotations.xml')
images = markup.getElementsByTagName('image')

for image in images:
    image_name = image.attributes['name'].value
    dict[image_name] = {}
    dict[image_name]['objects'] = []

    boxes = image.getElementsByTagName('box')
    for box in boxes:
        x1 = box.attributes['xtl'].value
        y1 = box.attributes['xbr'].value
        x2 = box.attributes['ytl'].value
        y2 = box.attributes['ybr'].value
        dict[image_name]['objects'].append({"class": 'head', "bbox": [x1,x2,y1,y2]})

with open("annotations.json", "w") as f: #Подразумевается, что json-файл уже создан
    json.dump(dict , f, indent = 3, separators = (',', ':'))
