from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageEnhance
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`o. ")
ascii_char2 = list("$$$$$$$$$$$$$$RRRRRRRRRRRRRRRRRRR????????????????????^^^^^^^^^^^^^^^")

def getChar(r,g,b,alpha=256):
    if alpha==0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    step = 256.0/len(ascii_char2)
    return ascii_char2[int(gray/step)]

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('resize')
    parser.add_argument('-o','--output')
    #parser.add_argument('--width',type=int,default=80)
    #parser.add_argument('--height',type=int,default=40)
    args = parser.parse_args()
    # print(type(args))
    return args

def getIMG(*args, **kwargs):
    IMG = kwargs['file']
    RESIZE = float(kwargs['resize'])

    image = Image.open(IMG)
    image = image.resize((int(image.size[0]*RESIZE),int(image.size[1]*RESIZE)))
    # image.show()
    size = image.size
    # image.show()
    # input()
    return image,size

def convertTXT(img):
    HEIGHT = img.size[1]
    WIDTH = img.size[0]
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += '  ' + getChar(*img.getpixel((j,i)))
        txt += '\n'
    return txt

def outputTXT(OUTPUT,txt):
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open('output.txt','w') as f:
            f.write(txt)

if __name__ == "__main__":
    args = getArgs();
    img,size = getIMG(file=args.file,resize=args.resize)

    contr = ImageEnhance.Contrast(img)
    CONTRAST_FACTOR = 5
    img_con = contr.enhance(CONTRAST_FACTOR)
    img_con.show()
    # input()

    txt = convertTXT(img_con)

    new_size = (size[0]*20,size[1]*16)
    new_image = Image.new("RGB",size=new_size)

    dr = ImageDraw.Draw(new_image)
    # font = ImageFont.truetype("S2Glove.ttf")
    font = ImageFont.load_default()
    dr.text((0,0),txt,font=font)

    new_image.show()
    new_image.save('newpic.jpg')