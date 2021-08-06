from PIL import Image
import os.path
import glob


def convertjpg(jpgfile, outdir, width=600, height=500):
    img = Image.open(jpgfile)
    try:
        new_img = img.resize((width, height),Image.BILINEAR)
        new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
        print("Convert and save successfully!")
    except Exception as e:
        print(e)

fileDir = os.path.join(os.getcwd(),"resize")
print(fileDir)

jpgfiles = glob.glob(fileDir + r'\*.jpg')
print(jpgfiles)

outDir = os.path.join(os.getcwd(),"resize2")
print(outDir)

for jpgfile in jpgfiles:
    convertjpg(jpgfile, outDir)


