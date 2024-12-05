import os
import shutil 

rt = os.path.expanduser("~/Téléchargements")
print(rt)
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"]
Img = os.path.join(rt, "Images")

if not os.path.exists(Img):
    os.makedirs(Img) 
    print('Dossier créé')
else:
    print("Le dossier existe déjà")

""" print(os.listdir(rt))
 """
for file in os.listdir(rt):
    filepath= os.path.join(rt , file)
    if os.path.isfile(filepath):
        for ext in image_extensions:
            if filepath.endswith(ext):
                shutil.move(filepath, Img)