from PIL import Image
import os

output_folder = input('Enter output_folder Name: ')
logo_name = input('Enter logo_name Name: ')

os.chdir('images')

if not os.path.isdir(output_folder):  # python create folder if not exists
   os.mkdir(output_folder)

for filename in os.listdir('.'):    #python code loop in folder file
    #print(filename)
    if filename.endswith(('.jpg','.png','.jp')):