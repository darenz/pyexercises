from PIL import Image
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`o. ")
ascii_char2 = list("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$???")


def getChar(r,g,b,alpha=256):
    if alpha==0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    step = 256.0/len(ascii_char2)
    return ascii_char2[int(gray/step)]

parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o','--output')
parser.add_argument('-r','--resize')
#parser.add_argument('--width',type=int,default=80)
#parser.add_argument('--height',type=int,default=40)

args = parser.parse_args()

IMG = args.file
OUTPUT = args.output
RESIZE = float(args.resize)

image = Image.open(IMG)
(WIDTH,HEIGHT) = image.size
#print(image.size)
#print(WIDTH)
#print(HEIGHT)

if RESIZE:
    HEIGHT = int(HEIGHT*RESIZE)
    WIDTH = 5*int(WIDTH*RESIZE)
    image = image.resize((WIDTH,HEIGHT),Image.NEAREST)

txt = ""

for i in range(HEIGHT):
    for j in range(WIDTH):
        txt += getChar(*image.getpixel((j,i)))
    txt += '\n'

print(txt)

if OUTPUT:
    with open(OUTPUT,'w') as f:
        f.write(txt)
else:
    with open('output.txt','w') as f:
        f.write(txt)
