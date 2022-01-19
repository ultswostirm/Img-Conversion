#In this code we conert png image to jpg

from PIL import Image
import glob

for file in glob.glob("*.png"):
    img = Image.open(file)
    rgb_img = img.convert('RGB')
    rgb_img.save(file.replace("png", "jpg"), quality=95)
    
    
#check the files section after running the code for a jpg format photo of the png version