import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_gradient_magnitude
import json
from wordcloud import WordCloud, ImageColorGenerator
import re
import time


while True:
    d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    os.system("top -b -n 1 > top.out")
    configJSON = json.loads(open("config.json", "r").read())
    commandList = []
    with open("top.out", "r") as topFile:
        topOutput = topFile.read().split("\n")[7:]
        for line in topOutput[:-1]:
            line = re.sub(r'\s+', ' ', line).strip()
            fields = line.split(" ")
            try:
                if fields[11].count("/") > 0:
                    command = fields[11].split("/")[0]
                else:
                    command = fields[11]
                cpu = float(fields[8].replace(",", "."))
                mem = float(fields[9].replace(",", "."))
                if command != "top":
                    commandList.append((command, cpu, mem))
            except:
                pass
    commandDict = {}
    for command, cpu, mem in commandList:
        if command in commandDict:
            commandDict[command][0] += cpu
            commandDict[command][1] += mem
        else:
            commandDict[command] = [cpu + 1, mem + 1]
    resourceDict = {}
    for command, [cpu, mem] in commandDict.items():
        resourceDict[command] = (cpu+mem)
    try:
        width, height = ((os.popen("xrandr | grep '*'").read()).split()[0]).split("x")
        width = int(width)
        height = int(height)
    except:
        pass
    wallpaper_coloring = np.array(Image.open(os.path.join(d, "Wallpaper1.png")))
    wallpaper_coloring = wallpaper_coloring[::2, ::2]
    wallpaper_mask = wallpaper_coloring.copy()
    wallpaper_mask[wallpaper_mask.sum(axis=2) == 0] = 255
    edges = np.mean([gaussian_gradient_magnitude(wallpaper_coloring[:, :, i] / 255., 2) for i in range(2)], axis=0)
    wallpaper_mask[edges > 1] = 255
    wc = WordCloud(mask=wallpaper_mask, random_state=55).generate_from_frequencies(resourceDict)
    plt.imshow(wc)
    image_colors = ImageColorGenerator(wallpaper_coloring)
    wc.recolor(color_func=image_colors)
    wc.to_file('wc.png')
    wordcloud = Image.open("wc.png")
    wallpaper = Image.new('RGB', (width, height), configJSON["wordcloud"]["background"])
    wallpaper.paste(
        wordcloud,
        (int(width / 2 - wordcloud.size[0] / 2), int(height / 2 - wordcloud.size[1] / 2))
    )
    wallpaper.save("wallpaper.png")
    os.system("gsettings set org.gnome.desktop.background picture-uri file://" + os.path.join(d, "wallpaper.png"))
    os.system("rm top.out")
    os.system("rm wc.png")    
    time.sleep(configJSON["interval"]["refresh"])