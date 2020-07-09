import sys
import os
from PIL import Image
#at argv[0] filename is used which is "JPGtoPNGconverter" in this case.
#grab first and second argument
path = sys.argv[1]
directory = sys.argv[2]


#check wher=ther new/exists, if not create it
if not os.path.exists(directory):
    os.makedirs(directory)


#loop through the pokedex
for filename in os.listdir(path):
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f'{path}{filename}')

  #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
  #convert images to png and save it to the new folder.
  img.save(f'{directory}/{clean_name}.png', 'png')
  print('all done!')