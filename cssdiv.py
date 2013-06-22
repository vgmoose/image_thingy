import Image, sys, string
from itertools import product

im = Image.open(sys.argv[1])
pix = im.load()
size = im.size

alphabet = list(string.lowercase)

bigolelist = []
for r in range(1, 5):
    for x in product(alphabet, repeat=r):
        bigolelist.append(''.join(x))

def to_argb(argb):
    return "".join(map(chr, argb)).encode('hex')

def to_rgb(rgb):
    return rgb[0:6]

def to_opacity(a):
    return int(a[6:8], 16)/255.0

def fake_trans(a):
    p = a[3]/255.0
    return to_rgb(to_argb(( int((1-p)*255 + p*a[0]), int((1-p)*255 + p*a[1]), int((1-p)*255 + p*a[2] ))))

def get_color(a):
    b = to_argb(a)
    if (len(b)==6):
        return b
    else:
        return fake_trans(a)

tag_count = -1

def get_tag():
    global tag_count
    tag_count+=1
    return bigolelist[tag_count]

colors = {}

print( "<style>."+get_tag()+"{height:1px;width:1px;float:left;}")

for x in range(0, size[1]):
    for y in range(0, size[0]):
        color = get_color(pix[y,x]);
        if not (color in colors):
            tag = get_tag()
            colors[color] = tag
            print("."+tag+"{background-color:"+color+";}")

print( "</style><div style='width:"+str(size[0])+"px;top:0;left:0;'>")
for x in range(0, size[1]):
    for y in range(0, size[0]):
        print("<div class='a "+colors[get_color(pix[y,x])]+"'></div>")
print "</div>"