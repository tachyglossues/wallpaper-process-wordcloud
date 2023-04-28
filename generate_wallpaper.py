import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_gradient_magnitude
import psutil
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import time
from screeninfo import get_monitors
from change_wallpaper import set_wallpaper





def get_running_processes():
	command_dict = {}
	for process in psutil.process_iter(['name', 'cpu_percent', 'memory_percent']): 
		command = process.info['name'].split('/')[0].replace(".exe", "") 
		cpu = process.info['cpu_percent']
		mem = process.info['memory_percent']
		if command in command_dict:
			command_dict[command][0] += cpu
			command_dict[command][1] += mem
		else:
			command_dict[command] = [cpu, mem]
	resource_dict = {}
	for command, [cpu, mem] in command_dict.items():
		resource_dict[command] = (cpu + mem)*10
	return resource_dict




def generate_wallpaper():
	if model != 0: 
		wallpaper_coloring = np.array(Image.open(imagesselect))  
		wallpaper_coloring = wallpaper_coloring[::2, ::2]
		wallpaper_mask = wallpaper_coloring.copy()  
		wallpaper_mask[wallpaper_mask.sum(axis=2) == 0] = 255
		edges = np.mean([gaussian_gradient_magnitude(wallpaper_coloring[:, :, i] / 255.0, 2)for i in range(2)],axis=0,) 
		wallpaper_coloring[edges > 1] = 255

		if color_ther ==2: 
			wc = WordCloud(mask=wallpaper_mask,background_color = background_colorg ,max_words=700,relative_scaling=0.4 ,repeat=True).generate_from_frequencies(get_running_processes())
			image_colors = ImageColorGenerator(wallpaper_coloring)
			wc.recolor(color_func=image_colors)
		else: 
			wc = WordCloud(mask=wallpaper_mask, background_color = background_colorg ,max_words=700,relative_scaling=0.4 ,repeat=True, colormap=chosen_palette).generate_from_frequencies(get_running_processes())
			
		wc.to_file("temp.png") 
		wordcloud = Image.open("temp.png")
		wallpaper = Image.new("RGB", (width, height), color = background_colorg) 
		wallpaper.paste(wordcloud,(int((width-wordcloud.size[0])/2),int((height - wordcloud.size[1])/ 2),),) 
		wallpaper.save("wallpaper.png")
	else: 
		wc = WordCloud(max_words=700,background_color = background_colorg,repeat=True,colormap=chosen_palette,width=width,height=height).generate_from_frequencies(get_running_processes())
		wc.to_file("wallpaper.png")
	print("wallpaper generated")
	
	
	
	
def is_valid_hex_color(color):
	if len(color)<2 or len(color)>7:
		return (False,None)
	if color[0] != '#': 
		color = "#" + color
	if (lencolor:=len(color)) == 4 or lencolor == 7 : 
		try:
			int(color[1:], 16)
			return (True,color)
		except ValueError:
			return (False,None)


infinity = False
color_palettes = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']  
current_dir = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

width, height = None, None 
for monitor in get_monitors(): 
	if monitor.x == 0 and monitor.y == 0:
		width = int(monitor.width)
		height = int(monitor.height)
		break

while True:

		try:
			mode = int(input("Choose the mode of operation of the program:\n- 0: predefined mode (can't change your wallpaper but will generate 'Wallpaper.png') \n- 1: customizable mode\n\nEnter the number corresponding to your choice:\t"))
			if mode in [0,1]: 
				break
			print("\nError: please enter an integer between 0 and 1.\n")	
		except ValueError:
			print("\nError: please enter an integer between 0 and 1.\n")	






