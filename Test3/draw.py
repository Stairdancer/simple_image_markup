import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import json

dpi = 80
with open('annotations.json', 'r') as f:
    data = json.load(f)

def process_image(file_name):
    image = plt.imread(f'./persons/{file_name}')

    height, width, _ = image.shape
    figsize = width / float(dpi), height / float(dpi)
    fig = plt.figure(figsize=figsize)

    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.imshow(image, interpolation='nearest')

    boxes = data[f"{file_name}"]["objects"]
    rectangle_draw(ax, boxes)
    
    #Пересохраняем модифицированные файлы поверх старых:
    fig.savefig(f"./persons/{file_name}", dpi=dpi, transparent=True) 

def rectangle_draw(ax, boxes):
    for box in boxes:
        x = float(box["bbox"][0])
        y = float(box["bbox"][1])
        width = float(box["bbox"][2]) - x
        height = float(box["bbox"][3]) - y
        rect = patches.Rectangle((x,y), width, height, linewidth=2, edgecolor='b', facecolor='none')
        ax.add_patch(rect)

directory = "./persons"
for file in os.listdir(directory): 
    if (file.endswith(".jpg") or file.endswith(".jpeg")):
        process_image(file)