if mode == 1:
	print("\n\n\n\nWelcome to the customizable mode\n\n")
	while True:
		try:
			model = int(input("Choose the type of word cloud :\n- 0: on the whole screen :\n- 1: a pre-installed model :\n- 2: a custom model that you have added in ./temp/ Enter the number corresponding to your choice :\t"))
			if model in [0,1,2]:
				break
			print("\nError: please enter an integer between 0 and 2\n")	
		except ValueError: 
			print("\nError: please enter an integer between 0 and 2\n")	
	print("\n"*7)
	if model != 0:
		if model == 2:
			folder_path = "temp/"
		else:
			folder_path = "model/"
		files = os.listdir(folder_path)
		images = [f for f in files if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg') ]
		if len(images) == 0: 
			print("Error: no image file found in the folder so the wallpaper will not have a template!!!")
			model = 0
			time.sleep(3) 
		else:	
			
			for i, image in enumerate(images):
				i = str(i+1)
				print(i + ': ' + image)
			try:
				chosen_number = int(input("Choose an image by entering its number: "))
				chosen_image = images[chosen_number-1]
			except ValueError:
				print("Error: please enter a number from the list.")
			print("Your choice " + chosen_image)
			imagesselect = folder_path + chosen_image
	print("\n"*7)
	while True:
		try:
			print("Choose the color palette of the word cloud:\n - 0: for a random color palette\n - 1: to choose from a pre-defined list of color palettes")
			permitted_value = [0,1]
			if model in [1,2]:	
				print("- 2: for the model's color palette")
				permitted_value.append(2)
			color_ther = int(input("\nEnter the number corresponding to your choice:\n"))
			if color_ther in permitted_value:
				break		   
			print("Error: value must be an allowed integer")
		except ValueError:
			print("Error: value must be an allowed integer")
	chosen_palette = "The model's one"
	if color_ther == 0: 
		chosen_palette = np.random.choice(color_palettes)
		time.sleep(1)
	elif color_ther == 1:
		for i, palette in enumerate(color_palettes):
			i = str(i+1)
			print('{:<3}'.format(i + ':' + palette), end=(25-(len(palette)+len(i)))*' ') 
			if int(i) % 7 == 0:
				print("")
		try:
			chosen_number = int(input("\nChoose a palette by entering its number: "))
			chosen_palette = color_palettes[chosen_number-1]
		except ValueError:
			print("Error: please enter a number from the list.")
	print("Selected color palette: " + chosen_palette)
	time.sleep(1)

	print("\n"*7)
	background_colorg = input("Enter a hexadecimal color for the background of the image (e.g. #000 -> black or #ffffff -> white): ") 
	try:
		while not is_valid_hex_color(background_colorg)[0]:	   
			print("Invalid hexadecimal color.")
			background_colorg = input("Enter a hexadecimal color for the background of the image (e.g. #000 -> black or #ffffff -> white): ")
	except ValueError:
		print("Invalid hexadecimal color.")
		
	background_colorg = is_valid_hex_color(background_colorg)[1]
	print("\n"*7)

	while True:  
		change_wallpaper = input("Do you want the program to automatically change your wallpaper? (yes/no): ").lower().replace(" ","") 
		if change_wallpaper in ["true","yes", "y"]:
			change_wallpaper = True
			break
		elif change_wallpaper in ["false","no", "n"]:
			change_wallpaper = False
			break
		print("Invalid answer")

	print("\n"*7)

	if change_wallpaper:
		while True:
			infinity= input("Do you want the wallpaper to be updated every X seconds? (yes/no): ").lower().replace(" ","") 
			if infinity in ["true","yes", "y"]:
				infinity = True
				print("\n"*7)
				break
			elif infinity in ["false","no", "n"]:
				infinity = False
				break 
			else :
				print("Invalid answer")

		
	if infinity:
		while True:
			try:
				delay = int(str(input("What delay in minutes between each wallpaper update (minimum 5min)? ")).replace("min","").replace(" ","").replace("minute","").replace("s",""))
				if delay > 4:
					delay *= 60
					break
				else:
					print("Error: delay must be greater than or equal to 5 minutes.")
			except ValueError:
				print("Error: delay must be greater than or equal to 5 minutes.")
		print("\n\n\n\n\nThe images will be generated")









	start_time = time.time() 
	generate_wallpaper()
	if change_wallpaper:
		set_wallpaper("Wallpaper.png")
	while True:
		end_time = time.time()
		execution_time = end_time - start_time
		time.sleep(delay-execution_time)
		start_time = time.time()
		generate_wallpaper()
		set_wallpaper("Wallpaper.png")
else: 
	print("\n\n\n\n\n\nWelcome to the predefined mode")
	while True:
		try:
			presets = int(input("Choose the model to use:\n- 0: Heart\n- 1: Windows\n- 2: Full Screen\n- 3: Kali\n\nEnter the number corresponding to your choice:\t"))
			if presets in [0,1,2,3]:
				break
			print("\nError: please enter an integer between 0 and 3.\n")
		except ValueError: #if the user's input is not an integer
			print("\nError: please enter an integer between 0 and 3.\n")	
			
	if presets == 0:
		model,imagesselect, color_ther,background_colorg  = 1, "model/heart.png", 2, "black"
	elif presets == 1:
		model,imagesselect, color_ther,background_colorg  = 1, "model/windows.png", 2, "black"
	elif presets ==	2:
		background_colorg, chosen_palette, model = None,  np.random.choice(color_palettes), 0
	else:
		model,imagesselect, color_ther,background_colorg  = 1, "model/dragon.png", 2, "black"
	print("the image will be generated\n\n")
	generate_wallpaper()
			
		
		
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
	
